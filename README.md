# 🏢 AI Company — Multi-Agent Startup Engine

> **Where AI Agents Run Your Entire Business**

A system where **5 AI agents** collaborate using CrewAI to automatically run a startup — from strategy to code to marketing to customer support.

---

## 🧠 How It Works

1. **You provide a startup idea** → e.g., *"Create a startup that sells AI study tools for students"*
2. **5 AI agents go to work** → Each agent handles a specific department
3. **You receive complete deliverables** → Business plan, code, marketing content, and more

### 🤖 The AI Team

| Agent | Role | Output |
|-------|------|--------|
| 👔 **CEO** | Business Strategy & Vision | Company vision, roadmap, revenue model |
| 🔬 **Research Analyst** | Market Analysis | Competitor analysis, SWOT, market sizing |
| 💻 **Developer** | Product & Code | Landing page, MVP spec, tech architecture |
| 📢 **Marketing Manager** | Go-to-Market | Social posts, ads, SEO blog, email campaigns |
| 🎧 **Customer Support** | Customer Experience | FAQ, response templates, feedback system |

---

## 🏗 Architecture

```
User Input
     ↓
CEO Agent → Business Strategy
     ↓
Research Agent → Market Analysis
     ↓
Developer Agent → Product Code
     ↓
Marketing Agent → Campaigns & Content
     ↓
Support Agent → FAQ & Responses
     ↓
📊 Dashboard (Streamlit)
📡 API (FastAPI)
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd AI-Company
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file:
```env
GOOGLE_API_KEY="your_google_api_key_here"
```

### 3. Run — Option A: Streamlit Dashboard (Recommended)

```bash
streamlit run app.py
```

### 3. Run — Option B: FastAPI + Dashboard

Start the API server:
```bash
uvicorn api:app --reload --port 8000
```

Then in a separate terminal:
```bash
streamlit run app.py
```

### 3. Run — Option C: Command Line

```bash
python crew.py
```

---

## 🧰 Tech Stack

- **[CrewAI](https://www.crewai.com/)** — Multi-agent orchestration
- **[LangChain](https://python.langchain.com/)** — LLM framework
- **[Google Gemini](https://ai.google.dev/)** — AI model (gemini-2.0-flash)
- **[FastAPI](https://fastapi.tiangolo.com/)** — REST API backend
- **[Streamlit](https://streamlit.io/)** — Interactive dashboard
- **Python 3.10+** — Programming language

---

## 📁 Project Structure

```
AI-Company/
├── agents.py          # Agent definitions (CEO, Research, Dev, Marketing, Support)
├── tasks.py           # Task definitions for each agent
├── crew.py            # CrewAI orchestrator + CLI entry point
├── api.py             # FastAPI backend
├── app.py             # Streamlit dashboard
├── config.py          # Configuration & environment
├── requirements.txt   # Python dependencies
├── .env               # API keys (create this!)
├── .env.example       # Example env file
└── outputs/           # Generated results (auto-created)
```

---

## 📊 Example Output

For the input: *"Create an AI productivity tool"*

The system generates:

1. ✅ **Business Plan** — Vision, mission, revenue model, 6-month roadmap
2. ✅ **Market Research** — TAM/SAM/SOM, competitor analysis, SWOT
3. ✅ **Product Code** — Landing page HTML/CSS/JS, tech architecture
4. ✅ **Marketing Campaign** — LinkedIn posts, Instagram ads, SEO blog
5. ✅ **Customer Support** — FAQ, response templates, feedback survey

All results are downloadable as Markdown files from the dashboard.

---

## 📝 License

MIT License — feel free to use, modify, and build upon this project.
