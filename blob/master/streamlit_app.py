import streamlit as st

st.set_page_config(
    page_title="A/B Testing App", page_icon="📊", initial_sidebar_state="expanded"
)


number = st.slider("Pick a number", 0, 100)
