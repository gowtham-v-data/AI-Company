"""
AI Company Tasks Module
=======================
Defines the specific tasks assigned to each agent.
Each task has a description, expected output, and assigned agent.
"""

from crewai import Task


def create_ceo_task(agent, startup_idea: str) -> Task:
    """CEO: Create business strategy and product roadmap."""
    return Task(
        description=(
            f"You are the CEO of a brand-new startup. The founder has given you this idea:\n\n"
            f'"{startup_idea}"\n\n'
            f"Your job is to:\n"
            f"1. Deeply understand and refine the idea\n"
            f"2. Define the company vision and mission statement\n"
            f"3. Identify the target audience\n"
            f"4. Outline the revenue model (how will this make money?)\n"
            f"5. Create a 6-month product roadmap with milestones\n"
            f"6. List the key departments and their immediate priorities\n"
            f"7. Identify potential risks and mitigation strategies\n\n"
            f"Be specific, actionable, and think like a YC-funded startup CEO."
        ),
        expected_output=(
            "A comprehensive business strategy document with:\n"
            "- Company Name & Tagline\n"
            "- Vision & Mission\n"
            "- Target Audience Profile\n"
            "- Revenue Model\n"
            "- 6-Month Roadmap with milestones\n"
            "- Department priorities\n"
            "- Risk Assessment"
        ),
        agent=agent,
    )


def create_research_task(agent, startup_idea: str) -> Task:
    """Research Agent: Conduct market analysis."""
    return Task(
        description=(
            f"Conduct comprehensive market research for a startup based on this idea:\n\n"
            f'"{startup_idea}"\n\n'
            f"Your research must cover:\n"
            f"1. Market Size & Growth (TAM, SAM, SOM estimates)\n"
            f"2. Top 5 competitors — their strengths, weaknesses, pricing\n"
            f"3. Target customer demographics & psychographics\n"
            f"4. Market trends and emerging opportunities\n"
            f"5. Potential entry barriers\n"
            f"6. Regulatory or compliance considerations\n"
            f"7. SWOT analysis for the startup\n\n"
            f"Present your findings in a professional market research report format."
        ),
        expected_output=(
            "A detailed market research report containing:\n"
            "- Executive Summary\n"
            "- Market Size Analysis (TAM/SAM/SOM)\n"
            "- Competitor Analysis Table\n"
            "- Customer Persona Profiles\n"
            "- Market Trends & Opportunities\n"
            "- SWOT Analysis\n"
            "- Strategic Recommendations"
        ),
        agent=agent,
    )


def create_developer_task(agent, startup_idea: str) -> Task:
    """Developer Agent: Build product prototype & landing page."""
    return Task(
        description=(
            f"You are the lead developer for a new startup:\n\n"
            f'"{startup_idea}"\n\n'
            f"Your deliverables:\n"
            f"1. Technical Architecture — what technologies to use, system design\n"
            f"2. MVP Feature List — core features for the first release\n"
            f"3. Landing Page Code — a complete, beautiful HTML/CSS/JS landing page\n"
            f"   - Must include: hero section, features, pricing, testimonials, CTA\n"
            f"   - Use modern design (gradients, animations, responsive)\n"
            f"4. Backend API outline — key endpoints and data models\n"
            f"5. Database schema suggestion\n"
            f"6. Technical roadmap for next 3 months\n\n"
            f"Provide complete, production-ready code for the landing page."
        ),
        expected_output=(
            "A technical deliverable package containing:\n"
            "- Technical Architecture Document\n"
            "- MVP Feature List\n"
            "- Complete Landing Page (HTML/CSS/JS code)\n"
            "- Backend API Design\n"
            "- Database Schema\n"
            "- Technical Roadmap"
        ),
        agent=agent,
    )


def create_marketing_task(agent, startup_idea: str) -> Task:
    """Marketing Agent: Create go-to-market strategy & content."""
    return Task(
        description=(
            f"Create a full marketing strategy for this startup:\n\n"
            f'"{startup_idea}"\n\n'
            f"Deliver the following:\n"
            f"1. Brand Positioning Statement\n"
            f"2. Go-to-Market Strategy (launch plan, channels, timeline)\n"
            f"3. 5 LinkedIn posts (professional, thought-leadership style)\n"
            f"4. 5 Instagram ad captions (engaging, emoji-rich, with hashtags)\n"
            f"5. 1 SEO blog article (1000+ words, keyword-optimized)\n"
            f"6. Email launch sequence (3 emails: teaser, launch, follow-up)\n"
            f"7. Paid advertising strategy (budget allocation, platforms, targeting)\n\n"
            f"Make all content ready to publish. Be creative and conversion-focused."
        ),
        expected_output=(
            "A complete marketing package containing:\n"
            "- Brand Positioning\n"
            "- Go-to-Market Strategy\n"
            "- 5 LinkedIn Posts (ready to publish)\n"
            "- 5 Instagram Ad Captions\n"
            "- 1 SEO Blog Article\n"
            "- 3-Email Launch Sequence\n"
            "- Paid Ad Strategy"
        ),
        agent=agent,
    )


def create_support_task(agent, startup_idea: str) -> Task:
    """Customer Support Agent: Create FAQ & response templates."""
    return Task(
        description=(
            f"You are setting up customer support for a new startup:\n\n"
            f'"{startup_idea}"\n\n'
            f"IMPORTANT RULES:\n"
            f"- You MUST invent a real, creative startup name based on the idea. NEVER write [Startup Name] or any [placeholder] brackets.\n"
            f"- Fill in ALL values: use a real company name, real sample user names (e.g. 'Sarah'), real email (e.g. support@companyname.com), real phone (e.g. +1-800-555-1234).\n"
            f"- NEVER leave any square brackets [ ] in your output. Every field must have a concrete value.\n\n"
            f"Create the following:\n"
            f"1. Comprehensive FAQ (at least 15 questions & answers)\n"
            f"   - Categories: Product, Pricing, Technical, Account, General\n"
            f"   - Use the actual startup name in every answer\n"
            f"2. 10 customer response templates for common scenarios:\n"
            f"   - Welcome message, refund request, bug report, feature request,\n"
            f"     billing inquiry, positive review response, negative review response,\n"
            f"     onboarding help, account issue, cancellation\n"
            f"   - Use realistic sample customer names, not [User Name]\n"
            f"   - Sign off with a realistic support team name, not [Your Name]\n"
            f"3. Feedback collection survey (5 questions)\n"
            f"4. Customer success onboarding checklist\n"
            f"5. Escalation policy (when to escalate, to whom)\n\n"
            f"All responses should be empathetic, professional, and brand-aligned.\n"
            f"REMINDER: Zero placeholders. Every name, email, phone number must be filled in with realistic values."
        ),
        expected_output=(
            "A complete customer support package with ALL placeholder values filled in "
            "(no square brackets anywhere) containing:\n"
            "- FAQ Document (15+ Q&As categorized)\n"
            "- 10 Response Templates (with real names, emails, phone numbers)\n"
            "- Feedback Survey\n"
            "- Onboarding Checklist\n"
            "- Escalation Policy"
        ),
        agent=agent,
    )
