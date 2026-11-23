class pelanggan:
    def __init__(self, idPelanggan, namaPelanggan, no_telepon, daftarPesanan):
        self.idPelanggan = idPelanggan
        self.namaPelanggan = namaPelanggan
        self.no_telepon = no_telepon
        self.daftarPesanan = daftarPesanan

    def pesanPaket(self, paketWisata):
        self.daftarPesanan.append(paketWisata)

    def batalkanPesanan(self, paketWisata):
        if paketWisata in self.daftarPesanan:
            self.daftarPesanan.remove(paketWisata)
            print(f"Pesanan paket {paketWisata.getnamaPaket()} berhasil dibatalkan.")
        else:
            print(f"Pesanan paket {paketWisata.getnamaPaket()} tidak ditemukan.")

    def tampilkanInfoPesanan(self):
        if not self.daftarPesanan:
            print("Tidak ada pesanan yang ditemukan.")
        else:
            print("Daftar Pesanan:")
            for pesanan in self.daftarPesanan:
                print(f"- {pesanan.getnamaPaket()} (ID: {pesanan.getidPaket()})")

    def tampilkanInfo(self):
        print(f"ID Pelanggan: {self.idPelanggan}")
        print(f"Nama: {self.namaPelanggan}")
        print(f"No Telepon: {self.no_telepon}")
        print("Daftar Pesanan:")
        for pesanan in self.daftarPesanan:
            print(f"- {pesanan.getnamaPaket()} (ID: {pesanan.getidPaket()})")
