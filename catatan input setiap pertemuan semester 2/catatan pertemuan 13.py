# Hasil Ekstraksi Kode Praktikum
# Topik: Tuple, Dictionaries, Exceptions in python
# Nama: PIGA MISBAHUL HAPIDHIIN
# Kelas: 2-INF-A

# no1. Membuat tuple dan tampilkan
# tuple_1 = (1, 2, 4, 8)
# tuple_2 = 1., 5, 25, 125
# print(tuple_1)
# print(tuple_2)

# no2. Elemen tuple kosong dan satu elemen
# kosong_tuple = ()
# satu_elemen_tuple_1 = (1,)
# satu_elemen_tuple_2 = 1.,
# print(kosong_tuple)
# print(satu_elemen_tuple_1)
# print(satu_elemen_tuple_2)

# no3. Mengakses elemen tuple
# my_tuple = (1, 10, 100, 1000)
# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-2])
# for elemen in my_tuple:
#     print(elemen)

# no4. Operasi pada tuple
# my_tuple = (1, 10, 100)
# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3
# print(len(t2))
# print(10 in my_tuple)
# print(1000 not in my_tuple)

# no5. Membuat dictionary dan tampilkan
# dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
# phone_directory = {'boss': 5551234567, 'Suzy': 22657854310}
# empty_dict = {}
# print(dictionary)
# print(phone_directory)
# print(empty_dict)

# no6. Mengakses elemen dictionary
# dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
# print(dictionary['cat'])
# print(dictionary['horse'])

# no7. Menghindari kesalahan akses key (Menggunakan operator in)
# dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
# words = ['cat', 'lion', 'horse']
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "tidak ada di dictionary")

# no8. Method keys()
# dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

# no9. Method items() dan values()
# dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
# for key, val in dictionary.items():
#     print(key, "->", val)
# print("---")
# for value in dictionary.values():
#     print(value)

# no10. Mengubah dan menambah elemen dictionary
# dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
# dictionary['cat'] = 'minou'
# dictionary['swan'] = 'angsa'
# print(dictionary)

# no11. Menambah elemen dengan method update()
# dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
# dictionary.update({"duck": "bebek"})
# print(dictionary)

# no12. Menghapus elemen dengan del dan popitem()
# dictionary = {"cat": "kucing", "dog": "anjing", "horse": "kuda"}
# del dictionary['dog']
# print(dictionary)
# dictionary.popitem()
# print(dictionary)

# no13. Menyalin isi dictionary dengan copy()
# dictionary = {"cat": "kucing", "dog": "anjing"}
# dictionary_baru = dictionary.copy()
# print("Dict 1:", dictionary)
# print("Dict 2:", dictionary_baru)

# no14. Mengosongkan isi dictionary dengan clear()
# dictionary = {"cat": "kucing", "dog": "anjing"}
# dictionary.clear()
# print(dictionary)

# no15. Mengonversi tuple pasangan menjadi dictionary menggunakan fungsi dict()
# colors = (("green", "#008000"), ("blue", "#0000FF"))
# colors_dict = dict(colors)
# print(colors_dict)