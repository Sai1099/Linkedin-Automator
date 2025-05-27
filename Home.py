import streamlit as st
import os
import pandas as pd 
from pymongo import MongoClient

from dotenv import load_dotenv
import os

load_dotenv() 

mongo = os.getenv('MONGO')
client = MongoClient(mongo)


st.set_page_config(layout="wide", page_title="Applier", initial_sidebar_state="expanded")

# No imports needed - Streamlit automatically handles pages in the pages/ folder

def jobs():
    st.switch_page("pages/Job.py")

def history():
    st.switch_page("pages/History.py")

def gmail_automator():
    st.switch_page("pages/Email Work Flow Manager.py")

st.title("The Applier")

base_dir = os.path.dirname(__file__)
file_path_sample = os.path.join(base_dir, "templates", "sample.csv")

df_sample = pd.read_csv(file_path_sample)

db = client['Email']
main_db = db['Sample_csv']

#main_db.insert_many(df_sample.to_dict(orient="records"))

left_col, right_col = st.columns(2)
with left_col:
    st.title("Welcome!👋👋")
    st.subheader("Applier Insights")
    st.progress(value=0)
    st.divider()