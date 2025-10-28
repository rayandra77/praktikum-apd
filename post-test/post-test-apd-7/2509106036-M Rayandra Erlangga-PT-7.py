import os

akun = {
    "admin": {"password": "admin", "role": "admin"},
    "rayandra": {"password": "036", "role": "user"}
}

data_ikan = {
    "Cupang": {"harga": 5000, "stok": 20},
    "Koi": {"harga": 15000, "stok": 10},
    "Guppy": {"harga": 7000, "stok": 15},
    "Nemo": {"harga": 10000, "stok": 10},
    "Glowfish": {"harga": 5000, "stok": 20},
    "Arwana": {"harga": 50000, "stok": 5}
}

is_running = True


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def input_angka(pesan):
    try:
        nilai = int(input(pesan))
        return nilai
    except ValueError:
        print("Input harus berupa angka! Coba lagi.")
        return input_angka(pesan)


def tampilkan_ikan():
    print("=========== DAFTAR IKAN HIAS ==========")
    print("|No   | Nama Ikan    | Harga    | Stok|")
    print("---------------------------------------")
    for i, (nama, info) in enumerate(data_ikan.items(), start=1):
        print(f"| {i:<3} | {nama:<12} | {info['harga']:<8} | {info['stok']:<3} |")
    print("---------------------------------------")


def menu_admin():
    print("=== MENU ADMIN TOKO IKAN HIAS ===")
    print("1. Lihat Data Ikan")
    print("2. Tambah Data Ikan")
    print("3. Ubah Data Ikan")
    print("4. Hapus Data Ikan")
    print("5. Logout")


def tambah_ikan(nama, harga, stok):
    if nama in data_ikan:
        print("Ikan tersebut sudah ada!")
    else:
        data_ikan[nama] = {"harga": int(harga), "stok": int(stok)}
        print(f"Ikan {nama} berhasil ditambahkan!")


def ubah_ikan():
    tampilkan_ikan()
    index = input_angka("Nomor ikan yang ingin diubah: ")

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
        print("Nomor ikan tidak ditemukan!")


def hapus_ikan():
    tampilkan_ikan()
    index = input_angka("Nomor ikan yang ingin dihapus: ")

    if 1 <= index <= len(data_ikan):
        nama = list(data_ikan.keys())[index - 1]
        del data_ikan[nama]
        print(f"Ikan {nama} berhasil dihapus!")
    else:
        print("Nomor ikan tidak ditemukan!")


# === REGISTER & LOGIN ===
def register():
    while True:
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")
        if username in akun:
            print("Username sudah digunakan! Coba lagi.\n")
        else:
            akun[username] = {"password": password, "role": "user"}
            print("Akun berhasil dibuat!")
            break


def login():
    clear()
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in akun and akun[username]["password"] == password:
        role = akun[username]["role"]
        print(f"\nSelamat datang, {username}!")
        input("\nTekan Enter untuk melanjutkan...")

        if role == "admin":
            while True:
                clear()
                menu_admin()
                pilih = input("Pilih menu: ")

                if pilih == "1":
                    clear()
                    tampilkan_ikan()
                    input("\nTekan Enter untuk melanjutkan...")

                elif pilih == "2":
                    clear()
                    print("=== TAMBAH DATA IKAN ===")
                    nama = input("Nama ikan: ")
                    harga = input("Harga ikan: ")
                    stok = input("Stok ikan: ")
                    tambah_ikan(nama, harga, stok)
                    input("\nTekan Enter untuk melanjutkan...")

                elif pilih == "3":
                    clear()
                    ubah_ikan()
                    input("\nTekan Enter untuk melanjutkan...")

                elif pilih == "4":
                    clear()
                    hapus_ikan()
                    input("\nTekan Enter untuk melanjutkan...")

                elif pilih == "5":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("\nTekan Enter untuk melanjutkan...")

        else:
            while True:
                clear()
                print("=== MENU PENGGUNA TOKO IKAN HIAS ===")
                print("1. Lihat Daftar Ikan")
                print("2. Logout")
                pilih = input("Pilih menu: ")

                if pilih == "1":
                    clear()
                    tampilkan_ikan()
                    input("\nTekan Enter untuk melanjutkan...")
                elif pilih == "2":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("\nTekan Enter untuk melanjutkan...")
    else:
        print("Username atau password salah!")
        input("\nTekan Enter untuk mencoba lagi...")
        login()


# MAIN PROGRAM
while is_running:
    clear()
    print("=== SELAMAT DATANG DI TOKO IKAN HIAS ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    menu_awal = input("Pilih menu: ")

    if menu_awal == "1":
        login()

    elif menu_awal == "2":
        clear()
        print("=== REGISTER AKUN BARU ===")
        register()
        input("\nTekan Enter untuk melanjutkan...")

    elif menu_awal == "3":
        clear()
        print("Terima kasih telah menggunakan program ini!")
        is_running = False

    else:
        print("Pilihan tidak valid!")
        input("\nTekan Enter untuk melanjutkan...")
