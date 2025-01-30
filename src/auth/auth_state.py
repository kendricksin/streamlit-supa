# src/auth/auth_state.py
import streamlit as st
from typing import Optional, Dict, Any
from supabase import Client

class AuthState:
    """Manages authentication state for the application."""
    
    def __init__(self, supabase: Client):
        self.supabase = supabase
        if 'user' not in st.session_state:
            st.session_state.user = None

    def sign_up(self, email: str, password: str) -> bool:
        """Register a new user."""
        try:
            response = self.supabase.auth.sign_up({
                "email": email,
                "password": password
            })
            st.success("Registration successful! Please check your email for verification.")
            return True
        except Exception as e:
            st.error(f"Registration failed: {str(e)}")
            return False

    def login(self, email: str, password: str) -> bool:
        """Log in an existing user."""
        try:
            response = self.supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            st.session_state.user = response.user
            return True
        except Exception as e:
            st.error(f"Login failed: {str(e)}")
            return False

    def logout(self) -> None:
        """Log out the current user."""
        try:
            self.supabase.auth.sign_out()
            st.session_state.user = None
        except Exception as e:
            st.error(f"Logout failed: {str(e)}")

    @property
    def is_authenticated(self) -> bool:
        """Check if user is authenticated."""
        return st.session_state.user is not None

    def get_user(self) -> Optional[Dict[str, Any]]:
        """Get current user data."""
        return st.session_state.user