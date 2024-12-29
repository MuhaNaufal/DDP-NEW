# buatlah sebuah fungsi celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius.fungsi ini harus harus mengembalikan suhu yang dikonversi ke fahrenheit

print('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit

suhu_celcius1 = 0
suhu_celcius2 = 100
# Cetak 0 celcius ke 32 Fahrenheit
suhu_fahrenheit1 = celcius_ke_fahrenheit
(suhu_celcius1)
print('suhu celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)

# cetak 100 celcius ke 212 Fahrenheit
suhu_fahrenheit2 = celcius_ke_fahrenheit
(suhu_celcius2)
print('suhu celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)
print('suhu celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)

# Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen:bilangan bulat.Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.

print()
print('## Nomer 2 ##')
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0 # membentuk bilangan ganjil atau genap
    return hitung  #mengembalikan nilai hitung

angka1 = 4 #mendefinisikan bilangan
hasil1 = genap_ganjil(angka1) #memanggil fungsi
print(f"bilangan {angka1} bernilai {hasil1}")

angka2 = 7
hasil2 =genap_ganjil(angka2) #mendifinisikan bilangan
print(f"bilangan {angka2} bernilai {hasil2}") #memanggil fungsi

# Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
# #lulus 
# #gagal

print()
print('## Nomer 3 ##')
def cek_kelulusan(nilai):
    if nilai > 60 :
        return 'lulus'
    else :
        return 'gagal'
    
nilai_kamu1 = 80 #mendefinisikan nilai
status1 = cek_kelulusan(nilai_kamu1) # memanggil fungsi dan parameter
print(f"nilai: {nilai_kamu1} , status: {status1}")

nilai_kamu2 = 60 # mendefinisikan nilai
status2 = cek_kelulusan(nilai_kamu2) #memanggil funsi dan parameter
print(f"nilai: {nilai_kamu2} , status: {status2}")

# buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumen bilangan(20) #1,3,5,7,,11,13,15,17,19

print()
print('## Nomer4 ##')
def bilangan_ganjil(number):
    for a in range(1, number, 2): #1, 3, 5.. 19
        print(a, end= " ")

bilangan_ganjil(20)