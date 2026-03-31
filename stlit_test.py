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