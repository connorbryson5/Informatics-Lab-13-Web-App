# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:07:21 2023

@author: Connor
"""

# Libraries

import streamlit as st
import pandas as pd
import plotly.express as px

# Page Layout

st.set_page_config(layout = "wide", initial_sidebar_state= "expanded")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html = True)


st.sidebar.header('Lab 13 App')


# Data
dat = pd.read_csv("C:/Users/Connor/Desktop/Intro to Informatics/Labs/Lab 13/Informatics-Lab-13-Web-App/data/heart_2022_no_nans.csv")

had_stroke = dat[dat['HadStroke'] == "Yes"]

hist1 = px.histogram(had_stroke , x = 'Sex')


st.markdown('# Question for Final Project: What factors go into whether a person had a heart attack and who does it affect?')
st.markdown('## This simple web app filters the data to every person who had a Stroke and the bar chart shows how many of each gender had a stroke based on the data.')

# Row A
a1 = st.columns(1)

st.markdown('### Bar chart')
st.plotly_chart(hist1, use_container_width=True)


st.markdown('### The filtered data is shown below:')
st.dataframe(had_stroke)
