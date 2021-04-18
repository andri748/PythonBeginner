# ------------List Dan Tuple------------
bulan_pembelian = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')
# --------Mengakses list dan tuple part 1--------
"""print(bulan_pembelian[0])
print(bulan_pembelian[5])
print(bulan_pembelian[11])
print(bulan_pembelian[10])
print(bulan_pembelian[-1])
print(bulan_pembelian[-2])"""

# --------Mengakses list dan tuple part 2--------
"""pertengahan_tahun = bulan_pembelian[4:8]
print(pertengahan_tahun)
awal_tahun = bulan_pembelian[:5]
print(awal_tahun)
akhir_tahun = bulan_pembelian[8:]
print(akhir_tahun)
print(bulan_pembelian[-4:-1])"""# memotong suatu list/tuple dengan menggunakan indeks negatif.

# -------Menggabungkan List-------
"""list_makanan = ['Gado-gado','Ayam Goreng','Rendang']
list_minuman = ['Es Teh','Es Jeruk','Es Campur']
list_menu = list_makanan + list_minuman
print(list_menu)"""

# -------List Manipulation Features-------
# Fitur .append()
"""-----print(">>> Fitur .append()")-----
list_makanan = ['Gado-gado', 'Mie Goreng', 'Rendang']
list_makanan.append('Ketoprak')
print(list_makanan)
# Fitur .clear()
print(">>> Fitur .clear()")
list_makanan = ['Gado-gado', 'Nasi Goreng', 'Rendang']
list_makanan.clear()
print(list_makanan)
# Fitur .copy()
print(">>> Fitur .copy()")
list_makanan1 = ['Gado-gado', 'Tempe Goreng', 'Rendang']
list_makanan2 = list_makanan1.copy()
list_makanan3 = list_makanan1
list_makanan2.append('Opor')
list_makanan3.append('Ketoprak')
print(list_makanan1)
print(list_makanan2)
# Fitur .count()
print(">>> Fitur .count()")
list_score = ['Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud']
score_budi = list_score.count('Budi')
score_sud = list_score.count('Sud')
print(score_budi) # akan menampilkan output 4
print(score_sud) # akan menampilkan output 3
# Fitur .extend()
print(">>> Fitur .extend()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu.extend(list_minuman)
print(list_menu)"""
"""-----# Fitur .index()-----
print(">>> Fitur .index()")
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
score_pertama_sud = list_score.index('Sud') + 1
print(score_pertama_sud) # akan menampilkan output 2
# Fitur .insert()
print(">>> Fitur .insert()")
list_score = ['Budi','Sud','Budi','Budi','Sud']
list_score.insert(3, 'Busud')
print(list_score) # akan menampikan Busud setelah baris ke 3
# Fitur .pop()
print(">>> Fitur .pop()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_menu.pop(1)
print(list_menu)
# Fitur .remove()
print(">>> Fitur .remove()")
list_menu = ['Gado-gado', 'Tempe Goreng', 'Rendang', 'Ketoprak']
list_menu.remove('Rendang')
print(list_menu)
# Fitur .reverse()
print(">>> Fitur .reverse()")
list_menu = ['Gado-gado', 'Tahu Goreng', 'Rendang', 'Ketoprak']
list_menu.reverse()
print(list_menu)
# Fitur .sort()
print(">>> Fitur .sort()")
list_menu = ['Gado-gado', 'Nasi Goreng', 'Rendang', 'Ketoprak']
list_menu.sort() # Default: Ascending
print(list_menu) 
list_menu.sort(reverse=True)# Descending
print(list_menu)"""

