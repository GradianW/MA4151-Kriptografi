# MA4151 - Kriptografi

Repository kumpulan materi, slide perkuliahan, catatan/ringkasan, latihan soal, dan pembahasan tugas mata kuliah Kriptografi.

## Struktur Direktori

Struktur direktori disusun modular berdasarkan urutan topik perkuliahan:

- **`01 Kriptografi Klasik/`**
  - `slides/`: Slide perkuliahan (`1 Classical.pdf`).
  - `catatan/`: Ringkasan teori dan konsep cipher klasik.
  - `tugas-dan-latihan/`: Latihan soal dan implementasi.
- **`02 Kriptoanalisis/`**
  - `slides/`: Slide perkuliahan (`2 Kriptoanalisis.pdf`).
  - `catatan/`: Ringkasan metode analisis frekuensi, pengujian Kasiski, indeks koinsidensi, dll.
  - `tugas-dan-latihan/`: Dokumen tugas, sumber kode LaTeX (`Pembahasan_Tugas_Kriptoanalisis.tex`), dan hasil kompilasi PDF.
- **`03 Teori Shannon/`**
  - `slides/`: Slide perkuliahan (`3 Shannon.pdf`).
  - `catatan/` & `tugas-dan-latihan/`: Perfect secrecy, entropy, unicity distance.
- **`04 Teori Bilangan (PTB)/`**
  - `slides/`: Slide perkuliahan (`4 PTB.pdf`).
  - `catatan/` & `tugas-dan-latihan/`: Pembangkitan bilangan prima, algoritma Euclidean, Chinese Remainder Theorem (CRT), residu kuadratik.
- **`05 RSA/`**
  - `slides/`: Slide perkuliahan (`5 RSA.pdf`).
  - `catatan/` & `tugas-dan-latihan/`: Kriptografi kunci publik, skema enkripsi & dekripsi RSA.
- **`06 Faktorisasi/`**
  - `slides/`: Slide perkuliahan (`6 Faktorisasi.pdf`).
  - `catatan/` & `tugas-dan-latihan/`: Algoritma faktorisasi integer (Pollard rho, $p-1$, basis basis faktor).
- **`Past Problems/`**
  - Arsip soal dan pembahasan UTS, UAS, serta diskusi kelompok tahun-tahun sebelumnya.

---

## Catatan Tambahan (LaTeX & Git)
Repository ini telah dikonfigurasi dengan [`.gitignore`](.gitignore) untuk mengabaikan file cache/temporary LaTeX compiler (`*.aux`, `*.log`, `*.synctex.gz`, `*.fls`, dll.), sehingga hanya file sumber dokumen (`.tex`) dan hasil akhir (`.pdf`) yang dilacak oleh Git.
