# Subclass: WisataBudaya
# Inheritance: Mewarisi class PaketWisata
from paketWisata import PaketWisata

class WisataBudaya(PaketWisata):
    # Constructor berparameter
    def __init__(self, idPaket, namaPaket, hargaPaket, durasiPaket, lokasiPaket, kuotaPaket, fasilitasPaket,
                 namaSitus, jenisBudaya, kegiatanBudaya):
        # Memanggil constructor superclass
        super().__init__(idPaket, namaPaket, hargaPaket, durasiPaket, lokasiPaket, kuotaPaket, fasilitasPaket)
        
        # Enkapsulasi: atribut private khusus WisataBudaya
        self.__namaSitus = namaSitus
        self.__jenisBudaya = jenisBudaya
        self.__kegiatanBudaya = kegiatanBudaya

    # Getter untuk atribut private
    def getNamaSitus(self):
        return self.__namaSitus

    def getJenisBudaya(self):
        return self.__jenisBudaya

    def getKegiatanBudaya(self):
        return self.__kegiatanBudaya

    # Method Overriding: Menampilkan informasi lengkap wisata budaya
    def tampilkanInfoPaket(self):
        print("=== PAKET WISATA BUDAYA ===")
        super().tampilkanInfoPaket()
        print(f"Nama Situs/Cagar: {self.__namaSitus}")
        print(f"Jenis Budaya: {self.__jenisBudaya}")
        print(f"Kegiatan: {self.__kegiatanBudaya}")

    # Method tambahan untuk menampilkan kegiatan budaya
    def tampilkanKegiatan(self):
        print(f"Agenda kegiatan budaya: {self.__kegiatanBudaya}")

    # Method tambahan untuk mengubah jenis budaya
    def ubahJenisBudaya(self, jenisBaru):
        self.__jenisBudaya = jenisBaru
        print(f"Jenis budaya berhasil diubah menjadi: {self.__jenisBudaya}")
