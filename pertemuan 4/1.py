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