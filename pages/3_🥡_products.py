import plotly.express as px
import streamlit as st

from functions.functions import load_dataset, global_init, update_figure, get_color_discrete_sequence
from widgets.info_bar import custom_info_bar


def main_products():
    global_init()
    df = load_dataset()

    custom_info_bar()

    st.divider()

    st.subheader('Filters:')
    cols_filters = st.columns(1)

    Selected_states = cols_filters[0].multiselect(
        "Select States",
        df['State'].unique(),
        default=df['State'].unique(),
    )

    if len(Selected_states) > 0:
        df = df[df['State'].isin(Selected_states)]

    st.divider()

    cols_1 = st.columns(2)

    with cols_1[0]:
        # Total Number of Delivery Days per Category
        df_temp = df.groupby('Category')['Delivery Days'].mean()

        fig = px.bar(x=df_temp.index, y=df_temp.values,color_discrete_sequence=get_color_discrete_sequence(),
                     title='Average Number of Delivery Days per Category')
        fig.update_layout(
            xaxis_title='Category',
            yaxis_title='Average Number of Delivery Days'
        )
        update_figure(fig)
        st.plotly_chart(fig)

    with cols_1[1]:
        # Total Profit per Category
        df_temp = df.groupby('Category')['Profit'].sum()

        fig = px.bar(x=df_temp.index, y=df_temp.values,color_discrete_sequence=get_color_discrete_sequence(),
                     title='Total Number of Delivery Days per Category')
        fig.update_layout(
            xaxis_title='Category',
            yaxis_title='Total Number of Profit'
        )
        update_figure(fig)
        st.plotly_chart(fig)


    cols_2 = st.columns(2)

    with cols_2[0]:
        # Total Profit per product ID
        df_temp = df.groupby('Product ID')['Profit'].sum()
        df_temp.sort_values(inplace = True, ascending = False)

        fig = px.bar(x=df_temp.index, y=df_temp.values,color_discrete_sequence=get_color_discrete_sequence(),
                     title='Total Number of Delivery Days per Product ID')
        fig.update_layout(
            xaxis_title='Product ID',
            yaxis_title='Total Number of Profit'
        )
        update_figure(fig)
        st.plotly_chart(fig)

    with cols_2[1]:
        # Total Profit per Year
        df_temp = df.groupby('Order Date Year')['Profit'].sum()

        fig = px.line(x=df_temp.index, y=df_temp.values,color_discrete_sequence=get_color_discrete_sequence(),
                     title='Total Profit per Year')
        fig.update_layout(
            xaxis_title='Year',
            yaxis_title='Total Profit'
        )
        fig.update_xaxes(
            dtick=1,
            range=[df_temp.index.min() - 0.1, df_temp.index.max() + 0.1]  # Expand range slightly to show edges
        )
        update_figure(fig)
        st.plotly_chart(fig)

main_products()
