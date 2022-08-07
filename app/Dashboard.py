import streamlit as st

from app.components.navbar import navbar
from app.components.dashboard import dashboard

navbar()
dashboard()
st.sidebar.markdown("# Dashboard")
