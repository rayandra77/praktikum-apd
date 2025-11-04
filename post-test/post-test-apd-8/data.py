from prettytable import PrettyTable
from colorama import Fore

data_ikan = {
    "Cupang": {"harga": 5000, "stok": 20},
    "Koi": {"harga": 15000, "stok": 10},
    "Guppy": {"harga": 7000, "stok": 15},
    "Nemo": {"harga": 10000, "stok": 10},
    "Glowfish": {"harga": 5000, "stok": 20},
    "Arwana": {"harga": 50000, "stok": 5}
}

def tampilkan_ikan():
    table = PrettyTable()
    table.field_names = ["No", "Nama Ikan", "Harga", "Stok"]
    for i, (nama, info) in enumerate(data_ikan.items(), start=1):
        table.add_row([i, nama, info['harga'], info['stok']])
    print(Fore.CYAN + "======== DAFTAR IKAN HIAS =======")
    print(table)

def tambah_ikan(nama, harga, stok):
    if nama in data_ikan:
        print(Fore.RED + "Ikan sudah ada!")
    else:
        data_ikan[nama] = {"harga": int(harga), "stok": int(stok)}
        print(Fore.GREEN + f"Ikan {nama} berhasil ditambahkan!")

def ubah_ikan(input_angka):
    tampilkan_ikan()
    index = input_angka("Nomor ikan yang ingin diubah: ")

    if 1 <= index <= len(data_ikan):
        nama_lama = list(data_ikan.keys())[index - 1]
        data_lama = data_ikan[nama_lama]

        nama_baru = input("Nama baru (kosong = tidak diubah): ")
        harga_baru = input("Harga baru (kosong = tidak diubah): ")
        stok_baru = input("Stok baru (kosong = tidak diubah): ")

        if nama_baru:
            data_ikan[nama_baru] = data_lama
            if nama_baru != nama_lama:
                del data_ikan[nama_lama]
            nama_lama = nama_baru
        if harga_baru:
            data_ikan[nama_lama]["harga"] = int(harga_baru)
        if stok_baru:
            data_ikan[nama_lama]["stok"] = int(stok_baru)

        print(Fore.GREEN + f"Data ikan {nama_lama} berhasil diperbarui!")
    else:
        print(Fore.RED + "Nomor ikan tidak ditemukan!")

def hapus_ikan(input_angka):
    tampilkan_ikan()
    index = input_angka("Nomor ikan yang ingin dihapus: ")

    if 1 <= index <= len(data_ikan):
        nama = list(data_ikan.keys())[index - 1]
        del data_ikan[nama]
        print(Fore.GREEN + f"Ikan {nama} berhasil dihapus!")
    else:
        print(Fore.RED + "Nomor ikan tidak ditemukan!")
