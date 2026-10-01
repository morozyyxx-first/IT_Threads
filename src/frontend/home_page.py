import httpx
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# MAIN HOME PAGE WITH POSTS

st.set_page_config(
    page_title = "IT Threads",
    page_icon = "💻",
    layout = "wide",
)

# Method to fetch all posts from database
def fetch_posts():
    with httpx.Client() as client:
        response = client.get(
            url = os.getenv("GET_POSTS_ROUTE"),
        )
        if response.status_code == 200:
            return response.json()
        else:
            return "Nothing here, create a new post!"

# Including the font for project and setting up the
# bg color of website
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap');
        * {
            font-family: "JetBrains Mono", monospace; 
        }
    </style>
""", unsafe_allow_html = True)

# Central main title
st.title("IT Threads", text_alignment = "center")
st.divider()

# Define a container with all current posts in DESC order
posts_container = st.container(
    border = True,
    horizontal_alignment = "center",
    height = 400,
    autoscroll = False,
)
posts = fetch_posts()

# Listing posts from database
with posts_container:
    if len(posts) == 0:
        st.subheader("Nothing here, create a new post!", text_alignment = "center")
    else:
        st.subheader("Posts", text_alignment = "center")
        for post in posts:
            with st.container(width = 500, border = True):
                st.markdown(f"**{post.get("post_owner")}**")
                st.markdown(f"*{post.get("description")}*")

# Button to add a new post
with st.container(horizontal_alignment = "center"):
    if st.button("Create Post", icon = "💬"):
        st.switch_page("create_post_page.py")