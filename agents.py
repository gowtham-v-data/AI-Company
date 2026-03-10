"""
AI Company Agents Module
========================
Defines all five AI agents that form the AI company:
  - CEO Agent           → Strategy & Vision
  - Research Agent      → Market Analysis & Competitor Research
  - Developer Agent     → Product Code & MVP
  - Marketing Agent     → Ads, Social Media, SEO
  - Customer Support    → FAQ & Customer Replies

Uses CrewAI v1.x native LLM class with Groq (ultra-fast inference).
"""

from crewai import Agent, LLM
from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE


def _get_llm() -> LLM:
    """Return the shared Groq LLM instance for all agents."""
    return LLM(
        model=MODEL_NAME,
        api_key=GROQ_API_KEY,
        temperature=TEMPERATURE,
        max_tokens=8192,
    )


# ═══════════════════════════════════════════════════════════
#  1.  CEO AGENT
# ═══════════════════════════════════════════════════════════
def create_ceo_agent() -> Agent:
    return Agent(
        role="Chief Executive Officer (CEO)",
        goal=(
            "Understand the startup idea deeply, craft a compelling company vision, "
            "define a clear business strategy, build a product roadmap, and coordinate "
            "all other departments to bring the startup to life."
        ),
        backstory=(
            "You are a visionary serial entrepreneur who has built and exited three "
            "successful tech startups. You excel at turning vague ideas into concrete, "
            "actionable business plans. You think in terms of market fit, revenue models, "
            "and scalable growth. You communicate with clarity and inspire your team."
        ),
        llm=_get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=5,
    )


# ═══════════════════════════════════════════════════════════
#  2.  RESEARCH ANALYST AGENT
# ═══════════════════════════════════════════════════════════
def create_research_agent() -> Agent:
    return Agent(
        role="Research Analyst",
        goal=(
            "Conduct thorough market research, analyze competitors, identify target "
            "demographics, evaluate market size & demand, and uncover untapped "
            "opportunities for the startup."
        ),
        backstory=(
            "You are a senior market research analyst with 15 years of experience at "
            "top consulting firms like McKinsey and BCG. You know how to dissect any "
            "market, identify trends, quantify opportunity sizes, and present your "
            "findings in a way that drives strategic decisions. You are data-driven "
            "and always back up your claims."
        ),
        llm=_get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=5,
    )


# ═══════════════════════════════════════════════════════════
#  3.  DEVELOPER AGENT
# ═══════════════════════════════════════════════════════════
def create_developer_agent() -> Agent:
    return Agent(
        role="Full-Stack Developer",
        goal=(
            "Design the product architecture, generate clean production-ready code "
            "for the MVP, build a professional landing page, and outline the technical "
            "roadmap for future development."
        ),
        backstory=(
            "You are a 10x developer who has shipped products used by millions. You "
            "specialize in Python, JavaScript, React, and modern web technologies. "
            "You write clean, well-documented code and think about scalability from "
            "day one. You can generate complete, functional code ready to deploy."
        ),
        llm=_get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=5,
    )


# ═══════════════════════════════════════════════════════════
#  4.  MARKETING MANAGER AGENT
# ═══════════════════════════════════════════════════════════
def create_marketing_agent() -> Agent:
    return Agent(
        role="Marketing Manager",
        goal=(
            "Develop a comprehensive go-to-market strategy, create engaging social "
            "media content for LinkedIn and Instagram, write persuasive ad copy, "
            "develop an SEO-optimized blog post, and plan a launch campaign."
        ),
        backstory=(
            "You are a growth marketing expert with a track record of taking startups "
            "from 0 to 100k users. You understand content marketing, paid ads, SEO, "
            "social media virality, and brand positioning. You write copy that converts "
            "and create campaigns that go viral."
        ),
        llm=_get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=5,
    )


# ═══════════════════════════════════════════════════════════
#  5.  CUSTOMER SUPPORT AGENT
# ═══════════════════════════════════════════════════════════
def create_customer_support_agent() -> Agent:
    return Agent(
        role="Customer Support Lead",
        goal=(
            "Anticipate common customer questions, create a comprehensive FAQ, "
            "draft professional customer response templates, and design a feedback "
            "collection system for the startup."
        ),
        backstory=(
            "You are a customer experience specialist who has managed support for "
            "SaaS products with 500k+ users. You know every trick to make customers "
            "feel heard and valued. You write empathetic, clear responses and build "
            "self-service knowledge bases that reduce ticket volume by 60%."
        ),
        llm=_get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=5,
    )
