import streamlit as st

def handle_processing_error(error):
    st.error(f"An error occurred: {str(error)}")
