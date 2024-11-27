import streamlit as st
from pages2.Scorer_predictor import run_score_predictor_page
from pages2.Winner_predictor import run_winner_predictor_page
from pages2.Home import home_page

# Add custom CSS for button styles
st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;  /* Green */
    color: white;                /* Text color */
    border: none;                /* No border */
    padding: 10px 20px;         /* Padding */
    text-align: center;          /* Centered text */
    text-decoration: none;        /* No underline */
    display: inline-block;        /* Inline block */
    font-size: 20px;             /* Font size */
    margin: 4px 2px;            /* Margin */
    cursor: pointer;             /* Pointer cursor */
    border-radius: 2px;         /* Rounded corners */
}

.stButton>button:hover {
    background-color: #45a049;   /* Darker green on hover */
}
</style>
""", unsafe_allow_html=True)

col1,  = st.columns(1)
# Place buttons in separate columns to align them on the same row
with col1:
    if st.button("Home"):
        st.session_state['page'] = "Home Page"

# Determine which page to display
if 'page' not in st.session_state:
    st.session_state['page'] = "Home Page"

if st.session_state['page'] == "Score Predictor":
    run_score_predictor_page()
elif st.session_state['page'] == "Winner Predictor":
    run_winner_predictor_page()
elif st.session_state['page'] == "Home Page":
    home_page()

col2, col3 = st.columns(2)
with col3:
    if st.button("Go to Winner Predictor"):
        st.session_state['page'] = "Winner Predictor"

with col2:
    if st.button("Go to Score Predictor"):
        st.session_state['page'] = "Score Predictor"
