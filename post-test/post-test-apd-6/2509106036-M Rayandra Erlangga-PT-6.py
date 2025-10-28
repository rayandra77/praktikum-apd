import os

# Data akun disimpan dalam dictionary
akun = {
    "admin": {"password": "admin", "role": "admin"},
    "rayandra": {"password": "036", "role": "user"}
}

# Data ikan disimpan dalam dictionary
data_ikan = {
    "Cupang": {"harga": 5000, "stok": 20},
    "Koi": {"harga": 15000, "stok": 10},
    "Guppy": {"harga": 7000, "stok": 15},
    "Nemo": {"harga": 10000, "stok": 10},
    "Glowfish": {"harga": 5000, "stok": 20},
    "Arwana": {"harga": 50000, "stok": 5}
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
                        for i, (nama, info) in enumerate(data_ikan.items(), start=1):
                            print(f"| {i:<3} | {nama:<12} | {info['harga']:<8} | {info['stok']:<3} |")
                        print("---------------------------------------")
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== TAMBAH DATA IKAN ===")
                        nama = input("Nama ikan: ")
                        harga = int(input("Harga ikan: "))
                        stok = int(input("Stok ikan: "))
                        if nama in data_ikan:
                            print("Ikan tersebut sudah ada!")
                        else:
                            data_ikan[nama] = {"harga": int(harga), "stok": int(stok)}
                            print(f"Ikan {nama} berhasil ditambahkan!")
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("============ UBAH DATA IKAN ===========")
                        print("|No   | Nama Ikan    | Harga    | Stok|")
                        print("---------------------------------------")
                        for i, (nama, info) in enumerate(data_ikan.items(), start=1):
                            print(f"| {i:<3} | {nama:<12} | {info['harga']:<8} | {info['stok']:<3} |")

                        print("---------------------------------------")
                        index = int(input("Nomor ikan yang ingin diubah: "))
                        if 1 <= index <= len(data_ikan):
                            nama_lama = list(data_ikan.keys())[index - 1]
                            data_lama = data_ikan[nama_lama]

                            nama_baru = input("Nama baru (kosong = tidak diubah): ")
                            harga_baru = input("Harga baru (kosong = tidak diubah): ")
                            stok_baru = input("Stok baru (kosong = tidak diubah): ")

                            if nama_baru != "":
                                data_ikan[nama_baru] = data_lama
                                if nama_baru != nama_lama:
                                    del data_ikan[nama_lama]
                                nama_lama = nama_baru
                            if harga_baru != "":
                                data_ikan[nama_lama]["harga"] = int(harga_baru)
                            if stok_baru != "":
                                data_ikan[nama_lama]["stok"] = int(stok_baru)

                            print(f"Data ikan {nama_lama} berhasil diperbarui!")
                        else:
                            print("Nomor ikan tidak valid!")
                        input("\nTekan Enter untuk melanjutkan...")

                    elif pilih == "4":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=========== HAPUS DATA IKAN ===========")
                        print("|No   | Nama Ikan    | Harga    | Stok|")
                        print("---------------------------------------")
                        for i, (nama, info) in enumerate(data_ikan.items(), start=1):
                            print(f"| {i:<3} | {nama:<12} | {info['harga']:<8} | {info['stok']:<3} |")

                        print("---------------------------------------")
                        index = int(input("Nomor ikan yang ingin dihapus: "))
                        if 1 <= index <= len(data_ikan):
                            nama = list(data_ikan.keys())[index - 1]
                            del data_ikan[nama]
                            print(f"Ikan {nama} berhasil dihapus!")
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
                        for i, (nama, info) in enumerate(data_ikan.items(), start=1):
                            print(f"| {i:<3} | {nama:<12} | {info['harga']:<8} | {info['stok']:<3} |")
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
