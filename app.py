import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Cloud Task Tracker", layout="wide")

# Initialize data structure in browser memory if it doesn't exist
if "tasks" not in st.session_state:
    st.session_state.tasks = pd.DataFrame(columns=["Task", "Category", "Priority"])

st.title("🚀 Cloud Task Analytics Tracker")
st.subheader("Running completely online via cloud compute resources.")

# Interactive layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📝 Create Task")
    with st.form(key="cloud_task_form", clear_on_submit=True):
        task_name = st.text_input("Task Description")
        category = st.selectbox("Category", ["Engineering", "Marketing", "Finance", "Ops"])
        priority = st.select_slider("Priority", options=["Low", "Medium", "High"])
        submit_button = st.form_submit_button(label="Save to Cloud")

    if submit_button and task_name:
        new_row = pd.DataFrame([{"Task": task_name, "Category": category, "Priority": priority}])
        st.session_state.tasks = pd.concat([st.session_state.tasks, new_row], ignore_index=True)
        st.success("Task uploaded to session memory!")

with col2:
    st.markdown("### 📊 Active Workspaces")
    if not st.session_state.tasks.empty:
        # Display and edit data
        edited_df = st.data_editor(st.session_state.tasks, num_rows="dynamic", use_container_width=True)
        st.session_state.tasks = edited_df
        
        # Display Metrics
        st.markdown("---")
        st.metric(label="Total Tasks Stored", value=len(st.session_state.tasks))
    else:
        st.info("No cloud data stored yet. Submit a task using the form.")
Use code with caution.
