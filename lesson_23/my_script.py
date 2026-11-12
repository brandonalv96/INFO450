import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

# Load the data
file_path = Path(__file__).parent / 'Advertising_F.csv'
df = pd.read_csv(file_path)

# Title
st.title('Advertising Effectiveness Brandon')

# Sidebar filters
st.sidebar.header('Filters')

x_var = st.sidebar.selectbox(
    'X axis',
    ['TV', 'Radio', 'Newspaper']
)

# Show scatterplot
fig = px.scatter(
    df,
    x=x_var,
    y='Sales',
    title='Advertising Spending vs Sales'
)

st.plotly_chart(fig)

# Show bar chart
sales_by_channel = pd.DataFrame({
    'Channel': ['TV', 'Radio', 'Newspaper'],
    'Total Spending': [
        df['TV'].sum(),
        df['Radio'].sum(),
        df['Newspaper'].sum()
    ]
})

fig = px.bar(
    sales_by_channel,
    x='Channel',
    y='Total Spending',
    title='Total Advertising Spending by Channel'
)

st.plotly_chart(fig)

# Show dataframe
st.dataframe(df)
