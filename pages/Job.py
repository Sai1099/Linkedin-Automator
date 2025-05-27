import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd
from pymongo import MongoClient
from pandasql import sqldf


st.set_page_config(page_title="Jobs",layout="wide",initial_sidebar_state="expanded",page_icon="🧑‍💻")




st.title("Welcome to the Job Portal")
st.subheader("Rephrased Example Text")
left_col,right_col = st.columns(2)





client = MongoClient('mongodb+srv://sai:sai1099@cluster0.l9c5xyp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client['Scrapper']
main_db = db['posts']

data = main_db.find({"job_title":"hiring interns"})

df = pd.DataFrame(data)


def main_data(df):
   df_exploded = df.explode('results').reset_index(drop=True)
   df_exploded   = df_exploded.rename(columns={'results':'post_with_time'})
   columns = ['post_with_time', 'timestamp', 'mode_tag', 'count', 'mode', 'url', 'job_title']
   df_final = df_exploded[columns]
   df_final.columns = ['post_with_time', 'TIMESTAMP', 'MODE_TAG', 'Count', 'MODE', 'URL', 'JOB_TITLE']
   return df_final
           
           #new_df = pd.DataFrame({'post_time':r,'TIMESTAMP': df['timestamp'],'Mode':df['mode_tag']})
new_df =main_data(df)


Query = "SELECT DISTINCT * FROM new_df WHERE MODE_TAG == 'top_match';"

Query1 = "SELECT DISTINCT * FROM new_df WHERE MODE_TAG == 'latest';"

with left_col:
  st.subheader("Latest Jobs")
  top_new_latest = sqldf(Query1)
  st.dataframe(top_new_latest)

with right_col:
   
 top_new_match = sqldf(Query)
 st.subheader("Top Match or Trending Jobs ")
 st.dataframe(top_new_match)


print("Top new latest posts")
print(top_new_latest)


print("Top new matchs posts")
print(top_new_match)


# Once data is fetched, spinner disappears and data is shown








