#jawaban No 1
nama = 'Muhammad Naufal Aziz'
nim = '0110124194'
kelas = 'SI02'
no_telp = '0895384312878'
alamat = 'Depok'

print('Nama saya', nama,'nim saya',nim,'kelas saya', kelas, 'no telpon saya',no_telp, 'alamat saya',alamat)

#jawaban no 2

nama = 'Muhammad Rafly Fauzan'
nim = '0110124191'
kelas = 'SI02'
no_telp = '088214688949'
alamat = 'Bekasi'

print('Nama saya', nama,'nim saya',nim,'kelas saya', kelas, 'no telpon saya',no_telp, 'alamat saya',alamat)

#jawaban No 3

berat_badan = int(input('berat badan (kg) : '))
tinggi_badan = int(input('tinggi badan (cm) : '))
 
tinggi_badan = tinggi_badan/168


nilai_bmi = berat_badan / (tinggi_badan**2)

print('nilai BMI anda :',nilai_bmi)

berat_badan = int(input('berat badan (kg) : '))
tinggi_badan = int(input('tinggi badan (cm) : '))
 
tinggi_badan = tinggi_badan/100


nilai_bmi = berat_badan / (tinggi_badan**2)

print('nilai BMI anda :',nilai_bmi)

if nilai_bmi < 18.5:
	print('Berat badan anda kurang ')
elif nilai_bmi > 18.5 and nilai_bmi < 24.9:
	print('Berat badan anda normal')
elif nilai_bmi > 25 and nilai_bmi < 29.9:
	print('Anda kelebihan berat badan')
elif nilai_bmi > 30:
	print('Anda obesitas')


#jawaban No 4
celcius = 23
fahrenheit = (celcius * 9/5) + 32

print('suhu dalam celcius:', celcius, 'c')
print('suhu dalam fahrenheit:', fahrenheit, 'f')


#jawaban No 5

print("Menghitung Luas Permukaan Tabung")

# Input Jari-jari
r = int(input("Input Jari-jari : "))
# Input Tinggi
t = int(input("Input Tinggi :"))
phi =22/7

# Hitung Luas Permukaan
luas_permukaan = 2 * 3.14 * r * (r + t)
keliling =(2*phi*r)

print("Luas Permukaan Tabung : %.2f"%luas_permukaan)
print('keliling tabung -',keliling)





