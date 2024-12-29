import streamlit as st

# Side bar Directory
dashbord = st.Page("./Fitur/dashboard.py", title ="dashbord")
Nabung = st.Page("./Fitur/nabung.py", title ="Nabung")
Penarikan =st.Page("./Fitur/Penarikan.py", title =" Penarikan")

pg = st.navigation(
    {
        "Menu Utama": [dashbord],
        "Transaksi": [Nabung, Penarikan],
    }
)

if 'jumlah' not in st.session_state:
    st.session_state['jumlah'] = []
# Menjalankan Navigasi#
pg.run()


