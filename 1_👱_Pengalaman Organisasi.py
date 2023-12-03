import streamlit as st

st.set_page_config(
    page_title="pengalaman organisasi",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("Pengalaman Organisasi")
st.write("beberapa pengalaman organisasi saya; ")

st.container()
col1, = st.columns(1)
with col1:
    st.subheader("Forum Permusyawaratan Santri")
   

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
   
    st.image("FPS.png", width= 190)

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
    st.write("*KOMISI B*")

st.container()
col1, = st.columns(2)
with col1:
    st.subheader("Ikatan Santri Intra Madrasah")
   

st.container()
st.write("---")
col1, = st.columns(2)
with col1:
   
    st.image("isim.png", width= 190)

st.container()
st.write("---")
col1, = st.columns(2)
with col1:
    st.write("*Departement Pendidikan dan Departemen Lingkungan Hidup*")

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
   
    st.image("FPS.png", width= 190)

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
    st.write("*KOMISI B*")

st.container()
col1, = st.columns(3)
with col1:
    st.subheader("Panitia Akbar")
   

st.container()
st.write("---")
col1, = st.columns(3)
with col1:
   
    st.image("PAS.png", width= 190)

st.container()
st.write("---")
col1, = st.columns(2)
with col1:
    st.write("*wakil ketua dan sie. acara*")



   