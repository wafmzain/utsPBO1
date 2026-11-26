# Main Program - Aplikasi Paket Wisata (CLI)
from paketWisata import PaketWisata
from wisataAlam import WisataAlam
from wisataBudaya import WisataBudaya
from pelanggan import Pelanggan

# List Penyimpanan Objek (Database Sederhana)
daftarPaketWisata = []
daftarPelanggan = []


# Fungsi - fungsi pengelolaan Paket Wisata
# Tambah Paket Wisata 
def tambahPaketWisata():
    print("\nPilih Kategori Paket Wisata:")
    print("1. Wisata Alam")
    print("2. Wisata Budaya")
    pilihanKategori = input("Masukkan pilihan kategori (1/2): ")

    if pilihanKategori not in ["1", "2"]:
        print("Pilihan kategori tidak valid.")
        return

    # ID otomatis 
    idPaket = max((paket.getIdPaket() for paket in daftarPaketWisata), default=0) + 1
    
    namaPaket = input("Masukkan Nama Paket: ")
    try:
        hargaPaket = float(input("Masukkan Harga Paket: "))
        durasiPaket = float(input("Masukkan Durasi Paket (hari): "))
        kuotaPaket = int(input("Masukkan Kuota Paket: "))
    except ValueError:
        print("Input harga, durasi, dan kuota harus berupa angka.")
        return

    lokasiPaket = input("Masukkan Lokasi Paket: ")
    fasilitasPaket = input("Masukkan Fasilitas Paket: ")

    if pilihanKategori == "1":
        jenisAktivitas = input("Masukkan Jenis Aktivitas (misal: Snorkeling/Hiking): ")
        tingkatKesulitan = input("Masukkan Tingkat Kesulitan (Mudah/Sedang/Sulit): ")
        perlengkapanKhusus = input("Masukkan Perlengkapan Khusus: ")

        paketBaru = WisataAlam(
            idPaket, namaPaket, hargaPaket, durasiPaket,
            lokasiPaket, kuotaPaket, fasilitasPaket,
            jenisAktivitas, tingkatKesulitan, perlengkapanKhusus
        )
    else:
        namaSitus = input("Masukkan Nama Situs/Tempat Bersejarah: ")
        jenisBudaya = input("Masukkan Jenis Budaya (misal: Tradisi/Candi/Kesenian): ")
        kegiatanBudaya = input("Masukkan Kegiatan Budaya: ")

        paketBaru = WisataBudaya(
            idPaket, namaPaket, hargaPaket, durasiPaket,
            lokasiPaket, kuotaPaket, fasilitasPaket,
            namaSitus, jenisBudaya, kegiatanBudaya
        )

    daftarPaketWisata.append(paketBaru)
    print(f"Paket wisata '{namaPaket}' berhasil ditambahkan dengan ID {idPaket}.")


# Tampilkan Semua Paket Wisata (Polymorphism)
def tampilkanPaketWisata():
    if not daftarPaketWisata:
        print("Belum ada data paket wisata.")
    else:
        print("\n=== DAFTAR PAKET WISATA ===")
        for paket in daftarPaketWisata:
            paket.tampilkanInfoPaket()
            print("-----------------------------------")


