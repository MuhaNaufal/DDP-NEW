#status
status =(input("""silahkan pilih status keanggotaaan seperti dibawah ini
GOLD | SILVER | BRONZE masukan pilihan anda = """))

if status.upper() == "GOLD" or status.upper() == "SILVER":
    print("selamat kamu  mendapatkan diskon!")
else:
    print('mohon maaf kamu tidak mendapatkan diskon')
