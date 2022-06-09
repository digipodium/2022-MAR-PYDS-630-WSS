
import streamlit as st
from seaborn import load_dataset
import pandas as pd
import plotly.express as px

st.title("Streamlit App Example: Data science")
penguins = load_dataset('penguins')
with st.expander("Penguins Data", expanded=False):
    st.write(penguins)

options = ['Bar Chart','Histogram','Scatter Plot']
choice = st.selectbox('Select an option',options)

if choice == options[0]:
    c1,c2 = st.columns(2)
    x = c1.selectbox('Select x-axis',penguins.columns)
    y = c2.selectbox('Select y-axis',penguins.columns)
    st.plotly_chart(px.bar(penguins,x=x,y=y))

if choice == options[1]:
    c1,c2 = st.columns(2)
    x = c1.selectbox('Select x-axis',penguins.columns)
    y = c2.selectbox('Select y-axis',penguins.columns)
    st.plotly_chart(px.histogram(penguins,x=x,y=y))

if choice == options[2]:
    c1,c2 = st.columns(2)
    x = c1.selectbox('Select x-axis',penguins.columns)
    y = c2.selectbox('Select y-axis',penguins.columns)
    st.plotly_chart(px.scatter(penguins,x=x,y=y))
