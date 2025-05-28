import pandas as pd
import plotly.express as px
import streamlit as st

from functions.functions import load_dataset, global_init, update_figure, get_color_discrete_sequence
from widgets.info_bar import custom_info_bar


def main_customers():
    global_init()

    df = load_dataset()

    custom_info_bar()

    # Orders vs Customer ID
    df_temp = df.groupby('Customer ID').size().reset_index(name='Order Count')
    df_temp.sort_values(by='Order Count', inplace=True, ascending=False)

    fig = px.bar(df_temp, x='Customer ID', y='Order Count',
                 color_discrete_sequence=get_color_discrete_sequence(),
                 title='Total Number of Orders per Customer ID')
    update_figure(fig)
    st.plotly_chart(fig)

    # Mean Quantity vs Customer ID
    df_temp = df.groupby('Customer ID')['Quantity'].mean()
    df_temp.sort_values(inplace=True, ascending=False)

    fig = px.bar(x=df_temp.index, y=df_temp.values, color_discrete_sequence=get_color_discrete_sequence(),
                 title='Average Number of Quantity per Customer ID')
    fig.update_layout(
        xaxis_title='Customer ID',
        yaxis_title='Average Number of Quantity'
    )

    update_figure(fig)
    st.plotly_chart(fig)

    # Profit sum vs Customer ID
    df_temp = df.groupby('Customer ID')['Profit'].sum()
    df_temp.sort_values(inplace=True, ascending=False)

    fig = px.bar(x=df_temp.index, y=df_temp.values, color_discrete_sequence=get_color_discrete_sequence(),
                 title='Total Profit per Customer per Customer ID')
    fig.update_layout(
        xaxis_title='Customer ID',
        yaxis_title='Total Profit per Customer'
    )
    update_figure(fig)
    st.plotly_chart(fig)

    cols = st.columns(2)
    with cols[0]:
        # Profit sum vs Segment
        df_temp = df.groupby('Segment')['Profit'].sum()
        df_temp.sort_values(inplace=True, ascending=False)

        fig = px.bar(x=df_temp.index, y=df_temp.values, color_discrete_sequence=get_color_discrete_sequence(),
                     title='Total Profit per Segment')
        fig.update_layout(
            xaxis_title='Segment',
            yaxis_title='Total Profit'
        )
        update_figure(fig)
        st.plotly_chart(fig)

    with cols[1]:
        # Customer ID vs Year
        df_unique = df.drop_duplicates(subset=['Order Date Year', 'Customer ID'])

        df_temp = df_unique.groupby('Order Date Year')['Customer ID'].count()

        fig = px.line(x=df_temp.index, y=df_temp.values, color_discrete_sequence=get_color_discrete_sequence(),
                      title='Number of Customers per Year')
        fig.update_xaxes(
            dtick=1,
            range=[df_temp.index.min() - 0.1, df_temp.index.max() + 0.1]  # Expand range slightly to show edges
        )
        fig.update_layout(
            xaxis_title='Year',
            yaxis_title='Number of Customers'
        )
        update_figure(fig)
        st.plotly_chart(fig)


main_customers()
