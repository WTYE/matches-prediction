import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="matches-prediction-app",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

# Load the results from the model_training script
results = pd.read_csv('../data/processed/rolling_matches.csv')

# Display the results in a Streamlit app
st.title('Matches Model Training Results')
st.dataframe(results)



