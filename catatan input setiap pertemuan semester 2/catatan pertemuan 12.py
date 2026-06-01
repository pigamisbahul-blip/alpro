# Hasil Ekstraksi Kode Praktikum
# Topik: Scope dan Multi-parameter function in python
# Nama: PIGA MISBAHUL HAPIDHIIN
# Kelas: 2-INF-A

# no1. Variable local: variable yang berada di dalam fungsi
# def penjumlahan(x):
#     bilangan = 7
#     return x + 7
# 
# print(penjumlahan(4))
# print(bilangan)

# no2. Variable di luar fungsi -1
# bilangan = 2
# def perkalian_bilangan(x):
#     return x * bilangan
# 
# print(perkalian_bilangan(7))

# no3. Variable di luar fungsi -2
# def perkalian_bilangan(x):
#     bilangan = 7
#     return x * bilangan
# 
# bilangan = 3
# print(perkalian_bilangan(7))

# no4. Variable global dengan keyword 'global'
# bilangan = 3
# print(bilangan)
# 
# def return_bilangan():
#     global bilangan
#     bilangan = 5
#     return bilangan
# 
# print(return_bilangan())
# print(bilangan)

# no5. Kuis IMT
# def hitung_imt(berat, tinggi):
#     # Rumus IMT = Berat (kg) / (Tinggi (m) x Tinggi (m))
#     imt = berat / (tinggi * tinggi)
#     return imt
# 
# jenis_kelamin = input("pilih jenis kelamin (L/P): ")
# berat = float(input("Masukkan berat badan anda (kg): "))
# tinggi = float(input("Masukkan tinggi badan anda (m): "))
# index_massa_tubuh = hitung_imt(berat, tinggi)
# 
# if jenis_kelamin == "P" or jenis_kelamin == "p":
#     if index_massa_tubuh < 18.5:
#         kategori_imt = "Kurus"
#     elif 18.5 <= index_massa_tubuh <= 25.8:
#         kategori_imt = "Normal"
#     elif 25.0 < index_massa_tubuh <= 27.0:
#         kategori_imt = "Gemuk"
#     else:
#         kategori_imt = "Obesitas"
#     print("Index massa tubuh anda tergolong", kategori_imt, ", dengan nilai IMT =", round(index_massa_tubuh, 2))
# elif jenis_kelamin == "L" or jenis_kelamin == "l":
#     if index_massa_tubuh < 18.5:
#         kategori_imt = "Kurus"
#     elif 18.5 <= index_massa_tubuh <= 25.0:
#         kategori_imt = "Normal"
#     elif 25.0 < index_massa_tubuh <= 27.0:
#         kategori_imt = "Gemuk"
#     else:
#         kategori_imt = "Obesitas"
#     print("Index massa tubuh anda tergolong", kategori_imt, ", dengan nilai IMT =", round(index_massa_tubuh, 2))
# else:
#     print("Jenis kelamin anda tidak ada")

# no6. Fungsi segitiga -1
# def cek_segitiga(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True
# 
# print(cek_segitiga(1, 1, 1))
# print(cek_segitiga(1, 1, 3))

# no7. Fungsi segitiga -2
# def cek_segitiga(a, b, c):
#     if a + b <= c or b + c <= a or c + a <= b:
#         return False
#     return True
# 
# print(cek_segitiga(1, 1, 1))
# print(cek_segitiga(1, 1, 3))

# no8. Fungsi segitiga -3
# def cek_segitiga(a, b, c):
#     return a + b > c and b + c > a and c + a > b
# 
# print(cek_segitiga(1, 1, 1))
# print(cek_segitiga(1, 1, 3))

# no9. Kuis faktorial
# def faktorial(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     hasil = 1
#     for i in range(2, n + 1):
#         hasil *= i
#     return hasil
# 
# n = int(input("masukan nilai yang ingin di faktorial :"))
# print(n, "! =", faktorial(n))

# no10. Kuis Fibonacci
# def fibonacci(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     elem_1 = 1
#     elem_2 = 1
#     hasil_jumlah = 0
#     for i in range(3, n + 1):
#         hasil_jumlah = elem_1 + elem_2
#         elem_1 = elem_2
#         elem_2 = hasil_jumlah
#     return hasil_jumlah
# 
# # test
# for n in range(1, 10):
#     print(n, "->", fibonacci(n))

# no11. Rekursif faktorial
# def faktorial_rekursif(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * faktorial_rekursif(n - 1)
# 
# nilai = int(input("Masukkan angka: "))
# print("Hasil faktorial:", faktorial_rekursif(nilai))

# no12. Rekursif fibonacci
# def fibonacci_rekursif(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)
# 
# # test
# for i in range(1, 8):
#     print("Fibonacci ke-", i, "adalah", fibonacci_rekursif(i))