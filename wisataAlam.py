# Subclass: WisataAlam
# Inheritance: Mewarisi class PaketWisata
from paketWisata import PaketWisata

class WisataAlam(PaketWisata):
    # Constructor berparameter
    def __init__(self, idPaket, namaPaket, hargaPaket, durasiPaket, lokasiPaket, kuotaPaket, fasilitasPaket,
                 jenisAktivitas, tingkatKesulitan, perlengkapanKhusus):
        # Memanggil constructor superclass
        super().__init__(idPaket, namaPaket, hargaPaket, durasiPaket, lokasiPaket, kuotaPaket, fasilitasPaket)
        
        # Enkapsulasi: atribut private khusus WisataAlam
        self.__jenisAktivitas = jenisAktivitas
        self.__tingkatKesulitan = tingkatKesulitan
        self.__perlengkapanKhusus = perlengkapanKhusus

    # Getter untuk atribut private
    def getJenisAktivitas(self):
        return self.__jenisAktivitas

    def getTingkatKesulitan(self):
        return self.__tingkatKesulitan

    def getPerlengkapanKhusus(self):
        return self.__perlengkapanKhusus

    # Method Overriding: Menampilkan informasi lengkap wisata alam
    def tampilkanInfoPaket(self):
        print("=== PAKET WISATA ALAM ===")
        super().tampilkanInfoPaket()
        print(f"Jenis Aktivitas: {self.__jenisAktivitas}")
        print(f"Tingkat Kesulitan: {self.__tingkatKesulitan}")
        print(f"Perlengkapan: {self.__perlengkapanKhusus}")

    # Method tambahan untuk mengecek tingkat kesulitan
    def cekTingkatKesulitan(self):
        kesulitan = self.__tingkatKesulitan.lower()
        if kesulitan == "mudah":
            print("Tingkat: Mudah (Cocok untuk pemula dan keluarga)")
        elif kesulitan == "sedang":
            print("Tingkat: Sedang (Memerlukan kondisi fisik yang fit)")
        elif kesulitan == "sulit":
            print("Tingkat: Sulit (Khusus untuk peserta berpengalaman)")
        else:
            print("Tingkat kesulitan belum diklasifikasikan.")

    # Method tambahan untuk mengubah jenis aktivitas
    def ubahJenisAktivitas(self, jenisBaru):
        self.__jenisAktivitas = jenisBaru
        print(f"Jenis aktivitas berhasil diubah menjadi: {self.__jenisAktivitas}")
