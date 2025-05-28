import streamlit as st

from functions.functions import global_init


def main_pie():
    global_init()
    # df = load_dataset()

    # custom_info_bar()

    cols = st.columns(2)

    with cols[0]:
        st.subheader(r"Youssef Samy Youssef")
        st.write(r"AI & ML Engineer")

        st.page_link(r'https://github.com/YosefSamy019', label='Open GitHub here')
        st.page_link(r'https://linkedin.com/in//yosef0samy/', label='Open Linkedin here')
        st.page_link(r'https://yosefsamy0portfolio.netlify.app', label='Open Portfolio here')

    with cols[1]:
        st.image(r'assets/cover.jpg')

main_pie()
