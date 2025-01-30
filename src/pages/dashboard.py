# src/pages/dashboard.py
import streamlit as st
from ..auth.auth_state import AuthState

def render_dashboard(auth_state: AuthState) -> None:
    st.title("Dashboard")
    
    # Test content for authenticated users
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            label="Sample Metric",
            value="42",
            delta="10.5%"
        )
        
    with col2:
        st.metric(
            label="Another Metric",
            value="123",
            delta="-5.2%"
        )
    
    # Test interactive elements
    st.subheader("Test Controls")
    test_value = st.slider("Test Slider", 0, 100, 50)
    st.write(f"Selected value: {test_value}")
    
    if st.button("Test Action"):
        st.success("Button clicked!")