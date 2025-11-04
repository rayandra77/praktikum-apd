import math
from math import sqrt
import random

pilih_acak = ["pisang", "rambutan", "manggis"]
print(random.choice(pilih_acak))
print(random.choice(pilih_acak))

acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
random.shuffle(acak_kartu)
print(acak_kartu)

from datetime import datetime
# print(datetime.now())

import inquirer
pertanyaan = [
    inquirer.List(
        "pilih",
        message="pilih menu",
        choices=["create", "read", "update", "delete", "out"]
    )
]

jawaban = inquirer.prompt(pertanyaan)
if jawaban['pilih'] == 'create':
    print("masuk menu create")
elif jawaban['pilih'] == 'read':
    print("masuk menu read")

karakter = "abcdefghijklmnopqrstuvwxyz0123456789!@#$"