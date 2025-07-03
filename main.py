import streamlit as st
from data_loader import load_data
from sidebar_s import sidebar_filters
from plot_utils import plot_pie_results

def main():
    st.title("La Liga Dashboard")

    la_liga_data = load_data()

    if la_liga_data.empty:
        st.write("Dumb")

    filters = sidebar_filters(la_liga_data)

    fig = plot_pie_results(la_liga_data,filters)

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()



