import streamlit as st

# -------------------------------------------------------
# PREMIUM THEME SETTINGS (Dark Navy + Gold)
# -------------------------------------------------------
st.set_page_config(page_title="Senior Intern", layout="wide")

PRIMARY_BG = "#0A1A2F"       # Dark navy
GOLD = "#D9A441"             # Gold
TEXT_LIGHT = "#F7F9FB"       # Off-white
CARD_BG = "#102238"          # Slightly lighter navy

# -------------------------------------------------------
# INITIALIZE SESSION STATE ROUTING
# -------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

def goto(page):
    st.session_state.page = page


# -------------------------------------------------------
# DUMMY SENIOR DATABASE
# -------------------------------------------------------
SENIORS = [
    {
        "name": "Arjun Mehta",
        "title": "Chief Technology Officer",
        "experience": "20+ years",
        "skills": "AI, Cloud, Distributed Systems",
        "match_reason": "Your problem requires deep tech leadership to redesign your funnel and tech stack."
    },
    {
        "name": "Sarah Ali",
        "title": "Digital Marketing Lead",
        "experience": "15+ years",
        "skills": "SEO, Paid Ads, Funnel Optimization",
        "match_reason": "You mentioned leads but low conversions—this is a classic funnel optimization issue."
    },
    {
        "name": "James Thompson",
        "title": "Sales Coach",
        "experience": "18+ years",
        "skills": "B2B Sales, Pitch Strategy, Conversion Psychology",
        "match_reason": "When leads aren’t converting, founders usually need stronger sales scripts and process."
    },
]


# -------------------------------------------------------
# PREMIUM HERO CAROUSEL (FAUX ROTATION)
# -------------------------------------------------------
def hero_carousel():
    st.markdown(f"""
    <div style='background-color:{PRIMARY_BG}; padding:50px; border-radius:12px;'>
        <h1 style='color:{GOLD}; text-align:center; font-size:60px; font-weight:700;'>
            Senior Intern
        </h1>
        <h3 style='color:{TEXT_LIGHT}; text-align:center; max-width:900px; margin:auto; font-size:24px;'>
            The world's first platform connecting startups with part-time senior professionals +
            an AI-powered Virtual Advisory Board.
        </h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("")  

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "✨ Senior Q1", "✨ Senior Q2", "✨ Senior Q3",
        "🚀 Founder Q1", "🚀 Founder Q2", "🚀 Founder Q3"
    ])

    with tab1:
        st.markdown(f"<h3 style='color:{TEXT_LIGHT};'>Your career ended, but your capability didn’t. Ready to feel valued again?</h3>", unsafe_allow_html=True)
    with tab2:
        st.markdown(f"<h3 style='color:{TEXT_LIGHT};'>What if your 25 years of wisdom could change a startup’s direction?</h3>", unsafe_allow_html=True)
    with tab3:
        st.markdown(f"<h3 style='color:{TEXT_LIGHT};'>Would you contribute 5 hours/week for purpose and income?</h3>", unsafe_allow_html=True)
    with tab4:
        st.markdown(f"<h3 style='color:{TEXT_LIGHT};'>What’s slowing your startup — skill or experience?</h3>", unsafe_allow_html=True)
    with tab5:
        st.markdown(f"<h3 style='color:{TEXT_LIGHT};'>If you could borrow a CMO for 5 hours… would you?</h3>", unsafe_allow_html=True)
    with tab6:
        st.markdown(f"<h3 style='color:{TEXT_LIGHT};'>What if your biggest problem is solvable in minutes?</h3>", unsafe_allow_html=True)


# -------------------------------------------------------
# HOMEPAGE
# -------------------------------------------------------
def home():
    hero_carousel()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style='background-color:{CARD_BG}; padding:40px; border-radius:12px; text-align:center;'>
            <h2 style='color:{GOLD};'>I am a Senior Professional</h2>
            <p style='color:{TEXT_LIGHT}; font-size:18px;'>Ready to contribute your experience part-time?</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Create Senior Profile", on_click=lambda: goto("senior"), use_container_width=True)

    with col2:
        st.markdown(f"""
        <div style='background-color:{CARD_BG}; padding:40px; border-radius:12px; text-align:center;'>
            <h2 style='color:{GOLD};'>I am a Startup Founder</h2>
            <p style='color:{TEXT_LIGHT}; font-size:18px;'>Need diagnosis + senior expert recommendations?</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Submit Startup Challenge", on_click=lambda: goto("founder"), use_container_width=True)


# -------------------------------------------------------
# SENIOR PROFILE FORM
# -------------------------------------------------------
def senior_profile():
    st.markdown(f"<h1 style='color:{GOLD};'>Senior Profile</h1>", unsafe_allow_html=True)

    name = st.text_input("Full Name")
    linkedin = st.text_input("LinkedIn URL")
    skills = st.text_area("Key Skills (comma separated)")
    intro = st.text_area("Short Intro")
    availability = st.selectbox("Availability per week", ["5 hours", "10 hours", "15 hours", "20+ hours"])

    if st.button("Submit Profile"):
        st.success("Your profile has been created and is now discoverable by startups.")
        st.balloons()
        if st.button("Back to Home"):
            goto("home")


# -------------------------------------------------------
# STARTUP CHALLENGE FORM
# -------------------------------------------------------
def founder_flow():
    st.markdown(f"<h1 style='color:{GOLD};'>Startup Challenge</h1>", unsafe_allow_html=True)

    name = st.text_input("Startup Name")
    problem = st.text_area("Describe your biggest current challenge")

    clarify = ""
    if problem:
        clarify = st.radio("What does this relate to most?", [
            "Marketing funnel",
            "Sales conversion",
            "Product failure",
            "Team experience gap",
            "Strategy / Clarity"
        ])

    if st.button("Analyze Problem"):
        st.session_state.problem = problem
        goto("match")


# -------------------------------------------------------
# MATCHING SCREEN (MAGIC MOMENT)
# -------------------------------------------------------
def match_screen():
    st.markdown(f"<h1 style='color:{GOLD};'>AI Advisory Board Recommendation</h1>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style='background-color:{CARD_BG}; padding:25px; border-radius:12px; margin-bottom:25px;'>
        <h2 style='color:{GOLD};'>Diagnosis</h2>
        <p style='color:{TEXT_LIGHT}; font-size:18px;'>
            Based on your inputs, your challenge seems related to conversion & experience gaps.
            Below are the best Senior Interns matched for you.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<h2 style='color:{GOLD};'>Top Matches</h2>", unsafe_allow_html=True)

    for s in SENIORS:
        st.markdown(f"""
        <div style='background-color:{CARD_BG}; padding:25px; border-radius:12px; margin-bottom:15px;'>
            <h3 style='color:{GOLD};'>{s['name']} — {s['title']}</h3>
            <p style='color:{TEXT_LIGHT};'><b>Experience:</b> {s['experience']}</p>
            <p style='color:{TEXT_LIGHT};'><b>Skills:</b> {s['skills']}</p>
            <p style='color:{TEXT_LIGHT};'><b>Why matched:</b> {s['match_reason']}</p>
        </div>
        """, unsafe_allow_html=True)

    if st.button("Back to Home"):
        goto("home")


# -------------------------------------------------------
# MAIN ROUTER
# -------------------------------------------------------
if st.session_state.page == "home":
    home()
elif st.session_state.page == "senior":
    senior_profile()
elif st.session_state.page == "founder":
    founder_flow()
elif st.session_state.page == "match":
    match_screen()
