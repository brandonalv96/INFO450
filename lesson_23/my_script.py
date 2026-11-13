
import pandas as pd 
import streamlit as st
import plotly.express as px

df=pd.read_csv("lesson_23/Advertising_F")
st.title('Advertising Effectiveness Brandon')

st.sidebar.header('Filters')
x_var=st.selectbox('X axis',['TV','radio','newspaper'])

#Show scatterplot
px.scatter(df, x=x_var, y='sales',
           labels={'TV': 'TV add spend', 'radio': 'Radio add spend'})

st.plotly_chart(fig)

#show the barplot
sales_per_city=df.groupby('City')['sales'].sum().reset_index()
fig=px.bar(sales_per_city,x='City',y='sales',title='data is fun')
st.plotly_chart(fig)

#show the dataframe
st.dataframe(df)
