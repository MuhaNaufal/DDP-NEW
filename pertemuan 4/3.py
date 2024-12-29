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
