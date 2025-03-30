import streamlit as st
import pandas as pd
import dashboard  # Import the dashboard module
import cv  # Import the CV module
import cover_letter  # Import the cover letter module

# Set wide mode
st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("vgsales.csv")

# Load dataset
df = load_data()

# Streamlit Sidebar
st.sidebar.title("📊 Video Game Sales Dashboard")
page = st.sidebar.radio("Select Analysis", ["Dashboard",  "CV", "Cover Letter"])

# Global Filters (for analysis pages)
st.sidebar.header("Filters")
platform = st.sidebar.multiselect("Platform", options=df["Platform"].unique(), default=df["Platform"].unique())
genre = st.sidebar.multiselect("Genre", options=df["Genre"].unique(), default=df["Genre"].unique())
year = st.sidebar.slider("Year Range", int(df["Year"].min()), int(df["Year"].max()), (2000, 2020))
publisher = st.sidebar.multiselect("Publisher", options=df["Publisher"].unique(), default=df["Publisher"].unique()[:5])

# Filter data (for analysis pages)
filtered_df = df[
    (df["Platform"].isin(platform)) &
    (df["Genre"].isin(genre)) &
    (df["Year"].between(year[0], year[1], inclusive="both")) &
    (df["Publisher"].isin(publisher))
]

# Display selected analysis
if page == "Dashboard":
    dashboard.show_dashboard(filtered_df)
elif page == "CV":
    cv.show_cv()
elif page == "Cover Letter":
    cover_letter.show_cover_letter()  # Call the cover letter function from cover_letter.py