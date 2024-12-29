import streamlit as st
import pandas as pd
import numpy as np

color = 'red'
font_size = '24px'

css_content = f"""
p {{
    color: {color};
    font-size: {font_size};
}}
"""

print(css_content)

# Fungsi untuk menghitung IMT
def hitung_imt(berat, tinggi):
    imt = berat / (tinggi ** 2)
    return imt

# Fungsi untuk saran hidup sehat
def saran_hidup_sehat(imt):
    if imt < 18.5:
        return "Anda termasuk kategori berat badan kurang. Disarankan untuk meningkatkan asupan kalori."
    elif 18.5 <= imt < 24.9:
        return "Anda memiliki berat badan ideal. Pertahankan pola makan sehat dan olahraga teratur."
    elif 25 <= imt < 29.9:
        return "Anda termasuk kategori berat badan berlebih. Disarankan untuk mengurangi asupan kalori dan berolahraga."
    else:
        return "Anda termasuk kategori obesitas. Disarankan untuk berkonsultasi dengan ahli gizi."

# Fungsi untuk pengatur diet mingguan
def pengatur_diet():
    diet_plan = {
        "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"],
        "Sarapan": ["Oatmeal", "Telur Rebus", "Smoothie", "Roti Gandum", "Yogurt", "Buah Segar", "Nasi Merah"],
        "Makan Siang": ["Salad Sayur", "Ayam Panggang", "Ikan Bakar", "Tahu Tempe", "Quinoa", "Sayur Kukus", "Sushi"],
        "Makan Malam": ["Sup Sayur", "Daging Sapi", "Pasta", "Nasi Goreng", "Pizza Sehat", "Sushi", "Salad Buah"]
    }
    return pd.DataFrame(diet_plan)

# Judul aplikasi
st.title("Aplikasi Kesehatan - Naufal")

# Pilihan versi
versi = st.selectbox("Pilih Versi:", ["Gratis", "Premium"])

if versi == "Gratis":
    st.header("Penghitung IMT dan Berat Badan Ideal")
    berat = st.number_input("Masukkan berat badan (kg):", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi badan (m):", min_value=0.0)

    if st.button("Hitung IMT"):
        imt = hitung_imt(berat, tinggi)
        st.write(f"IMT Anda adalah: {imt:.2f}")
        st.write(saran_hidup_sehat(imt))

elif versi == "Premium":
    st.header("Pengatur Diet Mingguan")
    diet_plan = pengatur_diet()
    st.write(diet_plan)

    st.header("Monitoring Berat Badan")
    berat_badan = st.number_input("Masukkan berat badan Anda (kg):", min_value=0.0)
    data_berat = st.session_state.get('data_berat', [])
    if st.button("Simpan Berat Badan"):
        data_berat.append(berat_badan)
        st.session_state['data_berat'] = data_berat

    if data_berat:
        st.line_chart(data_berat)

    st.header("Konsultasi Online")
    st.write("Silakan hubungi ahli gizi kami untuk konsultasi lebih lanjut.")

    st.header("Pengingat Harian")
    olahraga = st.checkbox("Set pengingat harian untuk olahraga")
    hidrasi = st.checkbox("Set pengingat harian untuk hidrasi")

    if olahraga:
        st.write("Pengingat harian untuk olahraga telah diaktifkan.")
    if hidrasi:
        st.write("Pengingat harian untuk hidrasi telah diaktifkan.")

# Menjalankan aplikasi
if __name__ == "__main__":
    
    st.run()