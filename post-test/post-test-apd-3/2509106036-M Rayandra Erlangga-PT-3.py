sisiA = int(input("Masukkan panjang sisi A: "))
sisiB = int(input("Masukkan panjang sisi B: "))
sisiC = int(input("Masukkan panjang sisi C: "))

print("========================================")

if (sisiA + sisiB > sisiC) and (sisiA + sisiC > sisiB) and (sisiB + sisiC > sisiA):
    if sisiA == sisiB == sisiC:
        print("Segitiga Sama Sisi")
        luas = ((3 ** 0.5) / 4) * (sisiA ** 2)
    
    elif sisiA == sisiB or sisiA == sisiC or sisiB == sisiC:
        print("Segitiga Sama Kaki")
        setengahKeliling = (sisiA + sisiB + sisiC) / 2
        luas = (setengahKeliling * (setengahKeliling - sisiA) * (setengahKeliling - sisiB) * (setengahKeliling - sisiC)) ** 0.5
    
    else:
        print("Segitiga Sembarang")
        setengahKeliling = (sisiA + sisiB + sisiC) / 2
        luas = (setengahKeliling * (setengahKeliling - sisiA) * (setengahKeliling - sisiB) * (setengahKeliling - sisiC)) ** 0.5
    
    print("Luas segitiga =", luas)
else:
    print("Bukan segitiga")

print("========================================")
