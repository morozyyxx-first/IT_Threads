import streamlit as st

home_page = st.Page("home_page.py")
create_post_page = st.Page("create_post_page.py")

nav = st.navigation(
    [
        home_page,
        create_post_page
    ],
    # Hiding a default sidebar
    position = "hidden"
)

nav.run()