# Cari Paket Wisata berdasarkan ID
def cariPaketWisata():
    try:
        idPaket = int(input("Masukkan ID Paket Wisata yang dicari: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    for paket in daftarPaketWisata:
        if paket.getIdPaket() == idPaket:
            print("\nData Paket Ditemukan:")
            paket.tampilkanInfoPaket()
            return

    print("Paket wisata tidak ditemukan.")


# Ubah Data Paket Wisata
def ubahPaketWisata():
    try:
        idPaket = int(input("Masukkan ID Paket Wisata yang ingin diubah: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    for paket in daftarPaketWisata:
        if paket.getIdPaket() == idPaket:
            print(f"\nMengubah Paket: {paket.getNamaPaket()}")
            print("1. Ubah Harga Paket")
            print("2. Ubah Fasilitas Paket")
            pilihan = input("Masukkan pilihan (1/2): ")

            if pilihan == "1":
                try:
                    hargaBaru = float(input("Masukkan Harga Baru: "))
                    paket.ubahHargaPaket(hargaBaru)
                except ValueError:
                    print("Harga harus berupa angka.")
            elif pilihan == "2":
                fasilitasBaru = input("Masukkan Fasilitas Baru: ")
                paket.ubahFasilitasPaket(fasilitasBaru)
            else:
                print("Pilihan tidak valid.")
            return

    print("Paket wisata tidak ditemukan.")


# Cek Status / Kuota Paket Wisata
def cekStatusPaketWisata():
    try:
        idPaket = int(input("Masukkan ID Paket Wisata: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    for paket in daftarPaketWisata:
        if paket.getIdPaket() == idPaket:
            print(f"\n--- Status Paket: {paket.getNamaPaket()} ---")
            paket.cekKuotaPaket()
            if isinstance(paket, WisataAlam):
                paket.cekTingkatKesulitan()
            elif isinstance(paket, WisataBudaya):
                paket.tampilkanKegiatan()
            return

    print("Paket wisata tidak ditemukan.")


# Hapus Paket Wisata
def hapusPaketWisata():
    try:
        idPaket = int(input("Masukkan ID Paket Wisata yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    for paket in daftarPaketWisata:
        if paket.getIdPaket() == idPaket:
            daftarPaketWisata.remove(paket)
            print("Paket wisata berhasil dihapus.")
            return

    print("Paket wisata tidak ditemukan.")


# Sub-menu Paket Wisata
def menuPaketWisata():
    while True:
        print("\n--- Menu Paket Wisata ---")
        print("1. Tambah Paket Wisata")
        print("2. Tampilkan Paket Wisata")
        print("3. Cari Paket Wisata")
        print("4. Ubah Paket Wisata")
        print("5. Cek Status/Kuota Paket Wisata")
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
            cekStatusPaketWisata()
        elif pilihan == "6":
            hapusPaketWisata()
        elif pilihan == "7":
            break
        else:
            print("Pilihan tidak valid.")


# Fungsi - fungsi pengelolaan Pelanggan

# Tambah Pelanggan
def tambahPelanggan():
    idPelanggan = input("Masukkan ID Pelanggan: ")
    namaPelanggan = input("Masukkan Nama Pelanggan: ")
    noTelepon = input("Masukkan Nomor Telepon: ")

    pelangganBaru = Pelanggan(idPelanggan, namaPelanggan, noTelepon)
    daftarPelanggan.append(pelangganBaru)
    print("Pelanggan berhasil ditambahkan.")


# Tampilkan Seluruh Pelanggan
def tampilkanPelanggan():
    if not daftarPelanggan:
        print("Belum ada data pelanggan.")
    else:
        print("\n=== DAFTAR PELANGGAN ===")
        for data in daftarPelanggan:
            data.tampilkanInfoPelanggan()
            print("-------------------------")


# Cari Pelanggan
def cariPelanggan():
    idPelanggan = input("Masukkan ID Pelanggan yang dicari: ")

    for data in daftarPelanggan:
        if data.getIdPelanggan() == idPelanggan:
            print("\nData Pelanggan Ditemukan:")
            data.tampilkanInfoPelanggan()
            return

    print("Pelanggan tidak ditemukan.")


# Ubah Data Pelanggan
def ubahPelanggan():
    idPelanggan = input("Masukkan ID Pelanggan yang ingin diubah: ")

    for data in daftarPelanggan:
        if data.getIdPelanggan() == idPelanggan:
            namaBaru = input("Masukkan Nama Baru: ")
            noTeleponBaru = input("Masukkan Nomor Telepon Baru: ")
            data.ubahDataPelanggan(namaBaru, noTeleponBaru)
            return

    print("Pelanggan tidak ditemukan.")


# Sub-menu Pelanggan
def menuPelanggan():
    while True:
        print("\n=== MENU PELANGGAN ===")
        print("1. Tambah Pelanggan")
        print("2. Tampilkan Pelanggan")
        print("3. Cari Pelanggan")
        print("4. Ubah Data Pelanggan")
        print("5. Kembali ke Menu Utama")

        pilihan = input("Masukkan Pilihan (1-5): ")

        if pilihan == "1":
            tambahPelanggan()
        elif pilihan == "2":
            tampilkanPelanggan()
        elif pilihan == "3":
            cariPelanggan()
        elif pilihan == "4":
            ubahPelanggan()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi - fungsi pengelolaan Pemesanan

# Pesan Paket Wisata
def pesanPaketWisata():
    idPelanggan = input("Masukkan ID Pelanggan: ")
    pelangganDitemukan = None

    for data in daftarPelanggan:
        if data.getIdPelanggan() == idPelanggan:
            pelangganDitemukan = data
            break

    if not pelangganDitemukan:
        print("Pelanggan tidak ditemukan.")
        return

    try:
        idPaket = int(input("Masukkan ID Paket Wisata: "))
    except ValueError:
        print("ID Paket harus berupa angka.")
        return

    for paket in daftarPaketWisata:
        if paket.getIdPaket() == idPaket:
            pelangganDitemukan.pesanPaket(paket)
            return

    print("Paket wisata tidak ditemukan.")


# Tampilkan Seluruh Pemesanan
def tampilkanPemesanan():
    if not daftarPelanggan:
        print("Belum ada data pelanggan.")
    else:
        print("\n=== DAFTAR PEMESANAN PELANGGAN ===")
        for data in daftarPelanggan:
            print(f"\nPelanggan: {data.getNamaPelanggan()} (ID: {data.getIdPelanggan()})")
            data.tampilkanInfoPesanan()


# Batalkan Pesanan
def batalkanPemesanan():
    idPelanggan = input("Masukkan ID Pelanggan: ")
    pelangganDitemukan = None

    for data in daftarPelanggan:
        if data.getIdPelanggan() == idPelanggan:
            pelangganDitemukan = data
            break

    if not pelangganDitemukan:
        print("Pelanggan tidak ditemukan.")
        return

    try:
        idPaket = int(input("Masukkan ID Paket Wisata yang ingin dibatalkan: "))
    except ValueError:
        print("ID Paket harus berupa angka.")
        return

    for paket in pelangganDitemukan.getDaftarPesanan():
        if paket.getIdPaket() == idPaket:
            pelangganDitemukan.batalkanPesanan(paket)
            return

    print("Paket wisata tidak ditemukan di daftar pesanan pelanggan.")


# Cek Status Pemesanan
def cekStatusPemesanan():
    idPelanggan = input("Masukkan ID Pelanggan: ")

    for data in daftarPelanggan:
        if data.getIdPelanggan() == idPelanggan:
            print(f"\nStatus Pemesanan {data.getNamaPelanggan()}:")
            data.tampilkanInfoPesanan()
            return

    print("Pelanggan tidak ditemukan.")


# Sub-menu Pemesanan
def menuPemesanan():
    while True:
        print("\n=== MENU PEMESANAN ===")
        print("1. Pesan Paket Wisata")
        print("2. Tampilkan Pemesanan")
        print("3. Batalkan Pemesanan")
        print("4. Cek Status Pemesanan")
        print("5. Kembali ke Menu Utama")

        pilihan = input("Masukkan Pilihan (1-5): ")

        if pilihan == "1":
            pesanPaketWisata()
        elif pilihan == "2":
            tampilkanPemesanan()
        elif pilihan == "3":
            batalkanPemesanan()
        elif pilihan == "4":
            cekStatusPemesanan()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")


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
