import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.express
st.title("Iris Dashboard")
df=pd.read_csv('iris.csv')
st.dataframe(df)


fig1,ax=plt.subplots()
ax.scatter(df.iloc[:,0],df.iloc[:,1])

fig2,ax=plt.subplots()
ax.scatter(df.iloc[:,2],df.iloc[:,3])

col1,col2=st.columns(2)
with col1:st.pyplot(fig1)
with col2:st.pyplot(fig2)

t=df['species'].value_counts()
st.write(t)
st.bar_chart(t)
st.area_chart(df.iloc[:,3])
st.line_chart(df.iloc[:,0])

fig,ax=plt.subplots()
ax.hist(df.iloc[:,1],color='orange',bins=12)
st.line_chart(df.iloc[:,1])
st.pyplot(fig)
