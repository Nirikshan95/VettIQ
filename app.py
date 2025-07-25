import streamlit as st
from graphs.workflow import build_graph

def main():
    st.set_page_config(page_title="VettIQ", layout="centered", initial_sidebar_state="auto",page_icon=":mag_right:")
    st.title("VettIQ : starup idea validation tool")
    st.write("This tool allows you to perform market analysis, competitor analysis, risk assessment, and receive advice on your startup idea.")
    idea=st.input_text = st.text_input("Enter your startup idea :")
    if st.button("validate"):
        if idea:
            vettiQ = build_graph()
            with st.spinner("Bot Thinking..."):
                result=vettiQ.invoke({"startup_idea":idea})
            st.write("Search Results:")
            st.write(f"startup_idea\n :{result['startup_idea']}")
            st.write(f"market_analysis\n :{result['market_analysis']}")
            st.write(f"competition_analysis\n :{result['competition_analysis']}")
            st.write(f"risk_assessment\n :{result['risk_assessment']}")
            st.write(f"advisor_recommendations\n :{result['advisor_recommendations']}")
            st.write(f"advice\n :{result['advice']}")
            
        else:
            st.error("Please enter a search query.")

if __name__ == "__main__":
    main()