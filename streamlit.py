# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.sidebar.title('Title')
sidebar_option = st.sidebar.selectbox('Select an option: ', ['Data info', 'First analysis', 'Second analysis'])

if(sidebar_option == 'Data info'):
    st.title('Data')
    st.write('''
             The data used in this analysis were sourced from the World Bank database, 
             chosen for its breadth of indicators and standardized format, which facilitates
             data processing and integration through Python. As is often the case with large
             international datasets, some values were missing for specific countries or years.
             To address these limitations and in consideration of time constraints, the scope 
             of the analysis was restricted to the last 50 years. Furthermore, the focus was 
             narrowed to five countries or regions deemed particularly relevant for comparison:
                 the EU27, China, the United States, India, and the global aggregate.
            '''          
             )
    st.header('Emissions')
    st.write('''         
    
            DATA SOURCE
            
            https://data.worldbank.org/indicator/EN.GHG.CO2.IP.MT.CE.AR5?most_recent_value_desc=true
            
            EDGAR ( Emissions Database for Global Atmospheric Research ) Community GHG Database, Joint Research Centre ( JRC ) - European Commission, uri: edgar.jrc.ec.europa.eu/dataset_ghg2032, publisher: JRC European Commission, date published: 2024; International Energy Agency ( IEA ), uri: edgar.jrc.ec.europa.eu/dataset_ghg2032, publisher: JRC European Commission, date published: 2024
            
            INDICATOR_NAME
            
            Carbon dioxide (CO2) emissions from Industrial Processes (Mt CO2e)	
            
            SOURCE_NOTE
            
            A measure of annual emissions of carbon dioxide (CO2), one of the six Kyoto greenhouse gases (GHG), from industrial processes including IPCC 2006 codes 2.A.1 Cement production, 2.A.2 Lime production, 2.A.3 Glass Production, 2.A.4 Other Process Uses of Carbonates, 2.B Chemical Industry, 2.C Metal Industry, 2.D Non-Energy Products from Fuels and Solvent Use, 2.E Electronics Industry, 2.F Product Uses as Substitutes for Ozone Depleting Substances, 2.G Other Product Manufacture and Use and 5.A Indirect N2O emissions from the atmospheric deposition of nitrogen in NOx and NH3). The measure is standardized to carbon dioxide equivalent values using the Global Warming Potential (GWP) factors of IPCC's 5th Assessment Report (AR5).
            ''')

    st.header('GDP')
    st.write('''
            DATA SOURCE
            
            https://data.worldbank.org/indicator/NY.GDP.MKTP.CD
            
            Country official statistics, National Statistical Organizations and/or Central Banks; National Accounts data files, Organisation for Economic Co-operation and Development ( OECD ); Staff estimates, World Bank ( WB )
            
            INDICATOR_NAME	
            
            GDP (current US$)
            
            SOURCE_NOTE
            
            Gross domestic product is the total income earned through the production of goods and services in an economic territory during an accounting period. It can be measured in three different ways: using either the expenditure approach, the income approach, or the production approach. This indicator is expressed in current prices, meaning no adjustment has been made to account for price changes over time. This indicator is expressed in United States dollars.
            Literacy rate:
            https://data.worldbank.org/indicator/SE.ADT.LITR.ZS
                         
             ''')

    
