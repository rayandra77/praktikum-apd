from colorama import init, Fore
from akun import login, register
from fungsi import clear, pause

init(autoreset=True)

def main():
    is_running = True
    while is_running:
        clear()
        print(Fore.MAGENTA + "=== SELAMAT DATANG DI TOKO IKAN HIAS ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

        menu_awal = input("Pilih menu: ")

        if menu_awal == "1":
            login()
        elif menu_awal == "2":
            register()
        elif menu_awal == "3":
            clear()
            print(Fore.GREEN + "Terima kasih telah menggunakan program ini!")
            is_running = False
        else:
            print(Fore.RED + "Pilihan tidak valid!")
            pause()
main()
