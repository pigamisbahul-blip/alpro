# no1 (Perulangan while, contoh 1)
# angka = 5
# while angka <= 50:
#     print("Kelipatan 5:", angka)
#     angka += 5

# no2 (Perulangan while, contoh 2)
# bilangan = 20
# while bilangan >= 2:
#     print("Bilangan genap mundur:", bilangan)
#     bilangan -= 2

# no3 (Menghitung angka ganjil dan genap dengan while)
# angka = 1
# ganjil = 0
# genap = 0
# while angka <= 20:
#     if angka % 2 == 0:
#         genap += 1
#     else:
#         ganjil += 1
#     angka += 1
# print("Jumlah angka Genap (1-20):", genap)
# print("Jumlah angka Ganjil (1-20):", ganjil)

# no4 (Kuis 15: Implementasi while dengan break)
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# no5 (Perulangan for, contoh 1)
# for i in range(5):
#     print(i)

# no6 (Perulangan for, contoh 2: eksponensial 2)
# for i in range(1, 6):
#     print(2 ** i)

# no7 (Contoh break dan continue)
# for i in range(1, 11):
#     if i == 3:
#         continue
#     if i == 8:
#         break
#     print("Angka:", i)

# no8 (Kuis 16: implementasi break)
# total = 0
# for angka in range(1, 101):
#     total += angka
#     if total > 50:
#         print(f"Total melebihi 50 saat menjumlah angka {angka}. Total: {total}")
#         break

# no9 (Kuis 17: implementasi continue)
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print("Bilangan ganjil:", i)

# no10 (Perulangan while dengan else)
# i = 1
# while i <= 5:
#     print("Nilai i:", i)
#     i += 1
# else:
#     print("Perulangan while selesai tanpa break.")

# no11 (Perulangan for dengan else)
# for i in range(1, 6):
#     print("Nilai i:", i)
# else:
#     print("Perulangan for selesai tanpa break.")

# no12 (Ekspresi logika pada Python)
# a = 10
# b = 5
# c = 0
# print("(a > b) and (b > c):", (a > b) and (b > c))
# print("(a < b) or (b > c):", (a < b) or (b > c))
# print("not (a == b):", not (a == b))

# no13 (Operasi logical vs bitwise)
# x = 5
# y = 3
# print("Logical AND (x and y):", x and y)
# print("Logical OR (x or y):", x or y)
# print("Bitwise AND (x & y):", x & y)
# print("Bitwise OR (x | y):", x | y)
# print("Bitwise XOR (x ^ y):", x ^ y)

# no14 (Binary shifting)
# x = 4
# geser_kiri = x << 2
# geser_kanan = x >> 1
# print(f"Nilai awal x: {x}")
# print(f"x << 2: {geser_kiri}")
# print(f"x >> 1: {geser_kanan}")

# no15 (Kuis 18: Bitwise operator dan shifting)
# x = 4
# y = 1
# a = x & y
# b = x | y
# c = ~x
# d = x ^ 5
# e = x >> 2
# f = x << 2
# print(a, b, c, d, e, f)