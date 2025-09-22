data = [15, 5.5, "angga", True]

print("===== DATA SEBELUM DIUBAH =====")
print("+----------+------------------+")
print("| Data     | Tipe             |")
print("+----------+------------------+")
print("|", data[0], "      |", type(data[0]), "   |")
print("|", data[1], "     |", type(data[1]), " |")
print("|", data[2], "   |", type(data[2]), "   |")
print("|", data[3], "    |", type(data[3]), "  |")
print("+----------+------------------+")

print("Jumlah int   : 1")
print("Jumlah float : 1")

data[0] = str(data[0])
data[1] = int(data[1])
data[2] = bool(data[2])
data[3] = float(data[3])

print("\n===== DATA SESUDAH DIUBAH =====")
print("+----------+------------------+")
print("| Data     | Tipe             |")
print("+----------+------------------+")
print("|", data[0], "      |", type(data[0]), "   |")
print("|", data[1], "       |", type(data[1]), "   |")
print("|", data[2], "    |", type(data[2]), "  |")
print("|", data[3], "     |", type(data[3]), " |")
print("+----------+------------------+")

print("Jumlah int   : 1")
print("Jumlah float : 1")