if(sidebar_option == 'First analysis'):
    st.title('First Analysis')
    st.write('The analysis of the graph shows clear differences in CO2 emissions from industrial activities relative to GDP across major global economies over the past 30 years. China currently exhibits the highest emissions per unit of economic output, followed by India. In contrast, the EU and the USA demonstrate significantly lower emission intensities, with the global average falling in between.')
    
    # data retreival

    df = pd.read_excel(r"C:\Users\WINASUS\Documents\CMCC\Python\Input_data.xlsx")  # Sostituisci col path corretto
    df.rename(columns = {'Year': 'year',
                         'Country Name': 'country'}, inplace = True)
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['value'] = df['Emissions']/df['GDP']
    
    # Sidebar
    st.sidebar.title("Filtri")
    
    # Select countries
    all_countries = sorted(df['country'].unique())
    selected_countries = st.sidebar.multiselect(
        "Seleziona i paesi",
        options=all_countries,
        default=['European Union', 'United States', 'World', 'China', 'India']
    )
    
    # Select year interval
    min_year = int(df['year'].min())
    max_year = int(df['year'].max())
    year_range = st.sidebar.slider(
        "Seleziona intervallo di anni",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )
    
    # Filter
    filtered_df = df[
        (df['country'].isin(selected_countries)) &
        (df['year'] >= year_range[0]) &
        (df['year'] <= year_range[1])
    ]
    
    # Title
    st.title("CO2 Emissions / GDP over time")
    st.caption("Interactive graph based on selected data")
    
    # Graph
    sns.set(style="whitegrid", context="talk", palette="colorblind")
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    sns.lineplot(
        data=filtered_df,
        x="year",
        y="value",
        hue="country",
        marker="o",
        linewidth=2.5,
        ax=ax
    )
    
    ax.set_title("Emissions and GDP ratio over time", fontsize=18, weight='bold')
    ax.set_xlabel("Year", fontsize=14)
    ax.set_ylabel("CO2 Emissions / GDP", fontsize=14)
    ax.legend(title="Country", fontsize=10)
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    
    # Streamlit
    st.pyplot(fig)
        

    
if(sidebar_option == 'Second analysis'):
    st.title('Second Analysis')
    st.write('''
            At the global level, data from the past 50 years shows no consistent decoupling: both GDP and emissions have generally increased in parallel. However, a notable shift occurs in 2023, where the two curves intersect — a potential early signal of global decoupling.
            Europe, on the other hand, stands out as a positive example. Over the same period, European GDP has steadily grown while CO2 emissions from industrial activities have declined, demonstrating that sustained economic growth without increased emissions is achievable.
            ''')
   
    
    df = pd.read_excel(r"C:\Users\WINASUS\Documents\CMCC\Python\Input_data.xlsx")  # Sostituisci col path corretto
    df.rename(columns = {'Year': 'year',
                         'Country Name': 'country',
                         'Emissions': 'emissions',
                         'GDP': 'gdp'}, inplace = True)
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['value'] = df['emissions']/df['gdp']
    
    # Country select
    st.sidebar.title("Select country")
    available_countries = sorted(df['country'].unique())
    selected_country = st.sidebar.selectbox("Select a country", available_countries, index=available_countries.index('European Union'))
    
    # Filtering
    df_country = df[df['country'] == selected_country].sort_values('year')
    
    # Style
    sns.set(style="whitegrid", context="talk", palette="colorblind")
    
    # Double Y-axis graph
    fig, ax1 = plt.subplots(figsize=(12, 7))
    
    # left Y-axis. Emissioni
    color_emissions = sns.color_palette("colorblind")[0]
    line1 = ax1.plot(df_country['year'], df_country['emissions'],
                     marker='o', color=color_emissions,
                     label="CO2 Emissions", linewidth=2.5)
    ax1.set_xlabel("Year", fontsize=14)
    ax1.set_ylabel("CO2 Emissions (tCO2)", color=color_emissions, fontsize=14)
    ax1.tick_params(axis='y', labelcolor=color_emissions)
    ax1.grid(True, linestyle='--', alpha=0.6)
    
    # right Y-axis: GDP
    ax2 = ax1.twinx()
    color_gdp = sns.color_palette("colorblind")[1]
    line2 = ax2.plot(df_country['year'], df_country['gdp'],
                     marker='s', color=color_gdp,
                     label="GDP", linewidth=2.5)
    ax2.set_ylabel("GDP (kUSD)", color=color_gdp, fontsize=14)
    ax2.tick_params(axis='y', labelcolor=color_gdp)
    
    # Title and legend
    plt.title(f"{selected_country} – Industrial CO2 emissions and GDP over time", fontsize=18, weight='bold')
    
    # Legend
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', fontsize=11)
    
    # Graph
    st.title("Emissioni CO2 and GDP over time")
    st.caption("Interactive graph with double Y-axis for the selected country")
    st.pyplot(fig)
        
    
