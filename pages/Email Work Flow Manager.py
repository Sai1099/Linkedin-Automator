import streamlit as st
import pandas as pd
from Home import main_db,db


st.set_page_config(page_title="Email WorkFlow Manager",layout="wide",initial_sidebar_state="expanded", page_icon="📧")

st.title("Email Work Flow Manager")

if "page" not in st.session_state:
   st.session_state = "upload"
sample_filee = main_db.find_one({"email": "somexyz@gamil.com"})
template_raw = sample_filee.get('template', '')
template_cleaned = template_raw.strip("[]")
if sample_filee:
        df_sample = pd.DataFrame([{
            's.no': sample_filee.get('s.no', ''),
            'email': sample_filee.get('email', ''),
            'template': template_raw
        }])


if st.session_state == "upload":
 left_col,right_col = st.columns(2) 
 with left_col:
  uploaded_file = st.file_uploader("Upload the CSV File:",type=['CSV'])
  if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    if list(df_sample.columns) == list(df.columns) and all(df_sample.dtypes == df.dtypes):
      st.write("Here is the Preview data of your File:")
      st.dataframe(df.head(5))
        
    else:
        st.error("Schema mismatch! Please upload a file with the correct format.")

  resume_file = st.file_uploader("Upload Your Resume File:",type=['PDF'])

  Gmail_id = st.text_input("Enter Your Gmail:")
  App_Password = st.text_input("Enter your Google App Password")
  if resume_file and uploaded_file and Gmail_id and App_Password:
            if st.button("Start Processing"):
                # Save to session state if needed
                st.session_state.resume_file = resume_file
                st.session_state.uploaded_file = uploaded_file
                st.session_state.email = Gmail_id
                st.session_state.app_password = App_Password
                st.session_state.page = "process"
                st.rerun()
 with right_col:
  st.subheader("This is the sample Header of CSV")
  st.dataframe(df_sample,hide_index=True,use_container_width=True) 
  st.info("To process the gmails requires App Password.\n" \
  "To Know More About the App Password Kindly click the Below Button.")
  st.link_button(url = 'https://support.google.com/accounts/answer/185833?hl=en',label="App Password Docs")
  st.divider()

elif st.session_state == "process":
    st.title("📤 Processing Started")
    st.success("Processing email workflow...")

    # Access session state values
    st.write(f"**Email:** {st.session_state.email}")
    st.write(f"**Resume File:** {st.session_state.resume_file.name}")
    st.write(f"**CSV File:** {st.session_state.uploaded_file.name}")

    # Add processing logic here
    # You can use st.progress or st.spinner to simulate steps

    if st.button("⬅ Back to Upload Page"):
        st.session_state.page = "upload"
        st.rerun()








