import os

akun = [["admin", "admin", "admin"],
        ["rayandra", "036", "user"]
]

data_ikan = [
    ["Cupang", 5000, 20],
    ["Koi", 15000, 10],
    ["Guppy", 7000, 15],
    ["Nemo", 10000, 10],
    ["Glowfish", 5000, 20],
    ["Arwana", 50000, 5]
]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SELAMAT DATANG DI TOKO IKAN HIAS ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu: ")

    # LOGIN
    if menu_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")

        role = None
        for user in akun:
            if user[0] == username and user[1] == password:
                role = user[2]
                break

        if role is None:
            print("Username atau password salah!")
            input("\nTekan Enter untuk melanjutkan...")
        else:
            print("\nSelamat datang,", username + "!")
            input("\nTekan Enter untuk melanjutkan...")

            # MENU ADMIN
            if role == "admin":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== MENU ADMIN TOKO IKAN HIAS ===")
                    print("1. Lihat Data Ikan")
                    print("2. Tambah Data Ikan")
                    print("3. Ubah Data Ikan")
                    print("4. Hapus Data Ikan")
                    print("5. Logout")
                    pilih = input("Pilih menu: ")

                    if pilih == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR IKAN HIAS ===")
                        print("No  Nama Ikan     Harga     Stok")
                        for i, ikan in enumerate(data_ikan):
                            print(str(i+1) + ". " + ikan[0] + " - Harga: " + str(ikan[1]) + " - Stok: " + str(ikan[2]))
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== TAMBAH DATA IKAN ===")
                        nama = input("Nama ikan: ")
                        harga = int(input("Harga ikan: "))
                        stok = int(input("Stok ikan: "))
                        data_ikan.append([nama, harga, stok])
                        print("Data ikan berhasil ditambahkan!")
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== UBAH DATA IKAN ===")
                        for i, ikan in enumerate(data_ikan):
                            print(str(i+1) + ". " + ikan[0] + " (Harga: " + str(ikan[1]) + ", Stok: " + str(ikan[2]) + ")")

                        index = int(input("Nomor ikan yang ingin diubah: ")) - 1
                        if 0 <= index < len(data_ikan):
                            nama = input("Nama baru (kosong = tidak diubah): ")
                            harga = input("Harga baru (kosong = tidak diubah): ")
                            stok = input("Stok baru (kosong = tidak diubah): ")

                            if nama != "":
                                data_ikan[index][0] = nama
                            if harga != "":
                                data_ikan[index][1] = int(harga)
                            if stok != "":
                                data_ikan[index][2] = int(stok)

                            print("Data ikan berhasil diperbarui!")
                        else:
                            print("Pilihan tidak valid!!")
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "4":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== HAPUS DATA IKAN ===")
                        for i, ikan in enumerate(data_ikan):
                            print(str(i+1) + ". " + ikan[0] + " (Harga: " + str(ikan[1]) + ", Stok: " + str(ikan[2]) + ")")

                        index = int(input("Nomor ikan yang ingin dihapus: ")) - 1
                        if 0 <= index < len(data_ikan):
                            data_ikan.pop(index)
                            print("Data ikan berhasil dihapus!")
                        else:
                            print("Pilihan tidak valid!!")
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "5":
                        break
                    else:
                        print("Pilihan tidak valid!!")
                        input("\nTekan Enter untuk melanjutkan...")

            # MENU USER
            elif role == "user":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== MENU PENGGUNA TOKO IKAN HIAS ===")
                    print("1. Lihat Daftar Ikan")
                    print("2. Logout")
                    pilih = input("Pilih menu: ")

                    if pilih == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR IKAN HIAS ===")
                        print("No  Nama Ikan     Harga     Stok")
                        for i, ikan in enumerate(data_ikan):
                            print(str(i+1) + ". " + ikan[0] + " - Harga: " + str(ikan[1]) + " - Stok: " + str(ikan[2]))
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "2":
                        break
                    else:
                        print("Pilihan tidak valid!!")
                        input("\nTekan Enter untuk melanjutkan...")

    # REGISTER
    elif menu_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")
        sudah_ada = False

        for user in akun:
                if user[0] == username:
                    sudah_ada = True
                    break

        if sudah_ada:
            print("Username sudah digunakan!, Gunakan username lain.")
        else:
            akun.append([username, password, "user"])
            print("Akun berhasil dibuat!")

        input("\nTekan Enter untuk melanjutkan...")

    elif menu_awal == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid!")
        input("\nTekan Enter untuk melanjutkan...")
