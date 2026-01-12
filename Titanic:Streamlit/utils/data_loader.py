import pandas as pd
from pathlib import Path
import streamlit as st

@st.cache_data
def load_data():
    data_path = Path(__file__).parent.parent / 'data/titanic_combined.csv'
    df = pd.read_csv(data_path)
    return df

