# PredictX!

Welcome to __PredictX!__

Get ready to elevate your IPL experience with our unique prediction tool! PredictX offers two exciting features:

__First Inning Score Prediction:__ Using advanced analytics and historical data, we provide real-time predictions for the first inning score, helping you anticipate the action on the field.

__Winning Team Prediction:__ After the first inning, we assess the first innings score, current score, and match dynamics to evaluate which team is more likely to secure victory in the match.


## Data Source


This project uses the [__Indian Premier League (IPL) - 2008-2024__](https://www.kaggle.com/datasets/saiprudvirajy/indian-premier-league-ipl-2008-2024) dataset available on __Kaggle__. The main files used are:

- IPL_BallByBall2008_2024(Updated).csv (renamed as __deliveries.csv__)
- team_performance_dataset_2008to2024.csv (renamed as __matches.csv__)

These datasets contain detailed historical match data including information such as:

- match_id: Unique match identifier
- inning: Inning number
- batting_team, bowling_team: Names of the batting and bowling teams
- is_wicket: Whether the ball resulted in a wicket
- season: IPL season year
- venue: Match venue
- winner: The winning team
## Acknowledgements

This project makes use of the following open-source libraries and frameworks:

- Pandas
- Numpy
- Scikit-Learn
- Kaggle
- Streamlit
- xgboost
I would like to express my gratitude to the developers of these tools for their invaluable contributions to the open-source community.


## Deployment
The application has been deployed in the Streamlit Cloud.

You can access it here: https://ipl-predictx.streamlit.app/
