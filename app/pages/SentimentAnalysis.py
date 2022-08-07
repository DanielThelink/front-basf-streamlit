import streamlit as st

from app.components.navbar import navbar
from app.components.sentiment_analisys import sentiment_analisys

st.sidebar.markdown("# SentimentAnalysis")
navbar()
sentiment_analisys()
