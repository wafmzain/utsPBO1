#class wisata alam
class WisataAlam:
    def __init__(self, jenisAktivitas, tingkatKesulitan, lokasiAlam):
        self.jenisAktivitas = jenisAktivitas
        self.tingkatKesulitan = tingkatKesulitan
        self.lokasiAlam = lokasiAlam

    def tampilkanAktivitas(self):
        print(f"Jenis Aktivitas: {self.jenisAktivitas}")
        print(f"Tingkat Kesulitan: {self.tingkatKesulitan}")
        print(f"Lokasi Alam: {self.lokasiAlam}")

    def cekTingkatKesulitan(self):
        if self.tingkatKesulitan.lower() == "mudah":
            print("Aktivitas ini cocok untuk pemula.")
        elif self.tingkatKesulitan.lower() == "sedang":
            print("Aktivitas ini cocok untuk tingkat menengah.")
        elif self.tingkatKesulitan.lower() == "sulit":
            print("Aktivitas ini cocok untuk tingkat mahir.")
        else:
            print("Tingkat kesulitan tidak valid.")

    def ubahJenisAktivitas(self, jenisBaru):
        self.jenisAktivitas = jenisBaru
        print(f"Jenis aktivitas berhasil diubah menjadi {self.jenisAktivitas}.")
        
