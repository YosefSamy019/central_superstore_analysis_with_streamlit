import pandas as pd
import streamlit as st


def global_init():
    FIRST_RUN_KEY = 'FRK'
    if FIRST_RUN_KEY not in st.session_state:
        st.session_state[FIRST_RUN_KEY] = True

    st.set_page_config(page_title='Central Superstore Analysis', page_icon='📈', layout="wide")


def fun_unify_numer(number):
    units = [
        (10 ** 9, 'G'),
        (10 ** 6, 'M'),
        (10 ** 3, 'K'),
    ]

    for multiplier, unit in units:
        if number > multiplier:
            return f"{(number / multiplier):0.2f} {unit}"

    return str(number)


@st.cache_resource
def load_dataset():
    df = pd.read_excel(r'Central_Superstore_with_lat_lon.xlsx')

    # add new feature
    df['Order Date Year'] = pd.DatetimeIndex(df['Order Date']).year.astype(int)
    df['Order Date Month'] = pd.DatetimeIndex(df['Order Date']).month.astype(int)

    # add new feature
    df['Delivery Days'] = (pd.DatetimeIndex(df['Ship Date']) - pd.DatetimeIndex(df['Order Date'])).astype(int) / (
            24 * 60 * 60 * (10 ** 9))
    df['Delivery Days'] = df['Delivery Days'].astype(int)

    return df


def update_figure(fig):
    fig.update_layout(
        plot_bgcolor='#F3F0D9',
        paper_bgcolor='#F3F0D9',
        legend_title_font_color="#573200",
        title_font=dict(size=16, color='#573200'),
        font=dict(size=14, color='#FFFFFF'),
    )

    fig.update_xaxes(
        title_font=dict(size=16, color='#573200', family='Georgia, serif'),
        tickfont=dict(size=14, color='#784600', family='Georgia, serif'),
        showgrid=True,
        gridcolor='lightgray'
    )

    fig.update_yaxes(
        title_font=dict(size=16, color='#573200', family='Georgia, serif'),
        tickfont=dict(size=14, color='#784600', family='Georgia, serif'),
        showgrid=True,
        gridcolor='lightgray'
    )


def get_color_discrete_sequence():
    return ['#573200']
