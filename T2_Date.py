x = int(input("masukan jumlah hari:"))

tahun = x // 365
sisa_hari = x % 365

bulan = sisa_hari // 30
hari = sisa_hari % 30

print("hasil konversi;")
print("tahun :", tahun)
print("bulan :", bulan)
print("hari :", hari)