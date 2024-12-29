kendaraan = ['honda','motor zx',150,'hitam', 5]
print("kendaraan saya")
print(kendaraan)
print("=========")

kendaraan.extend([350000000, "kopling"])
print(kendaraan)

#tambahkan setelah jenis kendaraan value [merk kendaraan].
kendaraan.insert(5, 'honda')
print(kendaraan)

#No 2
print('ini adalah program sederhana untuk menghitung luas bangun datar')
print('pilih menu angka 1-5 : n\1. persegi\n2. lingkaran\n3. segitiga.')
pilihmenu = int(input("silahkan pilih menu dengan mengetikan angka 1-3 : "))

match pilihmenu:
    case 1:
        print("ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("silahkan masukan nilai yang mau dihitung"))
        hitung = sisi*sisi 
        print(f"luas persegi adalah : 16 {hitung}")
    
    case 2:
        print("ini adalah menu untuk menghitung luas lingkaran")
        r = int(input("masukan nilai yang ingin di hitung"))
        phi = 3.14
        luas = phi*r*r
        print (int(luas))
    case 3:
        print("ini adalah menu untuk menghitung luas segitiga")
        alas= int(input("masukan alas"))
        tinggi= int(input("masukan tinggi"))

        luas_segitiga= int(1/2*alas*tinggi)
        print(f'luas segitiga = 1/2 *', alas, '*', tinggi, '=', luas_segitiga)
    case _:
        print("pilihan tidak valid,silahkan pilih antar 1-3")