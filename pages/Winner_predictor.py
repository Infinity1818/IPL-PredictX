import streamlit as st
import pickle
import pandas as pd

def run_winner_predictor_page():
    teams = ['Sunrisers Hyderabad',
            'Mumbai Indians',
            'Royal Challengers Bengaluru',
            'Kolkata Knight Riders',
            'Punjab Kings',
            'Chennai Super Kings',
            'Rajasthan Royals',
            'Delhi Capitals',
            'Gujarat Titans',
            'Lucknow Super Giants']

    cities = ['Hyderabad', 'Mumbai', 'Bengaluru', 'Delhi', 'Kolkata',
               'Jaipur', 'Chandigarh', 'Chennai', 'Abu Dhabi', 'Navi Mumbai',
               'Sharjah', 'Nagpur', 'Dharamsala', 'Mohali', 'Dubai', 'Pune',
               'Ahmedabad', 'Visakhapatnam', 'Rajkot', 'Lucknow', 'Ranchi',
               'Cuttack', 'Guwahati', 'Raipur', 'Kanpur', 'Indore']

    wicket = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    over = [1,2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    # pipe = pickle.load(open('models/winner_predictor.pkl', 'rb'))
    pipe = pickle.load(open('models/winner_predictor_2022.pkl', 'rb'))
    st.title('Winner Predictor After First Inning')

    col1, col2 = st.columns(2)

    with col1:
        batting_team = st.selectbox('Select the chasing team', sorted(teams))
    with col2:
        bowling_team = st.selectbox('Select the defending team', sorted(teams))

    selected_city = st.selectbox('Select host city', sorted(cities))

    target = st.number_input('Target')

    col3, col4, col5 = st.columns(3)

    with col3:
        score = st.number_input('Score')
    with col4:
        overs = st.selectbox('Overs', sorted(over))
    with col5:
        wicket = st.selectbox('Wicket', sorted(wicket))

    if st.button('Predict Probability'):
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets = 10 - wicket
        crr = score / overs
        rrr = (runs_left * 6) / balls_left

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets],
            'target_runs': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]
        st.header(batting_team + "- " + str(round(win * 100)) + "%")
        st.header(bowling_team + "- " + str(round(loss * 100)) + "%")

