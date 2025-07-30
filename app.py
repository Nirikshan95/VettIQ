import streamlit as st
import requests
from config import BASE_URL

def main():
    st.set_page_config(page_title="VettIQ", layout="centered", initial_sidebar_state="auto",page_icon=":mag_right:")
    st.title("VettIQ : starup idea validation tool")
    st.write("This tool allows you to perform market analysis, competitor analysis, risk assessment, and receive advice on your startup idea.")
    idea=st.text_area("Enter your startup idea :")
    
    if st.button("validate"):
        if idea:  
            with st.spinner("validating..."):
                try:
                    result=requests.post(f"{BASE_URL}/validate", json={"startup_idea": idea})
                    if result.status_code == 200:
                        st.success("Validation successful!")
                        result = result.json()
                        st.markdown("# Validation :\n")
                        st.markdown(f"advice:\n {result['advice']}\n\n")
                        st.markdown(f"advisor_recommendations:\n {result['advisor_recommendations']}\n")
                        st.markdown("# Analysis Results:")
                        st.markdown(f"## startup_idea:\n {result['startup_idea']}")
                        st.markdown(f"## market_analysis:\n {result['market_analysis']}")
                        st.markdown(f"## competition_analysis:\n {result['competition_analysis']}")
                        st.markdown(f"## risk_assessment:\n {result['risk_assessment']}")
                    else:
                        st.error(f"Error: {result.status_code} - {result.text}")
                except requests.exceptions.ConnectionError:
                    st.error("Error: Unable to connect to the VettIQ API. Please ensure the server is running.")
            
        else:
            st.error("Please enter a search query.")

if __name__ == "__main__":
    main()