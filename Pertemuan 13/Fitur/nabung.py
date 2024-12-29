import streamlit as st

st.title("Halaman Menabung")

#Halaman Menabung
with st.form("Menabung"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    button = st.form_submit_button(label="Menabung")
    if button:
        st.session_state['jumlah'].append({
            "Tipe" : "Menabung",
            "Nama" : nama,
            "Jumlah" : jumlah
        })
        st.success("Anda Berhasil Menabung")
    else:
        st.error("Gagal")
    