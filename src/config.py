# src/config.py
from pathlib import Path
import streamlit as st
from supabase import create_client, Client

def get_supabase() -> Client:
    """Initialize and return Supabase client."""
    if 'supabase' not in st.session_state:
        supabase_url = st.secrets["supabase_url"]
        supabase_key = st.secrets["supabase_key"]
        st.session_state.supabase = create_client(supabase_url, supabase_key)
    return st.session_state.supabase