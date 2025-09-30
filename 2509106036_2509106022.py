n = int(input("Masukkan jumlah mahasiswa: "))

total_nilai = 0
jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0

for i in range(1, n + 1):
    nilai = float(input(f"Masukkan nilai mahasiswa ke-{i}: "))
    total_nilai += nilai

    if nilai >= 85:
        jumlah_A += 1
    elif nilai >= 75:
        jumlah_B += 1
    elif nilai >= 55:
        jumlah_C += 1
    else:
        jumlah_D += 1


rata_rata = total_nilai / n if n > 0 else 0

print("\n Hasil Penilaian ")
print(f"Rata-rata nilai: {rata_rata:.2f}")
print(f"Jumlah mahasiswa dengan nilai A: {jumlah_A}")
print(f"Jumlah mahasiswa dengan nilai B: {jumlah_B}")
print(f"Jumlah mahasiswa dengan nilai C: {jumlah_C}")
print(f"Jumlah mahasiswa dengan nilai D: {jumlah_D}")