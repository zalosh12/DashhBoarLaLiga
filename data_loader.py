import pandas as pd
import streamlit as st

def load_data():
    url = "https://raw.githubusercontent.com/zalosh12/la_liga_csv/refs/heads/main/matches_full.csv"
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e :
        st.error(f"Error loading data")
        return pd.DataFrame()

