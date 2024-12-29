#bilangan genap atau ganjil

bilangan = int(input("masukan angka\n="))

hasil = bilangan % 2
if hasil == 0 :
    print(f"angka {bilangan} merupakan angka genap")
elif hasil == 1:
    print(f"angka {bilangan} merupakan angka ganjil")
else:
    print("angka tidak jelas")

# nilai ujian

nilai = int(input("masukan nilai anda\n="))

if nilai >= 75 :
    print('kamu lulus')
elif nilai < 75 :
    print('kamu tidak lulus')
else:
    print ('kamu gajelas')
if nilai>= 90 :
    print ('dengan predikat A')
elif nilai >= 75 :
    print ('dengan predikat B')
elif nilai >= 65 :
    print ('dengan predikat C')
elif nilai < 65 :
    print ('dengan predikat D')
else :
    print('tidak tahu')

#cek usia dan status

usia = int(input('masukan usia anda\n='))
if usia >= 18 :
    print('kamu sudah DEWASA')
elif usia >= 13 and usia <= 17 :
    print('kamu sedang memasuki masa remaja')
elif usia < 18:
    print('kamu masih bocil')
else:
    print('kamu tidak diketahui')     

#status
status =(input("""silahkan pilih status keanggotaaan seperti dibawah ini
GOLD | SILVER | BRONZE masukan pilihan anda = """))

if status.upper() == "GOLD" or status.upper() == "SILVER":
    print("selamat kamu  mendapatkan diskon!")
else:
    print('mohon maaf kamu tidak mendapatkan diskon')

#pembelian diskon
jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))

diskon = 10* jumlah_pembelian if jumlah_pembelian > 100 else 5

total = jumlah_pembelian - diskon

print(f"Jumlah pembelian: {jumlah_pembelian}")
print(f"Diskon: {diskon}")
print(f"Total yang harus dibayar: {total}")




