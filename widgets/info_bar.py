import streamlit as st

from functions.functions import fun_unify_numer, load_dataset


def custom_info_bar():
    df = load_dataset()

    unique_users = df['Customer ID'].unique()
    unique_cities = df['City'].unique()
    unique_states = df['State'].unique()
    unique_products = df['Product ID'].unique()

    total_profit = df['Profit'].sum()

    cols = st.columns(6)


    with cols[0]:
        st.metric(label="💰 Total Profit",
                  border=True, value=fun_unify_numer(total_profit))

    with cols[1]:
        st.metric(label="📦 Number of Products", border=True, value=fun_unify_numer(len(unique_products)))

    with cols[2]:
        st.metric(label="🫳 Number of orders", border=True, value=fun_unify_numer(len(df)))

    with cols[3]:
        st.metric(label="🏢 Number of cities", border=True, value=fun_unify_numer(len(unique_cities)))

    with cols[4]:
        st.metric(label="🏢 Number of states", border=True, value=fun_unify_numer(len(unique_states)))

    with cols[5]:
        st.metric(label="👱 Number of Users", border=True, value=fun_unify_numer(len(unique_users)))

