def input_matrix(baris, kolom):
    matrix = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            nilai = int(input(f"Masukkan nilai [{i}][{j}]: "))
            row.append(nilai)
        matrix.append(row)
    return matrix

def tampilkan_matrix(matrix):
    for row in matrix:
        print(row)

def penjumlahan(A, B):
    hasil = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        hasil.append(row)
    return hasil

def pengurangan(A, B):
    hasil = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        hasil.append(row)
    return hasil

def perkalian(A, B):
    hasil = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        hasil.append(row)
    return hasil

while True:
    print("\n=== MENU ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")

    pilih = input("Pilih menu: ")

    if pilih == "0":
        print("Program selesai.")
        break

    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))

    print("\nMatrix A")
    A = input_matrix(baris, kolom)

    print("\nMatrix B")
    B = input_matrix(baris, kolom)

    if pilih == "1":
        hasil = penjumlahan(A, B)
        print("\nHasil Penjumlahan:")
        tampilkan_matrix(hasil)

    elif pilih == "2":
        hasil = pengurangan(A, B)
        print("\nHasil Pengurangan:")
        tampilkan_matrix(hasil)

    elif pilih == "3":
        hasil = perkalian(A, B)
        print("\nHasil Perkalian:")
        tampilkan_matrix(hasil)

    else:
        print("Pilihan tidak valid!")