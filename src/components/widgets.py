# src/components/widgets.py
import streamlit as st
from ..auth.auth_state import AuthState

def render_login_form(auth_state: AuthState) -> None:
    """Render the login form."""
    with st.form("login_form"):
        st.subheader("Login")
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        submit = st.form_submit_button("Login")
        
        if submit:
            if auth_state.login(email, password):
                st.rerun()

def render_signup_form(auth_state: AuthState) -> None:
    """Render the signup form."""
    with st.form("signup_form"):
        st.subheader("Create Account")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")
        password_confirm = st.text_input(
            "Confirm Password", 
            type="password", 
            key="signup_password_confirm"
        )
        submit = st.form_submit_button("Sign Up")
        
        if submit:
            if password != password_confirm:
                st.error("Passwords do not match!")
            else:
                auth_state.sign_up(email, password)