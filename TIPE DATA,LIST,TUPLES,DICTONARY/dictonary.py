aku = {"nama": "Rio Agus Setiawan"
       "url:" "https://www.fsttundikma.id",}
                                        
# Cara membuat Dictionary
# contoh jika 1 item
nama_dict = {
    "key": "value"
}

# contoh jika lebih dari 1 item
nama_dict = {
    "key1": "value",
    "key2": "value",
    "key3": "value"
}

# membuat dictionary
dict = {
    "nama"      : "Rio Agus Setiawan",
    "NIDN"      : 24241044,
    "Prodi"     : "Pendidikan Teknologi Informasi",
    "mat_kul"    : ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO'],
    "status"    : True,
    "sosmed"    : {
        "Github"    : "@Trioxtwz/struktur-data-rio-styawan-24241044",
        "twiter"    : '_',
        "instagram" : '-'
    }
}

# Fungsi atau Method Dictionary
# Mengakses Nilai Dictionary

# mengakses dict menggunakan key
print("Nama Saya adalah %s" % dict['nama'])
print("Akun Github saya %s" % dict['sosmed']['Github'])

# cara lainnya dengan menggunakan .get
print("NIDN Saya adalah %s" % dict.get('NIDN'))

# Mengubah Nilai Item Dictionary

# Buat dictionary dengan nama 'data'
data = {
    "nama": "Rio agus setiawan",
    "status": True
}

# Ubah nilai item dictionary
data['status'] = False

# Cek hasil perubahan
print(data['status'])

# Mengubah nilai dictionary dengan .update()
data.update({
    "sosmed": {
        "twitter": ""
    }
})

# Cek hasil perubahan
print(data['sosmed']['twitter'])

# Menghapus Nilai Item Dictionary 

# Menghapus menggunakan perintah del
del data['status']

# cek hasil penghapusan data 
print(data)

# Menghapus item menggunkan method pop()
data.pop("sosmed")

# cek hasil penghapusan data 
print(data)

# Buat dictionary awal
data = {
    "nama": "Rio agus setiawan",
    "NIDN": 24241044,
    "Prodi": "Pendidikan Teknologi Informasi",
    "mat_kul": ["Algoritma dan Pemrograman", "Struktur Data", "PBO"],
    "sosmed": {
        "twitter": ""
    }
}

# Tampilkan data awal
print(data)

# Hapus item 'sosmed' dari dictionary
data.pop("sosmed")

# Tampilkan data setelah penghapusan
print(data)

data.clear()

# Menambahkan item pada dictionary

# membuat dictionary
mahasiswa = {
    "name" : "Rio agus setiawan"
}

# menambahkan nim
mahasiswa.update({
    "nidn" : "24241044"
})

# melihat hasilnya
print(mahasiswa)

# Looping Dictionary

# mencetak data pada dict secara berulang-ulang setiap key
for key in mahasiswa:
    print(key, mahasiswa[key])

# Atau:
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

# Latihan Dictionary

data_mahasiswa = {}
jumlah = int(input("Jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nim = input("NIM: ")
    nama = input("Nama: ")
    jurusan = input("Jurusan: ")
    data_mahasiswa[nim] = {
        "nama": nama,
        "jurusan": jurusan
    }


print("\nCari data mahasiswa")
cari = input("Masukkan NIM: ")
if cari in data_mahasiswa:
    mhs = data_mahasiswa[cari]
    print(f"Nama: {mhs['nama']}, Jurusan: {mhs['jurusan']}")
else:
    print("Mahasiswa tidak ditemukan.")

print("\nDaftar Seluruh Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} → {info['nama']} ({info['jurusan']})")