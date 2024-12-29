import streamlit as st

st.title("Halaman Dashboard")

def total():
    total_nabung = sum(t['Jumlah'] for t in st.session_state ['jumlah']  if t['Tipe'] == 'Menabung')

    return f"Total Nabung Anda {total_nabung}" 

st.write(total())

total_semua = st.session_state['total_semua']
total_nabung, total_penarikan, saldo = total()

st.metric("Total Menabung", f"Rp. {total_nabung}")
st.metric("Total Penarikan", f"Rp. {total_penarikan}")
st.metric("Sisa Saldo Anda", f"Rp. {saldo}")
