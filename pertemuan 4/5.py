#pembelian diskon
jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))

diskon = 10* jumlah_pembelian if jumlah_pembelian > 100 else 5

total = jumlah_pembelian - diskon

print(f"Jumlah pembelian: {jumlah_pembelian}")
print(f"Diskon: {diskon}")
print(f"Total yang harus dibayar: {total}")

