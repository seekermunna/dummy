import streamlit as st


st.set_page_config(
    page_title="streamlit app demo",
    page_icon="🚀",
    layout="centered"
)

st.title(" Ultimate Data Science ")

st.subheader("Level 1")

st.write("This is for the checking of streamlit as per practice")

tab1, tab2, tab3 = st.tabs(["Home","Dashboard","Settings"])

with tab1:
    st.write("Welcome to Home Tab!😊")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Left Section of Home !")
        st.button("Click on LEFT Button",type="primary")

    with col2:
        st.write("Center section of the Home !")
        st.button("Click on CENTER Button",type="secondary")

    with col3:
        st.write("Right section of the Home !")
        st.button("Click on RIGHT Button",type="tertiary")

with tab2:
    st.write("Welcome to Dashboard Tab !")

with tab3:
    st.write("Welcome to Settings Tab !")

st.divider()

st.subheader("Level 2")

with st.container(width=150,height=100,border=True):
    for i in range(100):
        st.write(f"Iterator{i}")

st.divider()

st.subheader("Level 3")

# input Wedgets

if st.button('Click Button'):
    st.write("Hello There !")

st.link_button("Streamlit button widgets",url="https://docs.streamlit.io/develop/api-reference/widgets")

a = 0
name = st.text_input("Enter Name")
a+= 1
print(a)
print(name)
st.write(f" Entered Your Name is {name}")

count = 0

if st.button("Click button to count"):
    count += 1
    st.write(f"No of times clicked button is {count}")

# Text input and text area

U_name = st.text_input("Enter your name ! ")
u_pwd = st.text_input("Enter your pswd",type="password")
bio = st.text_area(" Tell about your self !",height=100)

st.divider()

st.subheader("Level 4")


import datetime
today = datetime.date.today()

pick_date = st.date_input("Todays Date ",today)
st.write(f"Date is {pick_date}")

st.divider()

from io import StringIO

uploaded_file = st.file_uploader("Upload a file",type=["pdf","csv"])

if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("ISO-8859-1"))
    string_data = stringio.read()

    st.write(f"{type(stringio)}")
    st.write(f"{type(string_data)}")

    st.write("Context : ")
    #st.code( string_data ,language="Text")
    st.success("File Uploaded Successfully !")

    st.warning("FILE is not uploaded successfully :(")
    st.error("Error !")
    st.info("Here the some information !")

st.divider()

if count not in st.session_state:
    st.session_state.count = 0
if st.button("Increment"):
    st.session_state.count += 1

st.write(st.session_state.count)

st.divider()

st.title("Title")
st.header("Header")
st.subheader("Sub-Header")

st.markdown("This is **Bold** context!")

st.divider()

st.subheader("Level 5")

import pandas as pd

df = pd.DataFrame({"a": ["1"], "b": ["5"], "c": ["10"], "d": ["15"]})
st.write("Data Visualization")
st.dataframe(df)
st.bar_chart(df)

st.image(r"C:\Users\HP\OneDrive\Pictures\muntains_lake.png",caption="My Image",width=800)

# loading bar

import time
bar = st.progress(0)
for perc in range(100):
    time.sleep(0.1)
    bar.progress(perc+1)


# download button

text = "1,2,3,4,5"

st.download_button(label="download_text",data=text,file_name="text.txt",mime="text/plain")