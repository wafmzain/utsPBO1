# Class Pelanggan
# Relasi Asosiasi: Pelanggan memiliki relasi dengan PaketWisata
class Pelanggan:
    # Constructor berparameter
    def __init__(self, idPelanggan, namaPelanggan, noTelepon, daftarPesanan=None):
        # Enkapsulasi: atribut private
        self.__idPelanggan = idPelanggan
        self.__namaPelanggan = namaPelanggan
        self.__noTelepon = noTelepon
        # Daftar pesanan menampung objek PaketWisata (Relasi Asosiasi)
        self.__daftarPesanan = daftarPesanan if daftarPesanan is not None else []

    # Getter
    def getIdPelanggan(self):
        return self.__idPelanggan

    def getNamaPelanggan(self):
        return self.__namaPelanggan

    def getNoTelepon(self):
        return self.__noTelepon

    def getDaftarPesanan(self):
        return self.__daftarPesanan

    # Method untuk mengubah profil pelanggan
    def ubahDataPelanggan(self, namaBaru, noTeleponBaru):
        self.__namaPelanggan = namaBaru
        self.__noTelepon = noTeleponBaru
        print("Data pelanggan berhasil diperbarui.")

    # Method memesan paket wisata 
    def pesanPaket(self, paket):
        if paket.getKuotaPaket() > 0:
            if paket.kurangiKuota(1):
                self.__daftarPesanan.append(paket)
                print(f"Berhasil! Pelanggan {self.__namaPelanggan} telah memesan {paket.getNamaPaket()}.")
                return True
        else:
            print(f"Gagal! Kuota paket {paket.getNamaPaket()} sudah habis.")
            return False

    # Method membatalkan pesanan
    def batalkanPesanan(self, paket):
        if paket in self.__daftarPesanan:
            self.__daftarPesanan.remove(paket)
            paket.tambahKuota(1)
            print("Pesanan berhasil dibatalkan dan kuota telah dikembalikan.")
            return True
        else:
            print("Pesanan tidak ditemukan pada riwayat pelanggan ini.")
            return False

    # Method menampilkan informasi pelanggan
    def tampilkanInfoPelanggan(self):
        print(f"ID Pelanggan : {self.__idPelanggan}")
        print(f"Nama         : {self.__namaPelanggan}")
        print(f"No. Telepon  : {self.__noTelepon}")

    # Method menampilkan pesanan pelanggan
    def tampilkanInfoPesanan(self):
        if not self.__daftarPesanan:
            print("Belum ada pesanan aktif.")
        else:
            print("Daftar Pesanan:")
            for i, paket in enumerate(self.__daftarPesanan, 1):
                print(f"{i}. [ID {paket.getIdPaket()}] {paket.getNamaPaket()} - Rp {paket.getHargaPaket():,.0f}")
