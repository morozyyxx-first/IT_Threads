from datetime import datetime

import httpx
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# CREATING NEW POST PAGE

st.set_page_config(
    page_title = "IT Threads | Create post",
    page_icon = "💬",
    layout = "centered",
)

def add_post(
        post_owner: str,
        description: str,
        created_at
) -> None:
    with httpx.Client() as client:
        response = client.post(
            url = os.getenv("ADD_NEW_POST_ROUTE"),
            json = {
                "post_owner": post_owner,
                "description": description,
                "created_at": created_at
            }
        )
        if response.status_code == 200:
            st.success("Successfully created post")
            st.switch_page("home_page.py")
        else:
            st.error("Server Error")
            st.stop()

# Title of the page
st.title("IT Threads | Creating new post", text_alignment = "center")
st.divider()

with st.container(border = True):
    username = st.text_input("Username", placeholder = "Write your username here...", max_chars = 20)
    post_description = st.text_area("Description", placeholder = "Write here...")
with st.container(horizontal_alignment = "center"):
    load_data = {}
    if st.button("Create post", icon = "💌"):
        if username != "":
            if post_description != "":
                try:
                    add_post(
                        username,
                        post_description,
                        datetime.now().isoformat()
                    )
                except ValueError as e:
                    st.error("Value Error, try again.")
            else:
                st.warning("Please enter a description")
        else:
            st.warning("Enter username please.")