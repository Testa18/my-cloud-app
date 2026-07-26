import streamlit as st

# Force responsive full-screen viewport layout
st.set_page_config(
    page_title="App Tech Skills", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Custom responsive CSS injection
st.markdown("""
    <style>
    /* Sky Blue Background for the entire application */
    .stApp {
        background-color: #87CEEB !important;
    }
    
    /* Center the Navy Blue Title and make size responsive */
    .app-title {
        color: #000080;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    
    /* Centered Metallic Wrench Logo Container */
    .logo-container {
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Metallic Wrench SVG styling */
    .metallic-wrench {
        width: 80px;
        height: 80px;
        filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.3));
    }
    
    /* Responsive Navigation Button container */
    .nav-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        width: 100%;
        max-width: 400px;
        margin: 0 auto;
    }
    
    /* White Buttons with Black Text styling for all devices */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        border-radius: 8px !important;
        width: 100% !important;
        padding: 12px 20px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        transition: all 0.3s ease;
    }
    
    /* Button Hover effect */
    div.stButton > button:hover {
        background-color: #F0F0F0 !important;
        transform: scale(1.02);
    }
    
    /* Secondary Content Styling */
    .content-box {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 12px;
        margin-top: 25px;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        color: #333333;
    }
    
    /* Floating Home Button for small screens / long scrolls */
    .home-link-container {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .home-link {
        color: #000080 !important;
        font-weight: bold;
        text-decoration: none;
        font-size: 16px;
    }
    </style>
    
    <!-- Anchor tag at the very top of the page for Home navigation -->
    <div id="top"></div>
""", unsafe_allow_html=True)

# 1. METALLIC WRENCH LOGO (Rendered via clean vector SVG to look crisp on mobile Retina displays)
st.markdown("""
    <div class="logo-container">
        <svg class="metallic-wrench" viewBox="0 0 24 24" xmlns="http://w3.org">
            <defs>
                <linearGradient id="metal" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#ffffff;stop-opacity:1" />
                    <stop offset="30%" style="stop-color:#e0e0e0;stop-opacity:1" />
                    <stop offset="50%" style="stop-color:#8c8c8c;stop-opacity:1" />
                    <stop offset="70%" style="stop-color:#bebebe;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#595959;stop-opacity:1" />
                </linearGradient>
            </defs>
            <path fill="url(#metal)" d="M13.57 2.3a8.38 8.38 0 0 0-4.7 1.83l2.84 2.84a1.36 1.36 0 0 1 0 1.93l-1.42 1.41a1.36 1.36 0 0 1-1.93 0L5.5 7.48a8.38 8.38 0 0 0-1.83 4.7 8.44 8.44 0 0 0 2.22 5.67l-3.32 3.32a1 1 0 0 0 0 1.41l1.42 1.42a1 1 0 0 0 1.41 0l3.32-3.32A8.44 8.44 0 0 0 14.4 17a8.38 8.38 0 0 0 4.7-1.83l-2.84-2.84a1.36 1.36 0 0 1 0-1.93l1.42-1.41a1.36 1.36 0 0 1 1.93 0l2.84 2.84a8.38 8.38 0 0 0 1.83-4.7 8.41 8.41 0 0 0-8.51-7.88z"/>
        </svg>
    </div>
""", unsafe_allow_html=True)

# 2. TITLE (Navy Blue, 32px)
st.markdown('<div class="app-title">App Tech Skills</div>', unsafe_allow_html=True)

# Initialize track state for menu selection
if "view" not in st.session_state:
    st.session_state.view = "Welcome"

# 3. RESPONSIVE VERTICAL BUTTONS CONTAINER
# Using standard elements inside a centered CSS flexible box wrapper
st.markdown('<div class="nav-container">', unsafe_allow_html=True)

if st.button("Info", key="btn_info"):
    st.session_state.view = "Info"

if st.button("Mechanic Services", key="btn_mechanic"):
    st.session_state.view = "Mechanic Services"

if st.button("Work Performed", key="btn_work"):
    st.session_state.view = "Work Performed"

if st.button("Parts Utilized", key="btn_parts"):
    st.session_state.view = "Parts Utilized"

st.markdown('</div>', unsafe_allow_html=True)

# 4. ACTIVE DISPLAY WORKSPACE
# Content updates inside a card without requiring extra screen reloads
if st.session_state.view != "Welcome":
    st.markdown(f"""
        <div class="content-box">
            <h3>📂 {st.session_state.view} Workspace</h3>
            <p>You have accessed the <strong>{st.session_state.view}</strong> dashboard pane.</p>
            <p>This layout adapts automatically to fit computer monitors, iPads, and phone displays full screen.</p>
        </div>
    """, unsafe_allow_html=True)

# 5. GO HOME / TOP LINK
# Allows mobile users to jump seamlessly back up to the header context
st.markdown("""
    <div class="home-link-container">
        <a href="#top" class="home-link">🔼 Return to Top (Home)</a>
    </div>
""", unsafe_allow_html=True)
