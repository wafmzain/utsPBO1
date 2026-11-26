# Superclass: PaketWisata
class PaketWisata:
    # Constructor berparameter
    def __init__(self, idPaket, namaPaket, hargaPaket, durasiPaket, lokasiPaket, kuotaPaket, fasilitasPaket):
        # Enkapsulasi: atribut private menggunakan prefix __
        self.__idPaket = idPaket
        self.__namaPaket = namaPaket
        self.__hargaPaket = hargaPaket
        self.__durasiPaket = durasiPaket
        self.__lokasiPaket = lokasiPaket
        self.__kuotaPaket = kuotaPaket
        self.__fasilitasPaket = fasilitasPaket

    # Getter untuk mengakses data private
    def getIdPaket(self):
        return self.__idPaket
    
    def getNamaPaket(self):
        return self.__namaPaket

    def getHargaPaket(self):
        return self.__hargaPaket

    def getDurasiPaket(self):
        return self.__durasiPaket

    def getLokasiPaket(self):
        return self.__lokasiPaket

    def getKuotaPaket(self):
        return self.__kuotaPaket

    def getFasilitasPaket(self):
        return self.__fasilitasPaket

    # Method menampilkan informasi dasar paket wisata
    def tampilkanInfoPaket(self):
        print(f"ID Paket: {self.__idPaket}")
        print(f"Nama Paket: {self.__namaPaket}")
        print(f"Lokasi: {self.__lokasiPaket}")
        print(f"Harga: Rp {self.__hargaPaket:,.0f}")
        print(f"Durasi: {self.__durasiPaket} Hari")
        print(f"Kuota: {self.__kuotaPaket} orang")
        print(f"Fasilitas: {self.__fasilitasPaket}")

    # Method untuk mengubah harga
    def ubahHargaPaket(self, hargaBaru):
        self.__hargaPaket = hargaBaru
        print(f"Harga paket {self.__namaPaket} berhasil diubah menjadi Rp {self.__hargaPaket:,.0f}.")

    # Method untuk mengubah fasilitas
    def ubahFasilitasPaket(self, fasilitasBaru):
        self.__fasilitasPaket = fasilitasBaru
        print(f"Fasilitas paket {self.__namaPaket} berhasil diubah.")

    # Method cek ketersediaan kuota
    def cekKuotaPaket(self):
        if self.__kuotaPaket > 0:
            print(f"Kuota paket {self.__namaPaket} tersedia: {self.__kuotaPaket} orang.")
            return True
        else:
            print(f"Kuota paket {self.__namaPaket} sudah habis.")
            return False

    # Method untuk mengurangi kuota saat ada pemesanan
    def kurangiKuota(self, jumlah=1):
        if self.__kuotaPaket >= jumlah:
            self.__kuotaPaket -= jumlah
            return True
        return False

    # Method untuk menambah kuota saat pesanan dibatalkan
    def tambahKuota(self, jumlah=1):
        self.__kuotaPaket += jumlah
