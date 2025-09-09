# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st


st.sidebar.title('Title')
sidebar_option = st.sidebar.selectbox('Select an option: ', ['Data info', 'First analysis', 'Second analysis'])

if(sidebar_option == 'Data info'):
    st.title('Streamlit Demos')
    st.write('Welcome!')
    st.header('Data:')

    
if(sidebar_option == 'First analysis'):
    st.title('Analysis')
    st.write('Welcome!')
    st.header('First analysis')
    
    country = st.selectbox('Select a country: ', ['Italy', 'France', 'Spain'])
    st.write('You select: ', country)
    
    st.subheader('Streamlit chart')
    #st.line_chart(df)
    
    
if(sidebar_option == 'Second analysis'):
    st.title('Analysis')
    st.write('Welcome!')
    st.header('Second analysis')
    
    country = st.selectbox('Select a country: ', ['Italy', 'France', 'Spain'])
    st.write('You select: ', country)
    
    st.subheader('Streamlit chart')