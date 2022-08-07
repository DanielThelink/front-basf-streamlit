import streamlit as st

from app.components.navbar import navbar
from app.components.words import words

navbar()
words()
st.sidebar.markdown("# CodeTracker")
