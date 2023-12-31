import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

data=pd.read_csv('ottugi_review_topic_1.csv')

st.subheader('Check the reviews by selecting a product')
  
v_list=list(data['title'].unique())
var1 = st.selectbox(label = "Choose a Product", options = v_list,key=0)
title = f"Slect Topic: {var1}"

st.dataframe(data[data['title']==var1])
y_values=data[data['title']==var1]['topic'].value_counts().to_frame().reset_index(drop=False)

fig = px.bar(y_values, x = 'topic', y = 'count', title=title)
st.plotly_chart(fig)
