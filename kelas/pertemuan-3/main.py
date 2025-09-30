# angka = 6

# if(angka>5):
#         print("angka lebih besar dari 5")

#contoh pertama

# cuaca = "hujan"

# if cuaca == "hujan":
#     print("Dirumah aja")
# else :
#     print("nongkrong")

#contoh 2

# nilai = 70

# if nilai >= 70:
#     print("lulus")
# else:
#     print("tidak lulus")

# status = "lulus" if nilai >= 70 else "tidak lulus"
# print(status)

# contoh

# cuaca = 'mendung'

# if cuaca == "hujan":
#     print("dirumah aja")

# elif cuaca == "mendung":
#     print("makan mie")

# else :
#     print("nongkrong")

# # contoh 4

# usia = int(input("masukkan usia anda :"))

# if usia <=0:
#     print("usia tidak valid")
# elif usia <= 13:
#     print("anak-anak")
# elif usia <= 18:
#     print("remaja")
# elif usia <= 40:
#     print("dewasa")
# else :
#     print("tua")

# contoh 5

# nilai = int(input("masukkan nilai anda :"))

# if nilai >= 90:
#     print("A")
# elif nilai >= 70:
#     print("B")
# elif nilai >= 60:
#     print("C")
# else :
#     print("D")

# neseted if

# a = 4
# b = 5
# c = 6

# if a<b :
#     if a<c:
#         print("a paling kecil")
#     else :
#         print("c lebih kecil dari a")
# elif a<c:
#     print("c lebih besar")
# else :
#     print("a paling besar")

# studi kasus 1

# tinggi_badan =float(input("masukkan tinggi badan :"))

# status = "diizinkan masuk wahana" if tinggi_badan>=145 else "tidak bisa naik wahana"
# print(status)

# studi kasus 2

# a = 100.000
# b =50.000

# total_belanja = int(input("masukkan total belanja anda :"))

# if total_belanja >=100000:
#     print("mendapat diskon 20%")
#     bayar = total_belanja * 0.2
#     total = total_belanja - bayar
#     print(total)
# elif total_belanja >=50000:
#     print("mendapat diskon 10%")
#     bayar = total_belanja * 0.2
#     total = total_belanja - bayar
#     print(total)
# else:
#     print("pembeli tidak mendapat diskon")

nilai = int(input("masukkan nilai :"))
kelas =input("masukkan kelas :")

if nilai>= 80 and (kelas =="A" or kelas=="a"):
    print("IPK 4")
elif nilai >= 80 and kelas =="B":
    print("IPK 3")
else :
    print("IPK 2")