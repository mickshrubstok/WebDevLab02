import streamlit as st
import pandas as pd
import json

# Set up the page
st.set_page_config(page_title="LeBron's Data", layout="wide")

st.title("LeBron James - Data and Analytics")
st.write("Explore LeBron's career stats and achievements through interactive visualizations.")

# Load data from JSON file
file = open("data.json", "r")
infile = file.readlines()
data = json.loads("".join(infile))
file.close()

# Convert JSON data to DataFrame
df = pd.DataFrame(data['stats'])
df.index += 1  # Start index at 1 instead of 0

# Accumulate accolades correctly over the years
accolades_df = df[["Season"]].copy()
accolades_columns = ["Championships", "MVPs", "Finals MVPs", "All-Star Appearances", "Scoring Titles", "Rookie of the Year", "All-NBA Teams", "All-Defensive Teams"]

# Initialize empty columns
for col in accolades_columns:
    accolades_df[col] = 0
    df[col] = df[col].fillna(0)  # Ensure there are no NaN values

# Create a DataFrame for cumulative accolades
yearly_accolades_df = df[["Season"] + accolades_columns].copy()
cumulative_accolades = {col: 0 for col in accolades_columns}

with pd.option_context('mode.chained_assignment', None):  # Suppress chained assignment warning
    for i, row in df.iterrows():
        for col in accolades_columns:
            cumulative_accolades[col] += row[col]  # Add accolades only when achieved
            accolades_df.at[i, col] = cumulative_accolades[col]

# NEW: User interaction to filter by season
selected_season = st.selectbox("Select Season:", df["Season"].unique())
filtered_data = df[df["Season"] == selected_season][["Season", "PPG", "APG", "RPG"] + accolades_columns]
filtered_accolades = accolades_df[accolades_df["Season"] == selected_season]

st.subheader(f"LeBron's Stats for {selected_season}")
st.dataframe(filtered_data)

# NEW: Dynamic Visualization - Points per Season using Streamlit's built-in chart
st.subheader("LeBron's Scoring Over the Years")
st.line_chart(df.set_index("Season")["PPG"])

# NEW: Bar Chart - Comparing Assists and Rebounds per Season
st.subheader("LeBron's Assists vs. Rebounds Per Season")
st.bar_chart(df.set_index("Season")[["APG", "RPG"]])

# NEW: Display LeBron's cumulative career accolades over time
st.subheader("Career Accolades Over Time")
st.dataframe(accolades_df)

st.write("---")
st.write("Created for CS 1301 Web Development Lab 02")
