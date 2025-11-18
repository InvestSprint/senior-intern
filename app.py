# app.py — Senior Intern • Senior Profile MVP (v2)

import streamlit as st
from dataclasses import dataclass, asdict
from datetime import datetime
import uuid

# ---------- Page config ----------

st.set_page_config(
    page_title="Senior Intern – Senior Profile",
    page_icon="🧓",
    layout="centered"
)

# ---------- Simple styling ----------

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
        background: linear-gradient(120deg, #e3f2fd, #e8f5e9);
        padding: 2rem 2.5rem;
        border-radius: 18px;
        border: 1px solid #c5e1a5;
        text-align: center;
    }
    .thankyou-title {
        font-size: 26px;
        font-weight: 700;
        color: #1b5e20;
        margin-bottom: 0.7rem;
    }
    .thankyou-text {
        font-size: 16px;
        color: #1b3335;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Data model ----------

@dataclass
class SeniorProfile:
    id: str
    name: str
    email: str
    linkedin_url: str
    headline: str
    skills: list
    intro: str
    preferred_domains: list
    preferred_startup_stage: str
    preferred_problem_types: list
    availability_days_per_week: int
    availability_hours_per_day: int
    created_at: str


# ---------- Helpers ----------

def build_ai_text(profile: SeniorProfile) -> str:
    """Text we will send to Gemini later."""
    return f"""
Senior profile:
Name: {profile.name}
Headline: {profile.headline}

Skills: {", ".join(profile.skills)}
Preferred domains: {", ".join(profile.preferred_domains)}
Preferred startup stage: {profile.preferred_startup_stage}
Enjoys solving: {", ".join(profile.preferred_problem_types)}

Availability: {profile.availability_days_per_week} days/week,
{profile.availability_hours_per_day} hours/day.

Intro:
{profile.intro}

LinkedIn: {profile.linkedin_url}
"""


# ---------- Session state ----------

if "profile" not in st.session_state:
    st.session_state.profile = None
if "ai_text" not in st.session_state:
    st.session_state.ai_text = ""


# ---------- UI flow ----------

if st.session_state.profile is None:
    # ------- Show form -------

    st.markdown('<div class="main-title">Senior Intern – Create Your Senior Profile</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-title">Share a few details so founders and our AI can understand your experience and match you with the right startup problems.</div>',
        unsafe_allow_html=True,
    )

    with st.form("senior_profile_form"):
        name = st.text_input("Full Name *")
        email = st.text_input("Email *")
        linkedin_url = st.text_input("LinkedIn Profile URL *")

        headline = st.text_input(
            "One-line headline about you *",
            placeholder="Ex: Ex-COO, 25+ yrs in Telecom & Operations",
        )

        skills_text = st.text_area(
            "Key Skills (comma-separated) *",
            placeholder="Strategy, Operations, Product, Go-To-Market, Fundraising",
            height=80,
        )

        intro = st.text_area(
            "Short Introduction (2–4 lines) *",
            placeholder="Share the kind of value you bring, your style of working, and what excites you about working with startups.",
            height=100,
        )

        preferred_domains = st.multiselect(
            "What kind of industries / domains do you want to work with? *",
            options=[
                "SaaS",
                "Fintech",
                "Edtech",
                "Healthtech",
                "E-commerce",
                "Telecom",
                "Manufacturing",
                "Retail",
                "Hospitality",
                "Other",
            ],
        )

        preferred_startup_stage = st.selectbox(
            "Preferred startup stage *",
            ["Idea stage", "MVP built", "Early revenue", "Scaling", "Any"],
        )

        preferred_problem_types = st.multiselect(
            "What kind of problems do you enjoy solving most? *",
            options=[
                "Strategy & Direction",
                "Operations & Execution",
                "Product & UX",
                "Sales & GTM",
                "Finance & Unit Economics",
                "People & Culture",
                "Turnaround / Crisis",
                "Other",
            ],
        )

        availability_days_per_week = st.slider(
            "How many days per week are you willing to contribute? *",
            min_value=1,
            max_value=7,
            value=2,
        )

        availability_hours_per_day = st.slider(
            "How many hours per day (on the days you work)? *",
            min_value=1,
            max_value=8,
            value=3,
        )

        submitted = st.form_submit_button("Create Profile")

    if submitted:
        if not (
            name
            and email
            and linkedin_url
            and skills_text
            and intro
            and preferred_domains
            and preferred_problem_types
        ):
            st.error("Please fill all required fields marked with *.")
        else:
            skills = [s.strip() for s in skills_text.split(",") if s.strip()]

            profile = SeniorProfile(
                id=str(uuid.uuid4()),
                name=name,
                email=email,
                linkedin_url=linkedin_url,
                headline=headline,
                skills=skills,
                intro=intro,
                preferred_domains=preferred_domains,
                preferred_startup_stage=preferred_startup_stage,
                preferred_problem_types=preferred_problem_types,
                availability_days_per_week=availability_days_per_week,
                availability_hours_per_day=availability_hours_per_day,
                created_at=datetime.utcnow().isoformat(),
            )

            st.session_state.profile = profile
            st.session_state.ai_text = build_ai_text(profile)
            st.rerun()

else:
    # ------- Thank-you screen -------

    profile: SeniorProfile = st.session_state.profile

    st.markdown(
        """
        <div class="thankyou-card">
            <div class="thankyou-title">Thank you for submitting your profile! 🌱</div>
            <div class="thankyou-text">
                You’re now part of our Senior Intern community.<br/>
                Very soon, founders will be matched with your experience and judgment.<br/><br/>
                In the next step of our build, this page will also let you explore startup problems that fit your interests.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")  # small spacer

    with st.expander("🔍 Developer View: Traceable Senior Profile (for judges)"):
        st.subheader("Senior Profile JSON")
        st.json(asdict(profile))

        st.subheader("Text we will send to Gemini")
        st.code(st.session_state.ai_text.strip(), language="markdown")
        st.caption(
            "This internal view shows how the profile will be processed by Gemini and turned into an embedding for storage in Qdrant."
        )

    st.write("")
    if st.button("⬅️ Create another profile"):
        st.session_state.profile = None
        st.session_state.ai_text = ""
        st.rerun()
