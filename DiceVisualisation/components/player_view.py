import streamlit as st

def display_player(name, score):
    st.sidebar.header("Player Info")
    st.sidebar.write(f"Name: {name}")
    st.sidebar.write(f"Score: {score}")
