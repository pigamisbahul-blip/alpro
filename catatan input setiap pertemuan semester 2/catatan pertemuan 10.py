# Hasil Ekstraksi Kode Praktikum
# Topik: List in advance applications in Python
# Nama: Piga Misbahul Hapidhiin
# Kelas: 2 INF A

# no1. List Comprehensions
# angka = [1, 2, 3, 4, 5]
# # Buat list baru berisi kuadrat dari setiap elemen
# kuadrat = [x**2 for x in angka]
# print("Kuadrat:", kuadrat)
# # Buat list hanya angka genap
# genap = [x for x in angka if x % 2 == 0]
# print("Genap:", genap)

# no2. Array 2 Dimensi
# # Array 2 Dimensi (list di dalam list)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # Tampilkan isi matrix baris per baris
# for baris in matrix:
#     print(baris)
# # Akses elemen tertentu (baris ke-1, kolom ke-2)
# print("Elemen [1][2]:", matrix[1][2])

# no3. List Multidimensi
# # List Multidimensi (3 dimensi)
# data = [
#     [
#         [1, 2], [3, 4]
#     ],
#     [
#         [5, 6], [7, 8]
#     ]
# ]
# # Tampilkan semua elemen
# for i in data:
#     for j in i:
#         for k in j:
#             print(k, end=" ")
#         print()
# print("---")
# # Akses elemen tertentu
# print("Elemen [0][1][1]:", data[0][1][1])

# no4. Fungsi Berparameter
# def hitung_luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     return luas
# 
# def sapa(nama, umur):
#     print(f"Halo, nama saya {nama} dan saya berumur {umur} tahun.")
# 
# # Memanggil fungsi dengan argumen
# hasil = hitung_luas_persegi_panjang(5, 3)
# print("Luas:", hasil)
# sapa("Alfa", 21)
# sapa("fufufafa", 28)

# no5 (Kuis 1)
# # Kuis 1: List comprehension bilangan 1-10, ambil genap, hasil dikalikan 3
# hasil = [x * 3 for x in range(1, 11) if x % 2 == 0]
# print("Hasil:", hasil)

# no6 (Kuis 2)
# # Kuis 2: Array 2 dimensi 3x3 berisi angka
# array = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # Tampilkan seluruh isi array
# for baris in array:
#     print(baris)

# no7 (Kuis 3)
# # Kuis 3: Meratakan list multidimensi (flattening)
# data = [[2, 4], [6, 8], [10, 12]]
# flatten = [angka for sublist in data for angka in sublist]
# print("Hasil flatten:", flatten)

# no8 (Kuis 4)
# # Kuis 4: Fungsi menghitung luas persegi panjang
# def hitung_luas(panjang, lebar):
#     luas = panjang * lebar
#     return luas
# 
# # Panggil fungsi dengan panjang = 8 dan lebar = 5
# hasil = hitung_luas(8, 5)
# print("Luas persegi panjang:", hasil)