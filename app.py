import streamlit as st
from pages.Scorer_predictor import run_score_predictor_page
from pages.Winner_predictor import run_winner_predictor_page

# App title
st.title("IPL Winner and Score Predictor")

# Navigation buttons
col1, col2 = st.columns(2)
# Place buttons in separate columns to align them on the same row
with col1:
    if st.button("Go to Winner Predictor"):
        st.session_state['page'] = "Winner Predictor"

with col2:
    if st.button("Go to Score Predictor"):
        st.session_state['page'] = "Score Predictor"

# Determine which page to display
if 'page' not in st.session_state:
    st.session_state['page'] = "Winner Predictor"


if st.session_state['page'] == "Score Predictor":
    run_score_predictor_page()
elif st.session_state['page'] == "Winner Predictor":
    run_winner_predictor_page()





