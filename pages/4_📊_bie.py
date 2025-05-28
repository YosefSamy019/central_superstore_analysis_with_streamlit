import plotly.express as px
import streamlit as st

from functions.functions import load_dataset, global_init, update_figure, get_color_discrete_sequence
from widgets.info_bar import custom_info_bar


def main_pie():
    global_init()
    df = load_dataset()

    custom_info_bar()

    # Ship Mode
    cols_1 = st.columns([0.7, 0.3])
    df_temp = df.groupby('Ship Mode').size().reset_index(name='Size')
    with cols_1[0]:
        fig = px.pie(df_temp, names='Ship Mode', values='Size', title='Ship Mode',
                     color_discrete_sequence=get_color_discrete_sequence(), )
        update_figure(fig)
        st.plotly_chart(fig)

    with cols_1[1]:
        st.container(height=1, border=False)
        update_figure(fig)
        st.dataframe(df_temp)

    # Segment
    cols_1 = st.columns([0.7, 0.3])
    df_temp = df.groupby('Segment').size().reset_index(name='Size')
    with cols_1[0]:
        fig = px.pie(df_temp, names='Segment', values='Size', title='Segment',
                     color_discrete_sequence=get_color_discrete_sequence(), )
        update_figure(fig)
        st.plotly_chart(fig)

    with cols_1[1]:
        st.container(height=1, border=False)
        update_figure(fig)
        st.dataframe(df_temp)

    # City
    cols_1 = st.columns([0.7, 0.3])
    df_temp = df.groupby('City').size().reset_index(name='Size')
    df_temp = df_temp.sort_values('Size', ascending=False).head(10)

    with cols_1[0]:
        fig = px.pie(df_temp, names='City', values='Size', title='City (Top 10 only)',
                     color_discrete_sequence=get_color_discrete_sequence(), )
        update_figure(fig)
        st.plotly_chart(fig)

    with cols_1[1]:
        st.container(height=1, border=False)
        update_figure(fig)
        st.dataframe(df_temp)

    # State
    cols_1 = st.columns([0.7, 0.3])
    df_temp = df.groupby('State').size().reset_index(name='Size')
    with cols_1[0]:
        fig = px.pie(df_temp, names='State', values='Size', title='State',
                     color_discrete_sequence=get_color_discrete_sequence(), )
        update_figure(fig)
        st.plotly_chart(fig)

    with cols_1[1]:
        st.container(height=1, border=False)
        update_figure(fig)
        st.dataframe(df_temp)


main_pie()
