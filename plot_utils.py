import plotly.express as px

def plot_pie_results(df,filters):
    mask = (df['team'] == filters['team']) & (df['season'] == filters['season'])
    clean_df = df[mask]

    result_counts = clean_df['result'].value_counts().reset_index()
    result_counts.columns = ['result', 'count']

    fig = px.pie(
        result_counts,
        names='result',
        values='count',
        title='Match Results Distribution'
    )

    return fig