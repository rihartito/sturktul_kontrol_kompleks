''' 
Rihar del tito-71200648
Universitas Kristen Duta wacana
struktur kontrol kompleks
soal buat sendiri

budi sedang mengadakan diskon besar-besaran ketika pelanggannya belanja sebesar 1500000-3000000 mendapatkan diskon 15%,
ketika lebih dari 3000000-5000000 mendapatkan diskon 20%,ketika kurang 1500000-500000 mendapatkan diskon 8% syarat ini berlaku jika 
pelanggan mempunyai kartu member.
tapi budi juga memberikan diskon kepada pelanggan yang tanpa kartu member mulai belanja sebesar dari 900000-1000000 mendapatkan 
diskon 5%
buatlah program tersebut

harga = harga belanja pelanggan
kartu = kartu member pelanggan

#input:harga = harga belanja ; kartu = kartu member yes/no

#proses:
membuat percabangan kartu yes dan harga minimum
membuat percbangan kartu no dan harga minimun 
membuat percabangan yang tidak mendapatkan diskon

#output:
menghasilkan diskon dan harga sesuai yang diinginkan sesuai soal


'''

harga = int(input("masukkan harga :"))
kartu = input("yes/no :")

kartu_M = kartu.lower()
if harga >= 500000 and kartu_M == "yes":
    if harga >= 1500000 and harga <= 3000000:
        diskon = harga * 15/100
        print("diskon yang anda dapat adalah",diskon,"harga sekarang adalah",harga-diskon)
    elif harga > 3000000 and harga <= 5000000:
        diskon = harga * 20/100
        print("anda mendapatkan diskon sebesar",diskon,"harga yang harus dibayar sekarang",harga-diskon)
    elif harga >= 500000 and 1500000 :
        diskon = harga * 8/100
        print("anda mendapatkan diskon sebesar",diskon,"harga yang harus dibayar sekarang",harga-diskon)
    else :
        print("maaf anda tidak mendapatkan diskon")
        print("harga yang harus dibayar adalah",harga)
else:
    if harga >= 900000 and harga <= 1000000 and kartu_M == "no":
        diskon = harga * 5/100
        print("anda mendapatkan diskon sebesar",diskon,"harga yang harus dibayar sekarang",harga-diskon)



