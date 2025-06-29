import streamlit as st
from tools.web_search_tool import web_search

def main():
    st.set_page_config(page_title="VettIQ", layout="centered", initial_sidebar_state="auto",page_icon=":mag_right:")
    st.title("VettIQ Web Search Tool")
    st.write("This tool allows you to perform web searches using DuckDuckGo.")
    query=st.input_text = st.text_input("Enter your search query:")
    if st.button("Search"):
        if query:
            result = web_search(query)
            st.write("Search Results:")
            st.write(result)
        else:
            st.error("Please enter a search query.")

if __name__ == "__main__":
    main()