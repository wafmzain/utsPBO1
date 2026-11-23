#Class paketWisata
class paketWisata:
    def __init__(self, idPaket,namaPaket, hargaPaket, durasiPaket, lokasiPaket, kuotaPaket, fasilitasPaket):
        self.__idPaket = idPaket
        self.__namaPaket = namaPaket
        self.__lokasiPaket = lokasiPaket
        self.__hargaPaket = hargaPaket
        self.__durasiPaket = durasiPaket
        self.__kuotaPaket = kuotaPaket
        self.__fasilitasPaket = fasilitasPaket

    def getidPaket(self):
        return self.__idPaket
    
    def getnamaPaket(self):
        return self.__namaPaket

    def getlokasiPaket(self):
        return self.__lokasiPaket
    
    def gethargaPaket(self):
        return self.__hargaPaket

    def getdurasiPaket(self):
        return self.__durasiPaket

    def getkuotaPaket(self):
        return self.__kuotaPaket

    def getfasilitasPaket(self):
        return self.__fasilitasPaket

    def tampilkanInfoPaket(self):
        print(f"ID Paket: {self.__idPaket}")
        print(f"Nama Paket: {self.__namaPaket}")
        print(f"Lokasi Paket: {self.__lokasiPaket}")
        print(f"Harga Paket: {self.__hargaPaket}")
        print(f"Durasi Paket: {self.__durasiPaket}")
        print(f"Kuota Paket: {self.__kuotaPaket}")
        print(f"Fasilitas Paket: {self.__fasilitasPaket}")

    def ubahHargaPaket(self, hargaBaru):
        self.__hargaPaket = hargaBaru
        print(f"Harga paket {self.__namaPaket} berhasil diubah menjadi {self.__hargaPaket}.")

    def cekKuotaPaket(self):
        if self.__kuotaPaket > 0:
            print(f"Kuota paket {self.__namaPaket} tersedia: {self.__kuotaPaket} orang.")
        else:
            print(f"Kuota paket {self.__namaPaket} sudah habis.")

    def ubahFasilitasPaket(self, fasilitasBaru):
        self.__fasilitasPaket = fasilitasBaru
        print(f"Fasilitas paket {self.__namaPaket} berhasil diubah menjadi {self.__fasilitasPaket}.")