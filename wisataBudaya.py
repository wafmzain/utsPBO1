#class wisataBudaya
class WisataBudaya:
    def __init__(self, namaBudaya, jenisBudaya, kegiatanBudaya):
        self.nama = namaBudaya
        self.jenis = jenisBudaya
        self.kegiatan = kegiatanBudaya

    def get_namaBudaya(self):
        return self.nama

    def getJenisBudaya(self):
        return self.jenis

    def getKegiatanBudaya(self):
        return self.kegiatan

    def tampilkanBudaya(self):
        print(f"Nama Wisata Budaya: {self.nama}")
        print(f"Jenis Budaya: {self.jenis}")
        print(f"Kegiatan Budaya: {self.kegiatan}")

    def tampilkanKegiatan(self):
        print(f"Kegiatan Budaya: {self.kegiatan}")

    def ubahJenisBudaya(self, jenisBaru):
        self.jenis = jenisBaru
        print(f"Jenis budaya berhasil diubah menjadi {self.jenis}.")