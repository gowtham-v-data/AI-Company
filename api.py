"""
AI Company — FastAPI Backend
=============================
REST API to trigger the AI company pipeline and retrieve results.

Endpoints:
  POST /api/run          → Start a new company run
  GET  /api/status/{id}  → Check run status
  GET  /api/results/{id} → Get run results
  GET  /api/history      → List all past runs
"""

import os
import json
import uuid
import threading
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from crew import run_company
from config import OUTPUT_DIR

# Path to the frontend directory
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend")

# ── App Setup ────────────────────────────────────────────
app = FastAPI(
    title="🏢 AI Company API",
    description="Multi-agent AI startup engine powered by CrewAI & Gemini",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── In-memory job store ──────────────────────────────────
jobs: dict = {}


# ── Models ───────────────────────────────────────────────
class RunRequest(BaseModel):
    startup_idea: str


class RunResponse(BaseModel):
    job_id: str
    status: str
    message: str


class JobStatus(BaseModel):
    job_id: str
    status: str
    startup_idea: str
    started_at: str
    completed_at: Optional[str] = None
    error: Optional[str] = None


# ── Background Runner ────────────────────────────────────
def _run_in_background(job_id: str, startup_idea: str):
    """Execute the company pipeline in a background thread."""
    try:
        jobs[job_id]["status"] = "running"
        results = run_company(startup_idea)
        jobs[job_id]["status"] = "completed"
        jobs[job_id]["completed_at"] = datetime.now().isoformat()
        jobs[job_id]["results"] = {
            k: v for k, v in results.items() if k != "_metadata"
        }
        jobs[job_id]["output_dir"] = results.get("_metadata", {}).get("output_dir", "")
    except Exception as e:
        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"] = str(e)
        jobs[job_id]["completed_at"] = datetime.now().isoformat()


# ── Endpoints ────────────────────────────────────────────
@app.post("/api/run", response_model=RunResponse)
async def start_run(request: RunRequest):
    """Start a new AI company run with the given startup idea."""
    job_id = str(uuid.uuid4())[:8]

    jobs[job_id] = {
        "job_id": job_id,
        "status": "queued",
        "startup_idea": request.startup_idea,
        "started_at": datetime.now().isoformat(),
        "completed_at": None,
        "results": None,
        "error": None,
        "output_dir": "",
    }

    thread = threading.Thread(
        target=_run_in_background,
        args=(job_id, request.startup_idea),
        daemon=True,
    )
    thread.start()

    return RunResponse(
        job_id=job_id,
        status="queued",
        message=f"AI Company is now working on: '{request.startup_idea}'",
    )


@app.get("/api/status/{job_id}", response_model=JobStatus)
async def get_status(job_id: str):
    """Check the status of a running job."""
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = jobs[job_id]
    return JobStatus(
        job_id=job["job_id"],
        status=job["status"],
        startup_idea=job["startup_idea"],
        started_at=job["started_at"],
        completed_at=job["completed_at"],
        error=job["error"],
    )


@app.get("/api/results/{job_id}")
async def get_results(job_id: str):
    """Get the full results of a completed job."""
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = jobs[job_id]
    if job["status"] != "completed":
        return {
            "job_id": job_id,
            "status": job["status"],
            "message": "Job has not completed yet." if job["status"] != "failed"
                       else f"Job failed: {job['error']}",
        }

    return {
        "job_id": job_id,
        "status": "completed",
        "startup_idea": job["startup_idea"],
        "results": job["results"],
    }


@app.get("/api/history")
async def get_history():
    """List all past runs."""
    history = []
    for job_id, job in jobs.items():
        history.append({
            "job_id": job["job_id"],
            "status": job["status"],
            "startup_idea": job["startup_idea"],
            "started_at": job["started_at"],
            "completed_at": job["completed_at"],
        })
    return {"runs": history}


@app.get("/")
async def root():
    """Serve the frontend."""
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))


# Mount static files LAST (so API routes take priority)
app.mount("/css", StaticFiles(directory=os.path.join(FRONTEND_DIR, "css")), name="css")
app.mount("/js", StaticFiles(directory=os.path.join(FRONTEND_DIR, "js")), name="js")
