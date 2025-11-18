# home.py – Senior Intern Landing Page (FINAL)

import streamlit as st

st.set_page_config(
    page_title="Senior Intern – Where Experience Meets Speed",
    page_icon="🧓🚀",
    layout="wide",
)

# ---------------- STYLES ----------------
st.markdown(
    """
    <style>
    body {
        background-color: #F7F9FB;
    }

    .page-wrap {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    /* Top logo */
    .top-bar {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        margin-bottom: 1.5rem;
    }
    .logo-text {
        font-size: 30px;
        font-weight: 800;
        color: #0B1A33;
        letter-spacing: 0.05em;
    }
    .logo-dot {
        display: inline-block;
        width: 11px;
        height: 11px;
        border-radius: 999px;
        background-color: #D9A441;
        margin-left: 8px;
    }

    /* Hero */
    .hero-card {
        background: linear-gradient(135deg, #FFFFFF, #F7F9FB);
        border-radius: 24px;
        padding: 2.5rem 3rem;
        border: 1px solid #E1E5F0;
        box-shadow: 0 18px 42px rgba(15, 23, 42, 0.12);
    }
    .hero-title {
        font-size: 40px;
        line-height: 1.1;
        font-weight: 800;
        color: #111827;
        margin-bottom: 0.8rem;
    }
    .hero-subtitle {
        font-size: 16px;
        color: #4B5563;
        max-width: 640px;
        margin-bottom: 1.3rem;
    }
    .hero-bridge {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: linear-gradient(90deg, #111827, #D9A441);
        border-radius: 999px;
        padding: 0.55rem 1.6rem;
        color: #F9FAFB;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.10em;
        text-transform: uppercase;
    }
    .hero-bridge span {
        opacity: 0.92;
    }
    .hero-bridge-center {
        font-size: 11px;
    }
    .chip-row {
        margin-top: 1.1rem;
    }
    .stat-chip {
        padding: 0.45rem 0.95rem;
        border-radius: 999px;
        background: rgba(217,164,65,0.10);
        border: 1px solid #D9A441;
        font-size: 13px;
        color: #5d4308;
        margin-right: 0.55rem;
        margin-bottom: 0.4rem;
        display: inline-block;
        white-space: nowrap;
    }

    /* Carousel banner */
    .carousel-card {
        background: #FFFFFF;
        border-radius: 20px;
        border: 1px solid #E1E5F0;
        box-shadow: 0 14px 36px rgba(15, 23, 42, 0.10);
        padding: 1.5rem 1.7rem;
    }
    .carousel-heading {
        font-size: 15px;
        font-weight: 600;
        color: #0B1A33;
        margin-bottom: 0.6rem;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .carousel-line {
        font-size: 14px;
        color: #374151;
        margin-bottom: 0.25rem;
    }

    /* CTAs */
    .cta-card {
        border-radius: 22px;
        padding: 1.8rem 2rem;
        background: #FFFFFF;
        border: 1px solid #E1E5F0;
        box-shadow: 0 10px 28px rgba(15, 23, 42, 0.08);
        height: 100%;
    }
    .cta-card.senior {
        background: radial-gradient(circle at top left, rgba(217,164,65,0.18), #FFFFFF);
    }
    .cta-card.founder {
        background: radial-gradient(circle at top right, rgba(15,23,42,0.12), #FFFFFF);
    }
    .cta-title {
        font-size: 20px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 0.4rem;
    }
    .cta-text {
        font-size: 14px;
        color: #4B5563;
        margin-bottom: 1.1rem;
        max-width: 440px;
    }

    .stButton>button {
        border-radius: 999px;
        padding: 0.6rem 1.8rem;
        border: none;
        background: #111827;
        color: #F9FAFB;
        font-weight: 600;
        font-size: 14px;
    }
    .stButton>button:hover {
        background: #D9A441;
        color: #111827;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- PAGE LAYOUT ----------------
st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

# TOP LOGO
st.markdown(
    """
    <div class="top-bar">
        <div class="logo-text">
            Senior Intern <span class="logo-dot"></span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# HERO SECTION
hero_left, hero_right = st.columns([1.6, 1.1])

with hero_left:
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-title">Where Experience Meets<br/>Speed.</div>
            <div class="hero-subtitle">
                Life expectancy is rising, but careers still end too early.
                Senior Intern connects experienced professionals who still want to contribute
                with founders who can’t afford full-time executives – through an AI-powered
                Virtual Senior Advisory Board.
            </div>
            <div class="hero-bridge">
                <span>STARTUPS</span>
                <span class="hero-bridge-center">AI-POWERED BRIDGE</span>
                <span>SENIOR PROFESSIONALS</span>
            </div>
            <div class="chip-row">
                <span class="stat-chip">150M+ people 55+ by 2030</span>
                <span class="stat-chip">40% of Japan’s workforce already 55+</span>
                <span class="stat-chip">A new category: Senior Interns</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with hero_right:
    st.markdown('<div class="carousel-card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="carousel-heading">💭 <span>Brain-tickling questions</span></div>',
        unsafe_allow_html=True,
    )

    tabs = st.tabs(["For Senior Professionals", "For Startup Founders"])

    senior_lines = [
        "Your career may have retired. Has your talent?",
        "What if your 30 years of judgment could shape a startup in 30 minutes?",
        "Looking for purpose, some income, and to feel truly needed again?",
    ]
    founder_lines = [
        "What if your toughest challenge was read like a board-meeting agenda?",
        "Why spend 3 months hiring when you can borrow judgment in 3 seconds?",
        "Are you moving fast – or fast in the wrong direction?",
    ]

    with tabs[0]:
        for line in senior_lines:
            st.markdown(f'<div class="carousel-line">• {line}</div>', unsafe_allow_html=True)

    with tabs[1]:
        for line in founder_lines:
            st.markdown(f'<div class="carousel-line">• {line}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- CTA SECTION ----------------
cta_col1, cta_col2 = st.columns(2)

with cta_col1:
    st.markdown('<div class="cta-card senior">', unsafe_allow_html=True)
    st.markdown(
        '<div class="cta-title">🧓 I am a Senior Professional</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="cta-text">'
        'Create your Senior Intern profile so our AI can understand your strengths, interests, and availability – '
        'and make you discoverable to the right startups.'
        '</div>',
        unsafe_allow_html=True,
    )
    if st.button("Create my Senior Intern profile"):
        st.info(
            "For this prototype, open the Senior app with:\n\n"
            "`streamlit run app.py`"
        )
    st.markdown('</div>', unsafe_allow_html=True)

with cta_col2:
    st.markdown('<div class="cta-card founder">', unsafe_allow_html=True)
    st.markdown(
        '<div class="cta-title">🚀 I am a Startup Founder</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="cta-text">'
        'Describe your biggest challenge and see how our Virtual Senior Advisory Board would analyse it – '
        'and which Senior Interns might be your best partners.'
        '</div>',
        unsafe_allow_html=True,
    )
    if st.button("Describe my startup challenge"):
        st.info(
            "For this prototype, open the Founder app with:\n\n"
            "`streamlit run founder_app.py`"
        )
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.caption(
    "Prototype note: In the full product these CTAs route directly into the Senior and Startup experiences. "
    "For the hackathon demo, the Senior and Founder flows run as two Streamlit apps (app.py and founder_app.py)."
)

st.markdown('</div>', unsafe_allow_html=True)
