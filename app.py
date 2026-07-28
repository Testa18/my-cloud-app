import streamlit as st
import pandas as pd
from datetime import datetime

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
        background-color: #87CEEC !important;
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
        gap: 12px;
        width: 100%;
        max-width: 400px;
        margin: 0 auto 25px auto;
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
    
    /* Workspace Card Container */
    .workspace-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        max-width: 800px;
        margin: 0 auto;
        color: #333333;
    }
    
    .workspace-title {
        color: #000080;
        margin-bottom: 20px;
        border-bottom: 2px solid #87CEEB;
        padding-bottom: 10px;
    }

    /* Floating Home Button */
    .home-link-container {
        text-align: center;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    .home-link {
        color: #000080 !important;
        font-weight: bold;
        text-decoration: none;
        font-size: 16px;
    }
    </style>
    <div id="top"></div>
""", unsafe_allow_html=True)

# Initialize Session State Data Tables (Persists data during app usage)
if "view" not in st.session_state:
    st.session_state.view = "Welcome"

if "mechanic_tickets" not in st.session_state:
    # Starter tickets counter
    st.session_state.mechanic_tickets = 4

if "work_records" not in st.session_state:
    # Starter database for work logs
    st.session_state.work_records = pd.DataFrame([
        {"Date": "2026-07-24", "Tech": "Alex M.", "Job Details": "Brake pad replacement and rotor resurfacing."},
        {"Date": "2026-07-25", "Tech": "Sam K.", "Job Details": "System diagnostic check and battery replacement."}
    ])

if "parts_inventory" not in st.session_state:
    # Mock parts database to show off searching/filtering
    st.session_state.parts_inventory = pd.DataFrame([
        {"Part ID": "P101", "Name": "Heavy Duty Brake Pads", "Category": "Brakes", "Stock": 14, "Location": "Shelf A1"},
        {"Part ID": "P102", "Name": "Premium Oil Filter", "Category": "Filters", "Stock": 32, "Location": "Shelf B3"},
        {"Part ID": "P103", "Name": "12V Automotive Battery", "Category": "Electrical", "Stock": 8, "Location": "Floor Bay 2"},
        {"Part ID": "P104", "Name": "Serpentine Belt", "Category": "Belts", "Stock": 19, "Location": "Shelf A4"},
        {"Part ID": "P105", "Name": "Spark Plug Set (X4)", "Category": "Engine", "Stock": 25, "Location": "Shelf C2"},
        {"Part ID": "P106", "Name": "Air Filter Assembly", "Category": "Filters", "Stock": 11, "Location": "Shelf B4"}
    ])

# 1. METALLIC WRENCH LOGO (Vector SVG)
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

# 2. TITLE
st.markdown('<div class="app-title">App Tech Skills</div>', unsafe_allow_html=True)

# 3. VERTICAL NAVIGATION BUTTONS (Stretches on mobile, stays compact on computer display)
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

# 4. ACTIVE DYNAMIC DASHBOARD WORKSPACES
if st.session_state.view == "Welcome":
    st.markdown("""
        <div class="workspace-card" style="text-align: center;">
            <h3 class="workspace-title">Welcome to App Tech Skills</h3>
            <p>Select an option from the menu list above to manage shop logs, track parts, or view analytics indicators.</p>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.view == "Info":
    st.markdown("""
        <div class="workspace-card">
            <h3 class="workspace-title">ℹ️ System Information</h3>
            <p><strong>App Platform:</strong> Cloud Web-App Environment</p>
            <p><strong>Target Devices:</strong> Optimized dynamically for Desktop Fullscreen, iPad Pro, iPad Mini, iPhone, and Android platforms.</p>
            <p><strong>Engine State:</strong> Active memory tracking protocol running.</p>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.view == "Mechanic Services":
    # Wrapper card container
    st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
    st.markdown('<h3 class="workspace-title">🛠️ Mechanic Services Dashboard</h3>', unsafe_allow_html=True)
    
    # 📈 Metric Counter Layout
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("Manage active service bays and track continuous daily work volume items below.")
    with col2:
        st.metric(label="Daily Active Tickets", value=st.session_state.mechanic_tickets)
    
    st.markdown("---")
    st.write("⚙️ **Counter Administration Controls**")
    
    # Interactive inline control buttons to change status metrics instantly
    ctrl_col1, ctrl_col2, ctrl_col3 = st.columns(3)
    with ctrl_col1:
        if st.button("➕ Open New Ticket", key="add_tix"):
            st.session_state.mechanic_tickets += 1
            st.rerun()
    with ctrl_col2:
        if st.button("➖ Complete Ticket", key="sub_tix"):
            if st.session_state.mechanic_tickets > 0:
                st.session_state.mechanic_tickets -= 1
                st.rerun()
    with ctrl_col3:
        if st.button("🔄 Reset Daily Count", key="reset_tix"):
            st.session_state.mechanic_tickets = 0
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.view == "Work Performed":
    st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
    st.markdown('<h3 class="workspace-title">📝 Work Performed Log</h3>', unsafe_allow_html=True)
    
    st.write("Submit formal service logging details. Entries are saved instantly to session memory storage below.")
    
    # Formal Text Form Entry Fields
    with st.form(key="work_entry_form", clear_on_submit=True):
        tech_name = st.text_input("Lead Mechanic / Technician Name", placeholder="e.g., J. Smith")
        job_description = st.text_area("Detailed Summary of Work Performed", placeholder="e.g., Flushed transmission fluid, fixed wiring harness...")
        submit_log = st.form_submit_button("Submit Formal Log Entry")
        
    if submit_log:
        if tech_name and job_description:
            current_date = datetime.now().strftime("%Y-%m-%d")
            new_entry = pd.DataFrame([{"Date": current_date, "Tech": tech_name, "Job Details": job_description}])
            st.session_state.work_records = pd.concat([st.session_state.work_records, new_entry], ignore_index=True)
            st.success("Success: Data saved to session record!")
        else:
            st.error("Error: Please fill out all text input parameters before submitting.")
            
    # Display the current logged table records
    st.markdown("#### 📋 Current Shift Logs")
    st.dataframe(st.session_state.work_records, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

