# Hasil Ekstraksi Kode Praktikum
# Topik: Sorting and Operations Lists in Python
# Nama: Piga Misbahul Hapidhiin
# Kelas: II INF A

# no1. Bubble sort
# angka = [4, 2, 3, 1]
# for i in range(len(angka)):
#     for j in range(len(angka)-1):
#         if angka[j] > angka[j+1]:
#             angka[j], angka[j+1] = angka[j+1], angka[j]

# no2. Interactive Bubble sort
# data = input("Masukkan angka: ")
# angka = list(map(int, data.split()))
# for i in range(len(angka)):
#     print(f"Iterasi ke-{i+1}")
#     for j in range(len(angka) - 1):
#         if angka[j] > angka[j + 1]:
#             angka[j], angka[j+1] = angka[j + 1], angka[j]
#     print(angka)
# print("Hasil akhir:", angka)

# no3. Method sort
# angka = [4, 2, 3, 1]
# angka.sort(reverse=True)
# print(angka)

# no4. Method Reverse (Urut Kecil ke Besar / Sort Biasa)
# data = [3, 1, 4, 2]
# data.sort()
# print(data)

# no5. The inner life of list - 1
# list_1 = [1]
# list_2 = list_1
# list_1[0] = 2
# print(list_2)

# no6. Slice1: [awal:akhir]
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)

# no7. Slice2: [positif:negative]
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1]
# print(new_list)

# no8. Slice3: [negative:positif]
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[-1:1]
# print(new_list)

# no9. Slice-4: [awal:] (Mulai indeks 3 sampai akhir)
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[3:]
# print(new_list)

# no10. Slice-5: [:akhir] (Mulai awal sampai sebelum indeks 3)
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:3]
# print(new_list)

# no11. Slice 6: [:] (Menyalin list)
# data = [1, 2, 3, 4]
# salinan = data[:]
# print(salinan)

# no12. Menghapus slice
# data = [1, 2, 3, 4, 5]
# del data[1:4]
# print(data)

# no13. Menghapus semua elemen list (Menggunakan del [:])
# data = [1, 2, 3]
# del data[:]
# print(data)

# no14. Menghapus list (Menggunakan clear())
# data = [1, 2, 3]
# data.clear()
# print(data)

# no15. Penggunaan operator in
# data = [1, 2, 3, 4]
# print(2 in data)

# no16. Penggunaan operator not in
# angka = [10, 20, 30]
# if 40 not in angka:
#     print("Angka 40 tidak ada")

# no17. Simple program dari list -1 (Mencari terbesar manual dengan range)
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
# for i in range(1, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]
# print(largest)

# no18. Simple program dari list -2 (Mencari terbesar manual dengan iterasi langsung)
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
# for i in my_list:
#     if i > largest:
#         largest = i
# print(largest)

# no19. Simple program dari list -3 (Mencari indeks elemen / Linear Search)
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False
# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break
# if found:
#     print("Elemen ditemukan pada index ke-", i)
# else:
#     print("Tidak ada di dalam list")

# no20. Kuis 21 (Menghitung jumlah tebakan yang benar)
# tebakan = [3, 7, 11, 42, 34, 49]
# hasil = [5, 9, 11, 42, 3, 49]
# benar = 0
# for angka in tebakan:
#     if angka in hasil:
#         benar += 1
# print("Jumlah tebakan yang benar:", benar)

# no21. Kuis 22 (Menghapus data duplikat dalam list)
# data = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# unik = []
# for angka in data:
#     if angka not in unik:
#         unik.append(angka)
# print("List tanpa duplikat:", unik)
