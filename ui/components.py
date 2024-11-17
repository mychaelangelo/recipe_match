import streamlit as st

def render_title():
    st.title("🥙 Recipe Finder")
    st.write("Submit an image or PDF of the ingredients you have and GPT4o will suggest recipes.")

def render_api_key_input():
    return st.text_input("Enter your OpenAI API Key:", type="password")

def render_input_method_selector():
    st.write("Choose your input method:")
    return st.radio("Select input method:", ["Upload File", "Take Picture"])

def render_results(final_text):
    st.markdown("# AI Results:")
    st.markdown(final_text)
    
    st.download_button(
        label="Download as Markdown",
        data=final_text,
        file_name="extracted_content.md",
        mime="text/markdown"
    )
