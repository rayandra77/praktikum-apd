import os

username_benar = "rayandra"
password_benar = "036"
percobaan = 0
batas = 5

while percobaan < batas:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========================================")
    print(" LOGIN PROGRAM MENGHITUNG LUAS SEGITIGA")
    print("========================================")
    user = input("Masukkan Username : ")
    password = input("Masukkan Password : ")

    if user == username_benar and password == password_benar:
        print("\nLogin berhasil! Selamat datang,", user)
        input("\nTekan ENTER untuk lanjut ke menu...")
        break
    else:
        percobaan += 1
        print(f"\nUsername atau password salah! Percobaan ke-{percobaan}")
        input("\nTekan ENTER untuk coba lagi...")

else:
    print("\nTerlalu banyak percobaan gagal. Program dihentikan.")
    exit()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========================================")
    print("    PROGRAM MENGHITUNG LUAS SEGITIGA")
    print("========================================")
    print("1. Hitung luas segitiga")
    print("2. Keluar program")
    print("========================================")
    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========================================")
        print("          HITUNG LUAS SEGITIGA")
        print("========================================")

        sisiA = float(input("Masukkan panjang sisi A: "))
        sisiB = float(input("Masukkan panjang sisi B: "))
        sisiC = float(input("Masukkan panjang sisi C: "))

        print("========================================")

        # Cek validitas segitiga
        if (sisiA + sisiB > sisiC) and (sisiA + sisiC > sisiB) and (sisiB + sisiC > sisiA):
            # Segitiga Sama Sisi
            if sisiA == sisiB == sisiC:
                print("Segitiga Sama Sisi")
                luas = ((3 ** 0.5) / 4) * (sisiA ** 2)
            
            # Segitiga Sama Kaki
            elif sisiA == sisiB or sisiA == sisiC or sisiB == sisiC:
                print("Segitiga Sama Kaki")
                setengahKeliling = (sisiA + sisiB + sisiC) / 2
                luas = (setengahKeliling * 
                        (setengahKeliling - sisiA) * 
                        (setengahKeliling - sisiB) * 
                        (setengahKeliling - sisiC)) ** 0.5
            
            # Segitiga Sembarang
            else:
                print("Segitiga Sembarang")
                setengahKeliling = (sisiA + sisiB + sisiC) / 2
                luas = (setengahKeliling * 
                        (setengahKeliling - sisiA) * 
                        (setengahKeliling - sisiB) * 
                        (setengahKeliling - sisiC)) ** 0.5
            
            print("Luas segitiga =", luas)
        else:
            print("Bukan segitiga")

        print("========================================")
        input("\nTekan ENTER untuk kembali ke menu...")

    elif pilihan == "2":
        print("\nTerima kasih telah menggunakan program ini!")
        break
    else:
        print("\nPilihan tidak valid!")
        input("\nTekan ENTER untuk kembali ke menu...")
