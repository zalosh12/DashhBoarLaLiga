import streamlit as st

def sidebar_filters(df):
    st.sidebar.header("Data Filters")

    st.sidebar.header('Data filters')
    st.sidebar.write("Select a team and seasons")

    team_list = sorted(df['team'].unique().tolist())
    selected_team = st.sidebar.selectbox(
        'Select Team:',
        team_list,
        index=0
    )

    season_list = sorted(df['season'].unique().tolist())
    selected_season = st.sidebar.selectbox(
        'Select Season:',
        season_list,
        index=0
    )

    return {
        'team':selected_team,
        'season':selected_season
    }


# def sidebar_filters(movies_data):
#     st.sidebar.header("Data Filters")
#
#     st.sidebar.write("Select a score range to see the number of movies per genre")
#
#     score_range = st.sidebar.slider(
#         label="Select Score Range:",
#         min_value=1.0,
#         max_value=10.0,
#         value=(3.0, 4.0)
#     )
#
#     genre_list = movies_data['genre'].unique().tolist()
#     selected_genres = st.sidebar.multiselect(
#         'Select Genres:',
#         genre_list,
#         default=['Animation', 'Horror', 'Fantasy', 'Romance']
#     )
#
#     year_list = sorted(movies_data['year'].unique().tolist())
#     selected_year = st.sidebar.selectbox(
#         'Select Year:',
#         year_list,
#         index=0
#     )
#
#     country_list = sorted(movies_data['year'].unique().tolist())
#     selected_country = st.sidebar.selectbox(
#         'Country:',
#         country_list,
#         index = 0
#     )
#
#     return {
#         'score_range': score_range,
#         'genres': selected_genres,
#         'year': selected_year
#     }