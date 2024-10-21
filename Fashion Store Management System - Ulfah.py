data_baju = {
    "a1": {"Nama": "King T-Shirt", "Kategori": "Pria", "Stok": 28, "Harga": 60000},
    "a2": {"Nama": "Yura Dress", "Kategori": "Wanita", "Stok": 16, "Harga": 150000},
    "a3": {"Nama": "Boyz Jacket", "Kategori": "Pria", "Stok": 11, "Harga": 95000},
    "a4": {"Nama": "Kidz Pajamas", "Kategori": "Anak", "Stok": 15, "Harga": 55000},
    "a5": {"Nama": "Lyla Pashmina", "Kategori": "Wanita", "Stok": 23, "Harga": 40000},
    "a6": {"Nama": "Baby Jumpsuit", "Kategori": "Anak", "Stok": 40, "Harga": 65000},
    "a7": {"Nama": "Cool Denim", "Kategori": "Pria", "Stok": 22, "Harga": 85000},
    "a8": {"Nama": "Sweet Blouse", "Kategori": "Wanita", "Stok": 9, "Harga": 40000}
}

# 1
# READ
# Fungsi untuk menampilkan data baju
def tampilkan_data_baju():
    if not data_baju:
        print("\nBelum ada data baju. Anda akan kembali ke Menu Utama.")
        return menu_utama()
    else:
        print("\n=============== Data Baju di Fashion Store ===============")
        print("+------+-------------------+-----------+-------+----------+")
        print("| Kode | Nama              | Kategori  | Stok  |  Harga   |")
        print("+------+-------------------+-----------+-------+----------+")
        for kode, info in data_baju.items():
            nama = info["Nama"].ljust(17)
            kategori = info["Kategori"].ljust(9)
            stok = str(info["Stok"]).rjust(5)
            harga = str(info["Harga"]).rjust(8)
            print(f"| {kode}  | {nama} | {kategori} | {stok} | {harga} |")
        print("+------+-------------------+-----------+-------+----------+\n")


def menu_read():
    while True:
        try:
            opsi = int(input('''
----------------------------------------------------------

Pilihan menampilkan data:
    1. Tampilkan semua data baju
    2. Lihat data baju sesuai kode barang
    3. Lihat data baju sesuai kategori
    4. Kembali ke Menu Utama
        
Untuk menampilkan data, silakan masukkan angka yang ingin dijalankan: '''))

            if opsi == 1:
                tampilkan_data_baju()
            elif opsi == 2:
                cari_kode_baju()
            elif opsi == 3:
                cari_kategori_baju()
            elif opsi == 4:
                menu_utama()
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan angka sesuai menu")
        except:
            print("Input tidak valid. Silakan masukkan angka antara 1 hingga 4.")


def cari_kode_baju():
    kode_cari = input("Masukkan kode baju yang ingin dicari: ")
    if kode_cari in data_baju:
        info = data_baju[kode_cari]
        print(f"\n=== Informasi Baju dengan Kode {kode_cari} ===")
        print(f"Nama     : {info['Nama']}")
        print(f"Kategori : {info['Kategori']}")
        print(f"Stok     : {info['Stok']}")
        print(f"Harga    : {info['Harga']}\n")
    else:
        print(f"Baju dengan kode {kode_cari} tidak ditemukan.\n")


def cari_kategori_baju():
    kategori_baju = input("Masukkan kategori yang ingin dicari (Pria/Wanita/Anak): ").capitalize()

    kategori_ditemukan = False
    print(f"\n=== Daftar Baju dalam Kategori: {kategori_baju} ===")
    print("+------+-------------------+-----------+-------+----------+")
    print("| Kode | Nama              | Kategori  | Stok  |  Harga   |")
    print("+------+-------------------+-----------+-------+----------+")
    
    for kode, info in data_baju.items():
        if info["Kategori"] == kategori_baju:
            nama = info["Nama"].ljust(17)
            kategori = info["Kategori"].ljust(9)
            stok = str(info["Stok"]).rjust(5)
            harga = str(info["Harga"]).rjust(8)
            print(f"| {kode}  | {nama} | {kategori} | {stok} | {harga} |")
            kategori_ditemukan = True

    if not kategori_ditemukan:
        print(f"Tidak ada baju yang ditemukan dalam kategori {kategori_baju}.")

    print("+------+-------------------+-----------+-------+----------+\n")


#2
# CREATE
# Fungsi untuk menambah data baju
def tambah_data_baju():
    while True:
        opsi = input('''
----------------------------------------------------------
Apakah anda ingin menambahkan data baju (y/n)?: ''').lower()
        
        if opsi == 'y':
            while True:
                kode_baru = input("Masukkan kode baju baru: ").lower()
                if kode_baru in data_baju:
                    print(f"Kode {kode_baru} sudah ada. Gunakan kode lain.")
                else:
                    break

            nama_baju = input("Masukkan nama baju: ").capitalize()
            
            kategori_baju = ''
            while kategori_baju not in ['Pria', 'Wanita', 'Anak']:
                kategori_baju = input("Masukkan kategori baju (Pria/Wanita/Anak): ").capitalize()
                if kategori_baju not in ['Pria', 'Wanita', 'Anak']:
                    print("Kategori tidak valid. Silakan pilih dari Pria, Wanita, atau Anak.")
                    
            while True:
                try:
                    stok_baju = int(input("Masukkan stok baju: "))
                    break
                except ValueError:
                    print("Input stok harus berupa angka.")
            
            while True:
                try:
                    harga_baju = int(input("Masukkan harga baju: "))
                    break
                except ValueError:
                    print("Input harga harus berupa angka.")

            simpan = input("Apakah anda ingin menyimpan data (y/n)?: ").lower()
            if simpan == 'y':
                data_baju[kode_baru] = {"Nama": nama_baju, "Kategori": kategori_baju, "Stok": stok_baju, "Harga": harga_baju}
                print(f"Baju dengan kode {kode_baru} berhasil ditambahkan.")
                tampilkan_data_baju()
            else:
                print("Data belum tersimpan.")
        
        elif opsi == 'n':
            print("Kembali ke Menu Utama")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih 'y' atau 'n'.")


