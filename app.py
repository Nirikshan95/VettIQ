import streamlit as st
import requests
from graphs.workflow import build_graph
from config import BASE_URL

def main():
    st.set_page_config(page_title="VettIQ", layout="centered", initial_sidebar_state="auto",page_icon=":mag_right:")
    st.title("VettIQ : starup idea validation tool")
    st.write("This tool allows you to perform market analysis, competitor analysis, risk assessment, and receive advice on your startup idea.")
    idea=st.input_text = st.text_input("Enter your startup idea :")
    vettiQ = build_graph()
    if st.button("validate"):
        if idea:
            
            with st.spinner("Bot Thinking..."):
                try:
                    result=requests.post(f"{BASE_URL}/validate", json={"startup_idea": idea})
                    if result.status_code == 200:
                        result = result.json()
                        result=result['validation_result']
                        st.write("Search Results:")
                        st.write(f"startup_idea\n :{result['startup_idea']}")
                        st.write(f"market_analysis\n :{result['market_analysis']}")
                        st.write(f"competition_analysis\n :{result['competition_analysis']}")
                        st.write(f"risk_assessment\n :{result['risk_assessment']}")
                        st.write(f"advisor_recommendations\n :{result['advisor_recommendations']}")
                        st.write(f"advice\n :{result['advice']}")
                    else:
                        st.error(f"Error: {result.status_code} - {result.text}")
                except requests.exceptions.ConnectionError:
                    st.error("Error: Unable to connect to the VettIQ API. Please ensure the server is running.")
            
        else:
            st.error("Please enter a search query.")

if __name__ == "__main__":
    main()