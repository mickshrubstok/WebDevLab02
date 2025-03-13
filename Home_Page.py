import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

st.title("Mick Shrubstok")
st.subheader("CS 1301 - Web Development Lab 02")

st.write(
    """
    Welcome to my Streamlit Web App! You can use the sidebar to navigate between pages.
   
    **Pages:**
    - **Lebron's Portfolio** → Learn about Lebron’s career and hobbies.
    - **Lebron Data** → View interactive visualizations about Lebron’s activity.
    """
)

st.sidebar.title("Navigation")
st.sidebar.page_link("pages/1_Lebron's_Portfolio.py", label="📌 Lebron's Portfolio")  
st.sidebar.page_link("pages/2_Lebron_Data.py", label="📊 Lebron's Data")  

st.write("---")
st.write("Created for CS 1301 Web Development Lab 02")
