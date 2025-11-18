import streamlit as st
from dataclasses import dataclass, asdict
from datetime import datetime
import uuid

# ---------- Page setup ----------

st.set_page_config(
    page_title="Senior Intern – Startup Problem",
    page_icon="🚀",
    layout="centered"
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 34px !important;
        font-weight: 700 !important;
        padding: 0.4rem 0 0.2rem 0;
    }
    .sub-title {
        font-size: 16px !important;
        color: #444444;
        padding-bottom: 0.8rem;
    }
    .thankyou-card {
        background: linear-gradient(120deg, #fff3e0, #e3f2fd);
        padding: 2rem 2.5rem;
        border-radius: 18px;
        border: 1px solid #ffe0b2;
        text-align: center;
    }
    .thankyou-title {
        font-size: 26px;
        font-weight: 700;
        color: #e65100;
        margin-bottom: 0.7rem;
    }
    .thankyou-text {
        font-size: 16px;
        color: #2d3436;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Data model ----------

@dataclass
class FounderProblem:
    id: str
    founder_name: str
    founder_email: str
    company_name: str
    company_one_liner: str
    main_problem_one_line: str
    impact_areas: list
    why_exists: list
    what_tried: list
    urgency: int
    company_stage: str
    detailed_description: str
    created_at: str


def build_ai_text(p: FounderProblem) -> str:
    return f"""
Startup problem:

Founder: {p.founder_name} ({p.founder_email})
Company: {p.company_name}
One-liner: {p.company_one_liner}

Main problem (one line):
{p.main_problem_one_line}

Impact areas: {", ".join(p.impact_areas)}

Why the founder thinks this problem exists:
{", ".join(p.why_exists)}

What they have tried so far:
{", ".join(p.what_tried)}

Urgency (1-10): {p.urgency}
Company stage: {p.company_stage}

Detailed description:
{p.detailed_description}
"""

# ---------- Session state ----------

if "problem" not in st.session_state:
    st.session_state.problem = None
if "problem_ai_text" not in st.session_state:
    st.session_state.problem_ai_text = ""

# ==========================================================
# VIEW 1: FORM – FOUNDER DESCRIBES PROBLEM
# ==========================================================

if st.session_state.problem is None:
    st.markdown(
        '<div class="main-title">Describe Your Startup Problem</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-title">Answer a few questions so our Virtual Senior Advisory Board can analyse your situation and match you with the right senior expert.</div>',
        unsafe_allow_html=True,
    )

    with st.form("founder_problem_form"):
        founder_name = st.text_input("Your name *")
        founder_email = st.text_input("Email *")
        company_name = st.text_input("Startup / Company name (optional)")
        company_one_liner = st.text_input(
            "Describe your business in one line *",
            placeholder="Ex: We are a SaaS platform helping small retailers manage inventory."
        )

        main_problem_one_line = st.text_input(
            "In one sentence, what is the main problem you're facing? *",
            placeholder="Ex: We don’t have repeat customers."
        )

        impact_areas = st.multiselect(
            "Where is this problem hurting you the most? *",
            options=[
                "Revenue / Sales",
                "Growth / New customers",
                "Customer satisfaction",
                "Operations / Delivery",
                "Team clarity / morale",
                "Cashflow / Runway",
                "Other"
            ],
        )

        why_exists = st.multiselect(
            "Why do you think this problem exists? (be honest) *",
            options=[
                "Lack of experience in this area",
                "Limited budget",
                "Weak or unclear strategy",
                "Poor execution / follow-through",
                "No mentor / guidance",
                "Team too junior",
                "Wrong product positioning",
                "Not talking enough to customers",
                "Low sales experience",
                "Market might not be right",
                "I am not sure",
                "Other"
            ],
        )

        what_tried = st.multiselect(
            "What have you already tried so far? *",
            options=[
                "Paid ads / performance marketing",
                "Content or social media marketing",
                "Discounts / offers",
                "Changing pricing",
                "Hiring new people",
                "Talking to customers",
                "Changing the product",
                "Nothing yet",
                "Other"
            ],
        )

        urgency = st.slider(
            "How urgent is this problem? (1 = low, 10 = critical) *",
            min_value=1,
            max_value=10,
            value=7,
        )

        company_stage = st.selectbox(
            "What stage is your startup at? *",
            ["Idea", "Prototype", "MVP", "Early revenue", "Scaling"]
        )

        detailed_description = st.text_area(
            "In 3–5 lines, describe the situation in more detail. *",
            placeholder="Ex: We acquired 500 users in 6 months but very few come back. We aren’t sure if it’s pricing, product, or positioning...",
            height=140,
        )

        submitted = st.form_submit_button("Analyse my problem")

    if submitted:
        if not (
            founder_name
            and founder_email
            and company_one_liner
            and main_problem_one_line
            and impact_areas
            and why_exists
            and what_tried
            and detailed_description
        ):
            st.error("Please fill all required fields marked with *.")
        else:
            problem = FounderProblem(
                id=str(uuid.uuid4()),
                founder_name=founder_name,
                founder_email=founder_email,
                company_name=company_name,
                company_one_liner=company_one_liner,
                main_problem_one_line=main_problem_one_line,
                impact_areas=impact_areas,
                why_exists=why_exists,
                what_tried=what_tried,
                urgency=urgency,
                company_stage=company_stage,
                detailed_description=detailed_description,
                created_at=datetime.utcnow().isoformat(),
            )

            st.session_state.problem = problem
            st.session_state.problem_ai_text = build_ai_text(problem)
            st.rerun()

# ==========================================================
# VIEW 2: MOCK AI – VIRTUAL BOARD + MATCHED SENIORS
# ==========================================================

else:
    p: FounderProblem = st.session_state.problem

    # --- Mock senior “database” ---
    mock_seniors = [
        {
            "name": "Anita Rao",
            "headline": "Ex-COO, 25+ yrs in Retail & Operations",
            "strengths": ["Operations & Execution", "Turnaround / Crisis", "People & Culture"],
            "fit_reason": "She has led multiple retail turnarounds where repeat customers and store-level execution were the main issues.",
        },
        {
            "name": "Vikram Mehta",
            "headline": "Ex-CPO, B2B SaaS & Product Strategy",
            "strengths": ["Product & UX", "Strategy & Direction", "Growth / New customers"],
            "fit_reason": "He’s scaled SaaS products from MVP to thousands of paying customers and knows how to fix retention and positioning problems.",
        },
        {
            "name": "Sara Al Mansoori",
            "headline": "Ex-CFO, 20+ yrs in Finance & Unit Economics",
            "strengths": ["Finance & Unit Economics", "Cashflow / Runway"],
            "fit_reason": "She is ideal when pricing, margins, or runway are the hidden reason behind a growth or retention issue.",
        },
    ]

    # --- Mock Virtual Advisory Board reasoning ---
    def mock_virtual_board(problem: FounderProblem) -> str:
        lines = []
        lines.append(f"Main problem identified: {problem.main_problem_one_line}")
        lines.append("")

        if "Weak or unclear strategy" in problem.why_exists:
            lines.append("🧭 Strategy Agent: The root cause seems to be an unclear strategy. You may not have a sharp definition of who you serve, with what offer, and why you are different.")
        if "Poor execution / follow-through" in problem.why_exists:
            lines.append("⚙️ Execution Agent: You’ve already tried some actions, but follow-through and consistency look weak. The problem may not be the idea, but how rigorously it’s being executed.")
        if "Not talking enough to customers" in problem.why_exists:
            lines.append("🗣️ Customer Agent: You are likely missing deep, structured conversations with customers. Without this, it’s hard to know whether the problem is pricing, product, or positioning.")
        if "Low sales experience" in problem.why_exists:
            lines.append("💼 Sales Agent: Sales capability appears to be a gap. You may need senior guidance on building a repeatable sales motion instead of one-off efforts.")
        if "Cashflow / Runway" in problem.impact_areas:
            lines.append("📊 Finance Agent: Cashflow is under pressure. Any solution must protect runway while you run experiments on product or marketing.")

        if len(lines) <= 2:
            lines.append("🤝 Board Summary: Based on your inputs, you’re facing a mix of strategy, execution, and learning issues. A senior with hands-on experience in your stage and domain can help you avoid expensive mistakes and focus on what truly moves the needle.")

        return "\n".join(lines)

    advisory_text = mock_virtual_board(p)

    # --- Mock matching logic ---
    def mock_match_seniors(problem: FounderProblem, seniors: list):
        matches = []
        for s in seniors:
            match = s.copy()
            if "Revenue / Sales" in problem.impact_areas:
                match["fit_reason"] += " Given that revenue and GTM are central for you, their experience will shortcut a lot of trial-and-error."
            if "Customer satisfaction" in problem.impact_areas:
                match["fit_reason"] += " They have seen similar churn or satisfaction issues and know how to improve experience step by step."
            matches.append(match)
        return matches[:3]

    matched_seniors = mock_match_seniors(p, mock_seniors)

    # ---------- UI ----------

    st.markdown(
        """
        <div class="thankyou-card">
            <div class="thankyou-title">Thank you for sharing your challenge. 🚀</div>
            <div class="thankyou-text">
                You’ve just done what most founders skip – clearly defining the real problem.<br/><br/>
                Below is how our <b>Virtual Senior Advisory Board</b> would read your situation
                and which <b>Senior Interns</b> could be the best fit to help you.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.subheader("🧠 Virtual Senior Advisory Board – Mock Analysis")
    st.write(advisory_text)

    st.subheader("👥 Suggested Senior Interns (Demo)")
    for s in matched_seniors:
        with st.container(border=True):
            st.markdown(f"**{s['name']}** – {s['headline']}")
            st.markdown(f"**Key strengths:** {', '.join(s['strengths'])}")
            st.markdown(f"**Why they’re a fit for you:** {s['fit_reason']}")

    st.write("")
    with st.expander("🔍 Developer View: Structured Problem (for judges)"):
        st.subheader("Startup Problem JSON")
        st.json(asdict(p))

        st.subheader("Text we would send to Gemini (when quota is available)")
        st.code(st.session_state.problem_ai_text.strip(), language="markdown")
        st.caption(
            "For the hackathon demo, the analysis above is mock logic. In production, this will be replaced with Gemini + Qdrant powered reasoning and matching."
        )

    st.write("")
    if st.button("⬅️ Describe another problem"):
        st.session_state.problem = None
        st.session_state.problem_ai_text = ""
        st.rerun()
