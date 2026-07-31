import streamlit as st
from auth import login

def login_page():

    st.title("AI Insider Threat Detection")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        success,user = login(
            username,
            password
        )

        if success:

            st.session_state.logged_in = True
            st.session_state.user = user

            st.rerun()

        else:

            st.error("Invalid Username or Password")