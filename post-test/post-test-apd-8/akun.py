from colorama import Fore
from menu import menu_admin, menu_user
from fungsi import clear, pause

akun = {
    "admin": {"password": "admin", "role": "admin"},
    "rayandra": {"password": "036", "role": "user"}
}


def login():
    clear()
    print(Fore.CYAN + "=== LOGIN TOKO IKAN HIAS ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in akun and akun[username]["password"] == password:
        print(Fore.GREEN + f"\nSelamat datang, {username}!")
        pause()
        if akun[username]["role"] == "admin":
            menu_admin()
        else:
            menu_user()
    else:
        print(Fore.RED + "Username atau password salah!")
        pause()
        login()

def register():
    clear()
    print(Fore.CYAN + "=== REGISTER AKUN BARU ===")
    while True:
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")
        if username in akun:
            print(Fore.RED + "Username sudah digunakan!")
        else:
            akun[username] = {"password": password, "role": "user"}
            print(Fore.GREEN + "Akun berhasil dibuat!")
            break
    pause()