# ------------Set Manipulation------------
"""-----# Fitur .add() tipe data set tidak mengizinkan adanya duplikasi elemen di dalamnya.-----
print(">>> Fitur .add()")
set_buah = {'Jeruk','Apel','Anggur'}
set_buah.add('Melon')
print(set_buah)
# Fitur .clear() Menghapus seluruh elemen dalam sebuah set
print(">>> Fitur .clear()")
set_buah = {'Jeruk','Apel','Anggur'}
set_buah.clear()
print(set_buah)
# Fitur .copy() Mengembalikan copy dari setiap elemen
print(">>> Fitur .copy()")
set_buah1 = {'Jeruk','Apel','Anggur'}
set_buah2 = set_buah1
set_buah3 = set_buah1.copy()
set_buah2.add('Melon')
set_buah3.add('Kiwi')
print(set_buah1)
print(set_buah2)
# Fitur .update() Menambahkan elemen dari suatu set dengan set lainnya.
print(">>> Fitur .update()")
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Apel','Kiwi','Melon'}
parcel1.update(parcel2)
print(parcel1)
# Fitur .pop() Menghilangkan elemen dari sebuah set secara acak.
print(">>> Fitur .pop()")
parcel = {'Anggur','Apel','Jeruk'}
buah = parcel.pop()
print(buah)
print(parcel)
# Fitur .remove() Menghilangkan elemen dengan nilai tertentu 	 
print(">>> Fitur .remove()")
parcel = {'Anggur','Apel','Jeruk'}
parcel.remove('Apel')
print(parcel)"""
# Fitur .union() Mengembalikan hasil penggabungan (union) dari dua buah set.
"""print(">>> Fitur .union()")
parcel1 = {'Anggur', 'Apel', 'Jeruk'}
parcel2 = {'Apel', 'Kiwi', 'Melon'}
parcel3 = parcel1.union(parcel2)
print(parcel1)
print(parcel3)
# Fitur .isdisjoint() --Mengembalikan nilai kebenaran apakah suatu set disjoint (saling lepas/tidak mengandung elemen
# yang sama) dengan set lainnya.
print(">>> Fitur .isdisjoint()")
parcel1 = {'Anggur', 'Apel', 'Jeruk'}
parcel2 = {'Kiwi', 'Melon', 'Pisang'}
parcel3 = {'Apel', 'Srikaya', 'Semangka'}
parcel1_parcel2_disjoint = parcel1.isdisjoint(parcel2)
print(parcel1_parcel2_disjoint)
parcel1_parcel3_disjoint = parcel1.isdisjoint(parcel3)
print(parcel1_parcel3_disjoint)
# Fitur .issubset() --Mengembalikan nilai kebenaran apakah sebuah set merupakan subset dari set lainnya. 
# Sebuah set A merupakan subset dari set B jika seluruh elemen dari set A merupakan bagian dari set B.
print(">>> Fitur .issubset()")
parcel_A = {'Anggur', 'Apel'}
parcel_B = {'Durian', 'Semangka', 'Apel'}
parcel_C = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_A_dalam_C = parcel_A.issubset(parcel_C)
parcel_B_dalam_C = parcel_B.issubset(parcel_C)
print(parcel_A_dalam_C)
print(parcel_B_dalam_C)
# Fitur .issuperset() --Mengembalikan nilai kebenaran apakah sebuah set merupakan superset dari set lainnya. 
# Sebuah set A merupakan superset dari set B jika seluruh elemen dari set B terkandung dalam set A.
print(">>> Fitur .issuperset()")
parcel_C_mengandung_A = parcel_C.issuperset(parcel_A)
parcel_C_mengandung_B = parcel_C.issuperset(parcel_B)
print(parcel_C_mengandung_A)
print(parcel_C_mengandung_B)
# Fitur .intersection() Mengembalikan sebuah set yang merupakan intersection dari dua set lainnya
print(">>> Fitur .intersection()")
parcel_A = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_B = {'Apel', 'Jeruk', 'Semangka', 'Durian', 'Tomat'}
parcel_C = parcel_A.intersection(parcel_B)
print(parcel_C)
# Fitur .difference() Mengembalikan sebuah set yang berisikan difference dari dua set lainnya. Difference dari 
# sebuah set A berdasarkan set B adalah setiap elemen yang terdapat di set A tetapi tidak terdapat di set B.
print(">>> Fitur .difference()")
parcel_C = parcel_A.difference(parcel_B)
print(parcel_C)
# Fitur .symmetric_difference() Mengembalikan sebuah set yang berisikan symmetric difference dari dua set lainnya. 
# Symmetric difference dari sebuah set A dan B adalah setiap elemen dari set A yang tidak terdapat di set B
# digabungkan dengan (union) setiap elemen dari set B yang tidak terdapat di set A.
print(">>> Fitur .symmetric_difference()")
parcel_A = {'Anggur', 'Apel', 'Jeruk', 'Melon'}
parcel_B = {'Apel', 'Jeruk', 'Semangka', 'Leci'}
parcel_C = parcel_A.symmetric_difference(parcel_B)
print(parcel_C)"""
# -----------Dictionary Manipulation-----------
"""# Fitur .clear()
print(">>> Fitur .clear()")
info_karyawan = {'nama': 'Aksara',
                 'nik': '1211011',
                 'pekerjaan' : 'Data Analyst'}
info_karyawan.clear()
print(info_karyawan)
# Fitur .copy()
print(">>> Fitur .copy()")
info_karyawan1 = {'nama': 'Aksara',
                  'nik': '1211011',
                  'pekerjaan' : 'Data Analyst'}
info_karyawan2 = info_karyawan.copy()
info_karyawan2['nama'] = 'Senja'
info_karyawan2['nik'] = '1211056'
print(info_karyawan1)
print(info_karyawan2)
# Fitur .keys()
print(">>> Fitur .keys()")
info_karyawan = {'nama': 'Aksara',
                 'nik': '1211011',
                 'pekerjaan': 'Data Analyst'}
kunci_akses = info_karyawan.keys()
print(kunci_akses)
# Fitur .values()
print(">>> Fitur .values()")
value_dict = info_karyawan.values()
print(value_dict)
# Fitur .update()
print(">>> Fitur .update()")
info_karyawan.update({'skillset': ['Python', 'R']})
print(info_karyawan)"""
# -----------Useful Tips and Trick----------
# Tuple
"""print(">>> Tuple")
tuple_menu = ('Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak')
jumlah_menu = len(tuple_menu)
print(jumlah_menu)
# List
print(">>> List")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
jumlah_menu = len(list_menu)
print(jumlah_menu)
# Konversi tipe data
print(">>> Konversi tipe data")
list_buah = ['Apel', 'Apel', 'Jeruk', 'Markisa', 'Jeruk', 'Markisa', 'Apel']
set_buah = set(list_buah)
print(set_buah)
list_buah = list(set_buah)
list_buah.sort()
print(list_buah)"""
# ----------Data Keuangan-----------
"""keuangan = {
'pengeluaran': [2, 2.5, 2.25, 2.5, 3.2, 2.5, 3.5, 4, 3],
'pemasukan': [7.8, 7.5, 9, 7.6, 7.2, 7.5, 7, 10, 7.5]
}
# Perhitungan rata-rata pemasukan dan rata-rata pengeluaran
total_pengeluaran = 0
total_pemasukan = 0
for biaya in keuangan['pengeluaran']:
    total_pengeluaran += biaya
for biaya in keuangan['pemasukan']:
    total_pemasukan += biaya
rata_rata_pengeluaran = total_pengeluaran/len(keuangan['pengeluaran'])
rata_rata_pemasukan = total_pemasukan/len(keuangan['pemasukan'])
print(rata_rata_pengeluaran)
print(rata_rata_pemasukan)"""
# ----------String Manipulation---------
"""nama_produk = "Sepatu Niko"
nama_produk = nama_produk[:2] + "P" + nama_produk[3:9] + "K" + nama_produk[-1]
print(nama_produk)
print(nama_produk[:7])
print(nama_produk[7:])
print(len(nama_produk))"""
# ---------Operator '+' untuk string----------
"""nama_depan = 'andri'
nama_belakang = 'nur'
nama_lengkap = nama_depan + ' ' + nama_belakang
print(nama_lengkap)
umur = '19 tahun'
alamat = 'Jl. Anggrek No. 100'
nama_umur_alamat = 'Hi, saya ' + nama_lengkap + ', umur ' + umur + ', tinggal di ' + alamat + '.'
print(nama_umur_alamat)"""
# -----------Menghilangkan Spasi di Awal dan/atau di Akhir----------
"""# Fitur .strip()
print(">>> Fitur .strip()") # Menghilangkan kelebihan spasi pada awal dan akhir string.
kata_sambutan = ' halo, selamat pagi! '
kata_sambutan = kata_sambutan.strip()
print(kata_sambutan)
# Fitur .lstrip() # Menghilangkan kelebihan spasi pada awal string.
print(">>> Fitur .lstrip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.lstrip()
print(kata_sambutan)
# Fitur .rstrip() # Menghilangkan kelebihan spasi pada akhir string.
print(">>> Fitur .rstrip()")
kata_sambutan = ' halo, selamat sore! '
kata_sambutan = kata_sambutan.rstrip()
print(kata_sambutan)"""
#----------Merubah Caps Pada String----------
# Fitur .capitalize() Mengubah elemen pertama dari string menjadi huruf kapital.
"""print(">>> Fitur .capitalize()")
judul_buku = 'belajar bahasa Python'
print(judul_buku.capitalize())
# Fitur .lower() Mengubah seluruh huruf dalam teks (string) menjadi huruf kecil
print(">>> Fitur .lower()")
judul_buku = 'Belajar Bahasa PYTHON.'
print(judul_buku.lower())
# Fitur .upper() Mengubah seluruh huruf dalam teks (string) menjadi huruf besar
print(">>> Fitur .upper()")
judul_buku = 'Belajar Bahasa PYTHON.'
print(judul_buku.upper())"""
# ----------Pemecahan, Penggabungan, dan Penggantian String----------
# Fitur .split()
"""print(">>> Fitur .split()")
bilangan = "ani dan budi dan wati dan johan"
karakter = bilangan.split("dan")
print(karakter)
kata = bilangan.split(" ")
print(kata)
# Fitur .join()
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
kalimat = pemisah.join(karakter)
print(kalimat)
# Fitur .replace()
print(">>> Fitur .replace()")
kalimat = "apel malang apel yang paling segar, apel sehat, apel nikmat"
kalimat = kalimat.replace("apel", "jeruk")
print(kalimat)"""
judul_artikel = [
"Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium", "Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat",
"Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang", "Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi",
"Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes", "Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
"Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik", "Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
"Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak", "Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]
"""jumlah_artikel_jeruk = 0
jumlah_artikel_salak = 0
for judul in judul_artikel:
    if judul.count("Jeruk") > 0:
        jumlah_artikel_jeruk += 1
    if judul.count("Salak") > 0:
        jumlah_artikel_salak += 1
print(jumlah_artikel_jeruk)
print(jumlah_artikel_salak)"""
"""kata_positif = ["Kaya", "Baik", "Mencegah", "Memperkuat"]
kata_positif_jeruk = 0
kata_positif_salak = 0
for judul in judul_artikel:
    for kata in kata_positif:
        if judul.count("Jeruk") > 0 and judul.count(kata):
            kata_positif_jeruk += 1
        if judul.count("Salak") > 0 and judul.count(kata):
            kata_positif_salak += 1
print(kata_positif_jeruk)
print(kata_positif_salak)"""


