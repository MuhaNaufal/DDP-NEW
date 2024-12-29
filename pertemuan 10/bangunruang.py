import streamlit as st
st.title('Bangun Ruang')
def l_persegi(sisi):
    hitung = sisi * sisi 
    print(f'luas persegi adalah {sisi} * {sisi} = {hitung}')


def l_persegipanjang(panjang, lebar):
    hitung = panjang * lebar
    print(f'luas persegi panjang adalah {panjang} * {lebar} = {hitung}')

def l_lingkaran(jari):
    hitung = 22/7 * jari * jari
    print(f'luas lingkaran adalah 22/7 * {jari} * {jari} = {hitung}')

def l_segitiga(a, t):
    
    hitung = 1/2 * a * t
    print(f'luas segitiga adalah 1/2 * {a} * {t} = {hitung}')

def l_jajargenjang(a, t):
    hitung = a * t
    print(f'luas jajargenjang adalah {a} * {t} = {hitung}')