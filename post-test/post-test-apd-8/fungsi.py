import os
from colorama import Fore

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_angka(pesan):
    try:
        return int(input(pesan))
    except ValueError:
        print(Fore.RED + "Input harus berupa angka!")
        return input_angka(pesan)

def pause():
    input("\nTekan Enter untuk melanjutkan...")
