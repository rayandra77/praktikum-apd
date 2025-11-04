from colorama import Fore
from fungsi import clear, input_angka, pause
from data import tampilkan_ikan, tambah_ikan, ubah_ikan, hapus_ikan

def menu_admin():
    while True:
        clear()
        print(Fore.YELLOW + "=== MENU ADMIN TOKO IKAN ===")
        print("1. Lihat Data Ikan")
        print("2. Tambah Data Ikan")
        print("3. Ubah Data Ikan")
        print("4. Hapus Data Ikan")
        print("5. Logout")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            clear()
            tampilkan_ikan()
            pause()
        elif pilih == "2":
            clear()
            nama = input("Nama ikan: ")
            harga = input("Harga ikan: ")
            stok = input("Stok ikan: ")
            tambah_ikan(nama, harga, stok)
            pause()
        elif pilih == "3":
            clear()
            ubah_ikan(input_angka)
            pause()
        elif pilih == "4":
            clear()
            hapus_ikan(input_angka)
            pause()
        elif pilih == "5":
            break
        else:
            print(Fore.RED + "Pilihan tidak valid!")
            pause()

def menu_user():
    while True:
        clear()
        print(Fore.CYAN + "=== MENU PENGGUNA TOKO IKAN HIAS ===")
        print("1. Lihat Daftar Ikan")
        print("2. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            clear()
            tampilkan_ikan()
            pause()
        elif pilih == "2":
            break
        else:
            print(Fore.RED + "Pilihan tidak valid!")
            pause()
