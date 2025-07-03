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
