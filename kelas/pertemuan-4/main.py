
# for i in range(10):
#     print(i +1)

# [1,2,3,4,,5,6,7,8,9]
# for i in range(1,11,2):
#     print(i)

# for loop untuk list
# nama = ['bakil', 'diftya', 'anugrah']
# for i in nama:
#     print(i)

# for name in range(5):
#     print("raffi")

# while loop
# jawab ="ya"
# hitung = 0

# while (jawab == 'ya'):
#     hitung += 1
#     jawab = input("ulang lagi? : ")

# print(f"total jawab ya {hitung}")

# cuaca = "hujan"

# while (cuaca == "hujan" or cuaca =="Hujan"):
#     print("jangan keluar rumah")
#     cuaca = input("Apa cuaca saat ini : ")

# print("pergi keluar rumah")


# angka = 10

# while (angka > 1):
#     print(angka)
#     angka -= 2

# for i in range(1,5):
#     for j in range(1,5):
#         print(f"{i} x {j} = {i*j}")
#     print()


# break
# angka = [2, 5, 8, 12, 15, 7, 20]

# print("mencari angka yang lebih dari besar 10....")

# for i in angka:
#     print(f"memeriksa angka {i}")
#     if i > 10:
#         print(f"{i} lebih besar dari 10")
#         break

# print("program selesai")

# for i in range (1,11):
#     if i % 2 == 0:
#         continue
#     print(f'angka ditemukan yaitu : {i}')

# print("program selesai")

# kuadrat = [i**2 for i in range(1,6)]
# print(kuadrat)

# for i in range(1,6):
#     print(i**2)

# angka_genap = [x for x in range(1,11) if x%2==0]
# print(angka_genap)

# for x in range(1,11):
#     if x%2==0:
#         print(x)

# angka_ganjil = [x for x in range(1,11) if x%2!=0]
# print(angka_ganjil)

# for x in range(1,11):
#     if x%2!=0:
#         print(x)

for i in range(1,6):
    print("*" * i)

for i in range(1,6):
    print("*" * (6-i))

for i in range(1,6):
    print(" " * (6-i) + (2*i-1)* "*" )