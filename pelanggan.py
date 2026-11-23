
# Class Pelanggan
class pelanggan:
    def __init__(self, idPelanggan, namaPelanggan, no_telepon, daftarPesanan=None):
        self.__idPelanggan = idPelanggan
        self.__namaPelanggan = namaPelanggan
        self.__no_telepon = no_telepon
        self.__daftarPesanan = daftarPesanan if daftarPesanan is not None else []

    # Getter
    def getidPelanggan(self):
        return self.__idPelanggan

    def getnamaPelanggan(self):
        return self.__namaPelanggan

    def getnoTelepon(self):
        return self.__no_telepon

    # Mengubah data pelanggan
    def ubahDataPelanggan(self, namaBaru, noTeleponBaru):
        self.__namaPelanggan = namaBaru
        self.__no_telepon = noTeleponBaru

    # Memesan paket wisata
    def pesanPaket(self, paketWisata):
        self.__daftarPesanan.append(paketWisata)

    # Membatalkan pesanan
    def batalkanPesanan(self, paketWisata):
        if paketWisata in self.__daftarPesanan:
            self.__daftarPesanan.remove(paketWisata)
            print("Pesanan berhasil dibatalkan.")
        else:
            print("Pesanan tidak ditemukan.")

    # Menampilkan informasi pelanggan
    def tampilkanInfoPelanggan(self):
        print(f"ID Pelanggan: {self.__idPelanggan}")
        print(f"Nama: {self.__namaPelanggan}")
        print(f"No Telepon: {self.__no_telepon}")

    # Menampilkan pesanan pelanggan
    def tampilkanInfoPesanan(self):
        if not self.__daftarPesanan:
            print("Tidak ada pesanan yang ditemukan.")
        else:
            print("Daftar Pesanan:")
            for pesanan in self.__daftarPesanan:
                print(f"- {pesanan.getnamaPaket()} (ID: {pesanan.getidPaket()})")
