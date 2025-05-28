import plotly.express as px
import streamlit as st

from functions.functions import load_dataset, global_init, update_figure, get_color_discrete_sequence
from widgets.info_bar import custom_info_bar


def main_geography():
    global_init()

    df = load_dataset()
    unique_cities = df['City'].unique()
    unique_states = df['State'].unique()

    custom_info_bar()


    # Write All Cites
    with st.expander(f"Show All Cities ({len(unique_cities)}):"):
        st.dataframe(unique_cities)

    # Write All States
    with st.expander(f"Show All States ({len(unique_states)}):"):
        st.dataframe(unique_states)

    st.divider()

    st.subheader('Filters:')
    cols_filters = st.columns(3)

    Selected_categories = cols_filters[0].multiselect(
        "Select Category",
        df['Category'].unique(),
        default=df['Category'].unique(),
    )
    Selected_segments = cols_filters[1].multiselect(
        "Select Segment",
        df['Segment'].unique(),
        default=df['Segment'].unique(),
    )
    Selected_shipMode = cols_filters[2].multiselect(
        "Select Ship Mode",
        df['Ship Mode'].unique(),
        default=df['Ship Mode'].unique(),
    )

    if len(Selected_shipMode) > 0:
        df = df[ df['Ship Mode'].isin(Selected_shipMode)]
    if len(Selected_segments) > 0:
        df = df[ df['Segment'].isin(Selected_segments)]
    if len(Selected_categories) > 0:
        df = df[ df['Category'].isin(Selected_categories)]

    st.divider()

    # Delivery Days taken vs City
    df_temp = df.groupby('City')['Delivery Days'].mean()
    df_temp.sort_values(inplace=True, ascending=False)

    fig = px.bar(x=df_temp.index, y=df_temp.values, color_discrete_sequence=get_color_discrete_sequence(),
                 title='Average Delivery Days taken per City')
    fig.update_layout(
        xaxis_title='City',
        yaxis_title='Delivery Days taken',
    )
    update_figure(fig)
    st.plotly_chart(fig)

    # Delivery Days taken vs State
    df_temp = df.groupby('State')['Delivery Days'].mean()
    df_temp.sort_values(inplace=True, ascending=False)

    fig = px.bar(x=df_temp.index, y=df_temp.values, color_discrete_sequence=get_color_discrete_sequence(),
                 title='Average Delivery Days taken per State')
    fig.update_layout(
        xaxis_title='State',
        yaxis_title='Delivery Days taken'
    )
    update_figure(fig)
    st.plotly_chart(fig)

    # Number of orders vs City
    df_temp = df.groupby('City').size()
    df_temp.sort_values(inplace=True, ascending=False)

    fig = px.bar(x=df_temp.index, y=df_temp.values, color_discrete_sequence=get_color_discrete_sequence(),
                 title='Number of orders per City')
    fig.update_layout(
        xaxis_title='City',
        yaxis_title='Number of orders'
    )
    update_figure(fig)
    st.plotly_chart(fig)

    # Number of orders vs State
    df_temp = df.groupby('State').size()
    df_temp.sort_values(inplace=True, ascending=False)

    fig = px.bar(x=df_temp.index, y=df_temp.values, color_discrete_sequence=get_color_discrete_sequence(),
                 title='Number of orders per State')
    fig.update_layout(
        xaxis_title='State',
        yaxis_title='Number of orders'
    )
    update_figure(fig)
    st.plotly_chart(fig)

    # Total Profit vs City
    df_temp = df.groupby('City')['Profit'].sum()
    df_temp.sort_values(inplace=True, ascending=False)

    fig = px.bar(x=df_temp.index, y=df_temp.values, color_discrete_sequence=get_color_discrete_sequence(),
                 title='Total Profit per City')
    fig.update_layout(
        xaxis_title='City',
        yaxis_title='Total Profit'
    )
    update_figure(fig)
    st.plotly_chart(fig)

    # Total Profit vs State
    df_temp = df.groupby('State')['Profit'].sum()
    df_temp.sort_values(inplace=True, ascending=False)

    fig = px.bar(x=df_temp.index, y=df_temp.values, color_discrete_sequence=get_color_discrete_sequence(),
                 title='Total Profit per State')
    fig.update_layout(
        xaxis_title='State',
        yaxis_title='Total Profit'
    )
    update_figure(fig)
    st.plotly_chart(fig)


main_geography()
