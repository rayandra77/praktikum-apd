import os

# Data akun disimpan dalam dictionary
akun = {
    "admin": {"password": "admin", "role": "admin"},
    "rayandra": {"password": "036", "role": "user"}
}

# Data ikan disimpan dalam dictionary
data_ikan = {
    1: {"nama": "Cupang", "harga": 5000, "stok": 20},
    2: {"nama": "Koi", "harga": 15000, "stok": 10},
    3: {"nama": "Guppy", "harga": 7000, "stok": 15},
    4: {"nama": "Nemo", "harga": 10000, "stok": 10},
    5: {"nama": "Glowfish", "harga": 5000, "stok": 20},
    6: {"nama": "Arwana", "harga": 50000, "stok": 5}
}

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

        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
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
                        print("=========== DAFTAR IKAN HIAS ==========")
                        print("|No   | Nama Ikan    | Harga    | Stok|")
                        print("---------------------------------------")
                        for i, ikan in data_ikan.items():
                            print(f"| {i:<3} | {ikan['nama']:<12} | {ikan['harga']:<8} | {ikan['stok']:<3} |")
                        print("---------------------------------------")
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== TAMBAH DATA IKAN ===")
                        nama = input("Nama ikan: ")
                        harga = int(input("Harga ikan: "))
                        stok = int(input("Stok ikan: "))
                        next_id = max(data_ikan.keys()) + 1
                        data_ikan[next_id] = {"nama": nama, "harga": harga, "stok": stok}
                        print("Data ikan berhasil ditambahkan!")
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("============ UBAH DATA IKAN ===========")
                        print("|No   | Nama Ikan    | Harga    | Stok|")
                        print("---------------------------------------")
                        for i, ikan in data_ikan.items():
                            print(f"| {i:<3} | {ikan['nama']:<12} | {ikan['harga']:<8} | {ikan['stok']:<3} |")

                        print("---------------------------------------")
                        index = int(input("Nomor ikan yang ingin diubah: "))
                        if index in data_ikan:
                            nama = input("Nama baru (kosong = tidak diubah): ")
                            harga = input("Harga baru (kosong = tidak diubah): ")
                            stok = input("Stok baru (kosong = tidak diubah): ")

                            if nama != "":
                                data_ikan[index]["nama"] = nama
                            if harga != "":
                                data_ikan[index]["harga"] = int(harga)
                            if stok != "":
                                data_ikan[index]["stok"] = int(stok)

                            print("Data ikan berhasil diperbarui!")
                        else:
                            print("Nomor ikan tidak valid!")
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "4":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=========== HAPUS DATA IKAN ===========")
                        print("|No   | Nama Ikan    | Harga    | Stok|")
                        print("---------------------------------------")
                        for i, ikan in data_ikan.items():
                            print(f"| {i:<3} | {ikan['nama']:<12} | {ikan['harga']:<8} | {ikan['stok']:<3} |")

                        print("---------------------------------------")
                        index = int(input("Nomor ikan yang ingin dihapus: "))
                        if index in data_ikan:
                            del data_ikan[index]
                            print("Data ikan berhasil dihapus!")
                        else:
                            print("Nomor ikan tidak valid!")
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "5":
                        break
                    else:
                        print("Pilihan tidak valid!")
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
                        print("=========== DAFTAR IKAN HIAS ==========")
                        print("|No   | Nama Ikan    | Harga    | Stok|")
                        print("---------------------------------------")
                        for i, ikan in data_ikan.items():
                            print(f"| {i:<3} | {ikan['nama']:<12} | {ikan['harga']:<8} | {ikan['stok']:<3} |")
                        print("---------------------------------------")
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "2":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("\nTekan Enter untuk melanjutkan...")

        else:
            print("Username atau password salah!")
            input("\nTekan Enter untuk melanjutkan...")

    # REGISTER
    elif menu_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        while True:
            username = input("Masukkan username baru: ")
            password = input("Masukkan password: ")

            if username in akun:
                print("Username sudah digunakan! Silakan coba lagi.\n")
            else:
                akun[username] = {"password": password, "role": "user"}
                print("Akun berhasil dibuat!")
                break
        input("\nTekan Enter untuk melanjutkan...")

    elif menu_awal == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid!")
        input("\nTekan Enter untuk melanjutkan...")
