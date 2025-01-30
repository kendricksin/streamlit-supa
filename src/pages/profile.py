# src/pages/profile.py
import streamlit as st
from ..auth.auth_state import AuthState

def render_profile(auth_state: AuthState) -> None:
    st.title("Profile")
    
    user = auth_state.get_user()
    if user:
        st.write("### User Information")
        st.write(f"Email: {user['email']}")
        st.write(f"ID: {user['id']}")
        st.write(f"Last Sign In: {user['last_sign_in_at']}")
        
        st.write("### Preferences")
        st.checkbox("Enable notifications", value=True)
        st.checkbox("Dark mode", value=False)
        
        if st.button("Save Preferences"):
            st.success("Preferences saved!")