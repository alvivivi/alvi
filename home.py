import streamlit as st

st.set_page_config(
    page_title="Portfolio | AIDA",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")



col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("me.jpg", width= 100)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : Aida Alvi Fitriyatin")
   st.caption("NIM : 0402201099")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 14 Desember 2001 
            - Alamat               : Pejagan Tanjung Brebes
            - Hobi                 : Membaca novel
            - Cita-cita            : Pengusaha Sukses
            - Hal yang disukai     : nonton TV
            - Status               : Mahasiswi
            """
        )
st.header("*Call Me If You Want*")


st.link_button("Go to contact", "http://localhost:8501/contact")
