# main.py
import streamlit as st
from src.config import get_supabase
from src.auth.auth_state import AuthState
from src.components.sidebar import render_sidebar
from src.components.widgets import render_login_form, render_signup_form
from src.pages.dashboard import render_dashboard
from src.pages.profile import render_profile

def main():
    # Page config
    st.set_page_config(
        page_title="Auth Test App",
        page_icon="🔒",
        layout="wide"
    )
    
    # Initialize Supabase and auth
    supabase = get_supabase()
    auth_state = AuthState(supabase)
    
    # Render sidebar
    render_sidebar(auth_state)
    
    if not auth_state.is_authenticated:
        st.title("Welcome to Test App")
        
        # Create tabs for login and signup
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        
        with tab1:
            render_login_form(auth_state)
        
        with tab2:
            render_signup_form(auth_state)
    
    else:
        # Navigation for authenticated users
        page = st.sidebar.radio("Navigation", ["Dashboard", "Profile"])
        
        if page == "Dashboard":
            render_dashboard(auth_state)
        else:
            render_profile(auth_state)

if __name__ == "__main__":
    main()