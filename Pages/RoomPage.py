import streamlit as st
st.title("Page1")
st.sidebar.title("hello")


if(st.button("back")):
    st.switch_page("LoginPage.py")

