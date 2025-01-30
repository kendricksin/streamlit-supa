# src/components/sidebar.py
import streamlit as st
from ..auth.auth_state import AuthState

def render_sidebar(auth_state: AuthState) -> None:
    with st.sidebar:
        st.title("🚀 Test App")
        
        if auth_state.is_authenticated:
            user = auth_state.get_user()
            st.write(f"👤 {user['email']}")
            
            if st.button("Logout", key="logout_button"):
                auth_state.logout()
                st.rerun()