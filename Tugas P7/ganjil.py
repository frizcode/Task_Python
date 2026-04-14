while True:
    print("\nMenu:")
    print("1. A pangkat B")
    print("2. Hitung deret")
    print("0. Keluar")

    pilihan = int(input("Masukkan: "))

    if pilihan == 1:
        a = int(input("Masukkan suatu bilangan bulat: "))
        b = int(input("Masukkan pangkat yang diinginkan: "))

        hasil = 1
        for i in range(1, b + 1):
            hasil *= a
            print(f"hasil {a} pangkat {i} adalah {hasil}")

    elif pilihan == 2:
        N = int(input("Masukkan jumlah N: "))

        a, b = 1, 2   # pembilang awal
        c, d = 3, 5   # penyebut awal
        total = 0
        tanda = 1

        for i in range(N):
            if i == 0:
                total += 1
            elif i == 1:
                total -= 2/3
            else:
                total += tanda * (b / c)

                # pola fibonacci
                a, b = b, a + b
                c, d = d, c + d

                tanda *= -1

        print("Hasil:", total)

    elif pilihan == 0:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")