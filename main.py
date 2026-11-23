# Import Class
from paketWisata import paketWisata
from wisataAlam import WisataAlam
from wisataBudaya import WisataBudaya
from pelanggan import pelanggan

# List Penyimpanan Data
daftarPaketWisata = []
daftarWisataAlam = []
daftarWisataBudaya = []
daftarPelanggan = []


# Fungsi-Fungsi Paket Wisata

# Tambah
def tambahPaketWisata():
    idPaket = max((paket.getidPaket() for paket in daftarPaketWisata), default=0) + 1
    namaPaket = input("Masukkan Nama Paket: ")
    hargaPaket = int(input("Masukkan Harga Paket: "))
    durasiPaket = float(input("Masukkan Durasi Paket: "))
    lokasiPaket = input("Masukkan Lokasi Paket: ")
    kuotaPaket = int(input("Masukkan Kuota Paket: "))
    fasilitasPaket = input("Masukkan Fasilitas Paket Wisata: ")

    paket = paketWisata(
        idPaket, namaPaket, hargaPaket, durasiPaket,
        lokasiPaket, kuotaPaket, fasilitasPaket
    )

    daftarPaketWisata.append(paket)
    print("Paket wisata berhasil ditambahkan")


# Tampilkan
def tampilkanPaketWisata():
    if len(daftarPaketWisata) == 0:
        print("Belum ada data paket wisata")
    else:
        for paket in daftarPaketWisata:
            paket.tampilkanInfoPaket()
            print("--------------------")


# Cari
def cariPaketWisata():
    idPaket = int(input("Masukkan ID Paket Wisata yang dicari: "))

    for paket in daftarPaketWisata:
        if paket.getidPaket() == idPaket:
            paket.tampilkanInfoPaket()
            return

    print("Paket wisata tidak ditemukan")


# Edit
def ubahPaketWisata():
    idPaket = int(input("Masukkan ID Paket Wisata yang ingin diubah: "))

    for paket in daftarPaketWisata:
        if paket.getidPaket() == idPaket:
            print("1. Ubah Harga Paket")
            print("2. Ubah Fasilitas Paket")

            pilihan = input("Masukkan pilihan: ")

            if pilihan == "1":
                hargaBaru = float(input("Masukkan Harga Baru: "))
                paket.ubahHargaPaket(hargaBaru)
                print("Harga paket berhasil diubah")

            elif pilihan == "2":
                fasilitasBaru = input("Masukkan Fasilitas Baru: ")
                paket.ubahFasilitasPaket(fasilitasBaru)
                print("Fasilitas paket berhasil diubah")

            else:
                print("Pilihan tidak valid")

            return

    print("Paket wisata tidak ditemukan")


# Cek Kuota
def cekKuotaPaketWisata():
    idPaket = int(input("Masukkan ID Paket Wisata: "))

    for paket in daftarPaketWisata:
        if paket.getidPaket() == idPaket:
            paket.cekKuotaPaketWisata()
            return

    print("Paket wisata tidak ditemukan")


# Hapus
def hapusPaketWisata():
    idPaket = int(input("Masukkan ID Paket Wisata yang ingin dihapus: "))

    for paket in daftarPaketWisata:
        if paket.getidPaket() == idPaket:
            daftarPaketWisata.remove(paket)
            print("Paket wisata berhasil dihapus")
            return

    print("Paket wisata tidak ditemukan")


# Menu Paket Wisata
def menuPaketWisata():
    while True:
        print("\n--- Menu Paket Wisata ---")
        print("1. Tambah Paket Wisata")
        print("2. Tampilkan Paket Wisata")
        print("3. Cari Paket Wisata")
        print("4. Ubah Paket Wisata")
        print("5. Cek Kuota Paket Wisata")
        print("6. Hapus Paket Wisata")
        print("7. Kembali ke Menu Utama")

        pilihan = input("Masukkan Pilihan (1-7): ")

        if pilihan == "1":
            tambahPaketWisata()

        elif pilihan == "2":
            tampilkanPaketWisata()

        elif pilihan == "3":
            cariPaketWisata()

        elif pilihan == "4":
            ubahPaketWisata()

        elif pilihan == "5":
            cekKuotaPaketWisata()

        elif pilihan == "6":
            hapusPaketWisata()

        elif pilihan == "7":
            break

        else:
            print("Pilihan tidak valid.")



# Fungsi-Fungsi Pengelolaan Pelanggan
# Tambah
def tambahPelanggan():
    pass

# Tampil
def tampilkanPelanggan():
    pass

# Cari
def cariPelanggan():
    pass

# Edit
def ubahPelanggan():
    pass


# Menu Pelanggan
def menuPelanggan():
    pass


# Fungsi-Fungsi Pengelolaan Pemesanan
# Tambah
def pesanPaketWisata():
    pass

# Tampil
def tampilkanPemesanan():
    pass

# Hapus
def batalkanPemesanan():
    pass

# Cek
def cekStatusPemesanan():
    pass


# Menu Pemesanan
def menuPemesanan():
    pass


# Menu Utama
def menuUtama():
    while True:
        print("\n=== APLIKASI PAKET WISATA ===")
        print("1. Kelola Paket Wisata")
        print("2. Kelola Pelanggan")
        print("3. Kelola Pemesanan")
        print("4. Keluar")

        pilihan = input("Masukkan Pilihan (1-4): ")

        if pilihan == "1":
            menuPaketWisata()

        elif pilihan == "2":
            menuPelanggan()

        elif pilihan == "3":
            menuPemesanan()

        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi!")
            break

        else:
            print("Pilihan tidak valid.")



if __name__ == "__main__":
    menuUtama()
