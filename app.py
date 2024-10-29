import streamlit as st

# In-memory storage for tasks
tasks = {
    "To Do": [],
    "In Progress": [],
    "Done": []
}

def add_task(title, status):
    if title and status in tasks:
        tasks[status].append(title)

def move_task(title, from_status, to_status):
    if title in tasks[from_status]:
        tasks[from_status].remove(title)
        tasks[to_status].append(title)

# Streamlit app layout
st.title("Simple Kanban Board")

# Task input form
with st.form(key='task_form'):
    task_title = st.text_input("Task Title")
    task_status = st.selectbox("Status", ["To Do", "In Progress", "Done"])
    submit_button = st.form_submit_button("Add Task")

    if submit_button:
        add_task(task_title, task_status)
        st.success(f"Task '{task_title}' added to '{task_status}'")

# Display Kanban board
for status in tasks:
    st.subheader(status)
    for task in tasks[status]:
        cols = st.columns([5, 1])
        cols[0].markdown(f"- {task}")
        
        # Move task dropdown
        with cols[1].form(key=f"move_task_{task}"):
            to_status = st.selectbox("Move to", ["To Do", "In Progress", "Done"], key=f"to_{task}")
            move_button = st.form_submit_button("Move")
            if move_button:
                move_task(task, status, to_status)
                st.success(f"Moved '{task}' to '{to_status}'")

