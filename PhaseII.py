import streamlit as st
import pandas as pd
import json

# Set up the page
st.set_page_config(page_title="Phase II - LeBron's Advanced Data", layout="wide")

st.title("LeBron James - Advanced Analytics")
st.write("Dive deeper into LeBron's stats with advanced data visualizations and interactive elements.")

# Load data from JSON file
file = open("data.json", "r")
infile = file.readlines()
data = json.loads("".join(infile))
file.close()

# Convert JSON data to DataFrame
df = pd.DataFrame(data['stats'])
df.index += 1  # Start index at 1 instead of 0

# NEW: User Interaction - Selectbox for Metric Selection
metric = st.selectbox("Select a Statistic to Visualize:", ["PPG", "APG", "RPG"])

# NEW: Line Chart for Selected Metric
st.subheader(f"LeBron's {metric} Over His Career")
st.line_chart(df.set_index("Season")[metric])

# NEW: Interactive Slider to Filter by Minimum Points Per Game
min_ppg = st.slider("Minimum Points Per Game", min_value=int(df["PPG"].min()), max_value=int(df["PPG"].max()), value=20)
filtered_df = df[df["PPG"] >= min_ppg]
st.write(filtered_df)

# NEW: Checkbox to Show Career Averages
if st.checkbox("Show Career Averages"):
    st.write(df.mean(numeric_only=True))

st.write("---")
st.write("Created for CS 1301 Web Development Lab 02")