# 3
# UPDATE
# Fungsi untuk memperbarui data baju
def menu_update():
    while True:
        opsi = str(input('''
----------------------------------------------------------
Apakah anda ingin meng-update data baju (y/n)?: ''')).lower()
        
        if opsi == 'y':
            kode = input("Masukkan kode baju yang ingin diperbarui: ").lower()
            if kode in data_baju:
                print(f"\nData baju dengan kode {kode}:")
                data_baju_yang_dipilih(kode)
                kolom = int(input('''
Indeks Kolom:
    1. Nama
    2. Kategori
    3. Stok
    4. Harga

Masukkan indeks kolom yang ingin di-update: '''))

                if kolom == 1:
                    data_update = str(input("Masukkan Nama Baju yang baru: ")).capitalize()
                    simpan = str(input("Apakah anda ingin menyimpan data (y/n)? ")).lower()
                    if simpan == 'y':
                        data_baju[kode]['Nama'] = data_update
                        print("Data berhasil disimpan.")
                    else:
                        print("Data belum tersimpan.")
                
                elif kolom == 2:
                    while True:
                        data_update = str(input("Masukkan Kategori Baju yang baru (Pria/Wanita/Anak): ")).capitalize()
                        if data_update in ['Pria', 'Wanita', 'Anak']:
                            break
                        else:
                            print("Kategori tidak valid. Silakan masukkan Pria, Wanita, atau Anak.")
                    
                    simpan = str(input("Apakah anda ingin menyimpan data (y/n)? ")).lower()
                    if simpan == 'y':
                        data_baju[kode]['Kategori'] = data_update
                        print("Data berhasil disimpan.")
                    else:
                        print("Data belum tersimpan.")
                
                elif kolom == 3:
                    data_update = int(input("Masukkan Stok Baju yang baru: "))
                    simpan = str(input("Apakah anda ingin menyimpan data (y/n)? ")).lower()
                    if simpan == 'y':
                        data_baju[kode]['Stok'] = data_update
                        print("Data berhasil disimpan.")
                    else:
                        print("Data belum tersimpan.")
                
                elif kolom == 4:
                    data_update = int(input("Masukkan Harga Baju yang baru: "))
                    simpan = str(input("Apakah anda ingin menyimpan data (y/n)? ")).lower()
                    if simpan == 'y':
                        data_baju[kode]['Harga'] = data_update
                        print("Data berhasil disimpan.")
                    else:
                        print("Data belum tersimpan.")
                
                else:
                    print("Indeks kolom tidak valid.")
               
                tampilkan_data_baju()
            
            else:
                print(f"Baju dengan kode {kode} tidak ditemukan.")
        
        elif opsi == 'n':
            print("Kembali ke Menu Utama")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih 'y' atau 'n'.")
    

# 4
# DELETE
# Fungsi untuk menghapus data baju
def menu_hapus():
    while True:
        opsi = str(input('''
----------------------------------------------------------
Apakah anda ingin menghapus data baju (y/n)?: ''')).lower()
        if opsi == 'y':
            kode = input("Masukkan kode baju yang ingin dihapus: ")
            if kode in data_baju:
                print(f"Data baju dengan kode {kode}:")
                data_baju_yang_dipilih(kode)
                hapus = str(input("Apakah anda ingin menghapus data ini (y/n)?: ")).lower()
                
                if hapus == 'y':
                    del data_baju[kode]
                    print(f"Baju dengan kode {kode} telah dihapus.")
                    tampilkan_data_baju()
                else:
                    print("Data tidak jadi dihapus.")
            else:
                print(f"Baju dengan kode {kode} tidak ditemukan.")
        
        elif opsi == 'n':
            print("Kembali ke Menu Utama")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih 'y' atau 'n'.")


# additional untuk fungsi UPDATE dan DELETE
def data_baju_yang_dipilih(kode):
    if kode in data_baju:
        info = data_baju[kode]
        print(f"Nama     : {info['Nama']}")
        print(f"Kategori : {info['Kategori']}")
        print(f"Stok     : {info['Stok']}")
        print(f"Harga    : {info['Harga']}\n")
    else:
        print(f"Baju dengan kode {kode} tidak ditemukan.")
        

# 5
# EXIT
def menu_keluar():
    while True:
        opsi = str(input('''
----------------------------------------------------------
Apakah anda ingin keluar dari program (y/n)?: ''')).lower()
        if opsi == 'y':
            print('\nAnda telah keluar dari aplikasi Fashion Store.')
            print('Have a good day (^--^)')
            exit()
        else:
            print("Kembali ke Menu Utama")
            menu_utama()


# Program utama
def menu_utama():
    while True:
        pilih_menu = int(input('''
=============== Welcome to Fashion Store ===============
                            
        List Menu Utama:
            1. Menampilkan Data Baju 
            2. Menambah Data Baju 
            3. Memperbaharui Data Baju 
            4. Menghapus Data Baju
            5. Keluar
                                
========================================================
Masukkan angka menu yang ingin dijalankan: '''))

        if pilih_menu == 1:
            menu_read()
        elif pilih_menu == 2:
            tambah_data_baju()
        elif pilih_menu == 3:
            menu_update()
        elif pilih_menu == 4:
            menu_hapus()
        elif pilih_menu == 5:
            menu_keluar()
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
menu_utama()


