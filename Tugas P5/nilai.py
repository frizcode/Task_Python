# Data mahasiswa
mahasiswa = [
    ["10121001", "Asep"],
    ["10121002", "Budi"],
    ["10121003", "Cecep"]
]

# Data nilai
nilai = [
    ["10121001", 50, 70, 40, 80],
    ["10121002", 78, 78, 80, 65],
    ["10121003", 57, 88, 67, 69]
]

rata_tertinggi = 0
nama_terpintar = ""

for n in nilai:
    nim = n[0]
    nilai_mk = n[1:]
    rata = sum(nilai_mk) / len(nilai_mk)

    for m in mahasiswa:
        if m[0] == nim:
            nama = m[1]

    if rata > rata_tertinggi:
        rata_tertinggi = rata
        nama_terpintar = nama

jumlah_mk = len(nilai[0]) - 1
rata_mk = []

for i in range(jumlah_mk):
    total = 0
    for n in nilai:
        total += n[i + 1]
    rata = total / len(nilai)
    rata_mk.append(rata)

nilai_terkecil = min(rata_mk)
index_mk = rata_mk.index(nilai_terkecil)

print("Mahasiswa Terpintar :", nama_terpintar, "(Nilai :", round(rata_tertinggi, 2), ")")
print("Mata Kuliah Nilai Terkecil : MK" + str(index_mk + 1), "(Nilai :", round(nilai_terkecil, 2), ")")