# Aplikasi Pengelolaan Paket Wisata (CLI)

Proyek ini dibuat untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah **Pemrograman Berorientasi Objek (PBO)**. Aplikasi berbasis Command Line Interface (CLI) menggunakan bahasa Python untuk mengelola data paket wisata, data pelanggan, serta transaksi pemesanan paket wisata.

**Identitas Mahasiswa:**
- **Nama:** Wafi Muhammad Zain
- **NIM:** 25552011290
- **Kelas:** TIF RP 25A

---

## Struktur Proyek

```text
UTS PBO/
├── main.py             # File utama program dan menu CLI interaktif
├── paketWisata.py      # Superclass PaketWisata
├── wisataAlam.py       # Subclass WisataAlam (turunan PaketWisata)
├── wisataBudaya.py     # Subclass WisataBudaya (turunan PaketWisata)
└── pelanggan.py        # Class Pelanggan (relasi asosiasi dengan PaketWisata)
```

---

## Penerapan Konsep OOP

1. **Class & Object**: Pemisahan entitas program ke dalam class `PaketWisata`, `WisataAlam`, `WisataBudaya`, dan `Pelanggan`.
2. **Constructor**: Setiap class memiliki constructor berparameter (`__init__`) untuk inisialisasi data awal saat object dibuat.
3. **Encapsulation**: Seluruh atribut pada class domain bersifat *private* (`__`) dengan akses melalui method *getter* dan pembaruan data melalui method khusus.
4. **Inheritance & Polymorphism**: `WisataAlam` dan `WisataBudaya` mewarisi atribut serta method dari `PaketWisata` menggunakan `super().__init__()`, serta menerapkan *method overriding* pada `tampilkanInfoPaket()`.
5. **Relasi Association**: Class `Pelanggan` dapat memesan satu atau lebih object `PaketWisata` yang disimpan di dalam list `__daftarPesanan`, lengkap dengan pembaruan kuota otomatis saat memesan atau membatalkan pesanan.

---

## Fitur Aplikasi

- **Kelola Paket Wisata**: Tambah paket (kategori Wisata Alam atau Wisata Budaya), tampilkan semua paket, cari berdasarkan ID, ubah harga/fasilitas, cek status & kuota paket, dan hapus paket.
- **Kelola Pelanggan**: Tambah data pelanggan, tampilkan seluruh pelanggan, cari pelanggan, dan ubah profil pelanggan.
- **Kelola Pemesanan**: Pemesanan paket wisata oleh pelanggan (otomatis mengurangi kuota paket), tampilkan daftar pemesanan, cek status pemesanan pelanggan, dan pembatalan pesanan (mengembalikan kuota paket).

---

## Coba Langsung (Google Colab)

Untuk mencoba menjalankan aplikasi langsung di browser tanpa perlu *clone* atau install Python di laptop, klik tombol di bawah ini lalu tekan tombol **Play (▶)**:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wafmzain/utsPBO1/blob/main/demo.ipynb)



