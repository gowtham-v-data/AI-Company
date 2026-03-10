"""
Configuration module for the AI Company system.
Loads environment variables and provides shared config.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ── API Keys ──────────────────────────────────────────────
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# ── Model Configuration ──────────────────────────────────
# llama-3.1-8b-instant has 131k TPM on Groq free tier (vs 12k for 70b)
MODEL_NAME = "groq/llama-3.1-8b-instant"
TEMPERATURE = 0.4
MAX_OUTPUT_TOKENS = 8192
AGENT_DELAY_SECONDS = 15  # Pause between agents to avoid rate limits

# ── Output Directory ─────────────────────────────────────
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Validation ────────────────────────────────────────────
def validate_config():
    """Validate that all required configuration is present."""
    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY not set. "
            "Create a .env file with GROQ_API_KEY='your_key_here'"
        )
    return True
