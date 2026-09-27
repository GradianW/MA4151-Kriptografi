# 07 Block Cipher (DES & AES)

Modul pembelajaran mendalam mengenai kriptografi kunci simetris berbasis blok (*Block Cipher*), berfokus pada dua standar utama: **Data Encryption Standard (DES)** dan **Advanced Encryption Standard (AES / Rijndael)**.

Semua materi dan kode implementasi dalam folder ini dibangun **100% *from scratch* (Python Murni)** tanpa menggunakan pustaka (*library*) kriptografi *shortcut* pihak ketiga, sehingga pembaca dapat memahami mekanisme internal aljabar, manipulasi bit, dan permutasi.

---

## 📚 Daftar Isi dan Berkas

### 1. 📄 Dokumen Teori & Panduan Lengkap (PDF & LaTeX)
- **[`Panduan_Lengkap_DES_dan_AES.pdf`](Panduan_Lengkap_DES_dan_AES.pdf)**: Dokumen buku ajar / kompendium teori lengkap (14 halaman) mencakup:
  - Prinsip *Confusion* & *Diffusion* (Claude Shannon)
  - Arsitektur Jaringan Feistel vs *Substitution-Permutation Network* (SPN)
  - Detail spesifikasi DES: *Initial Permutation* ($IP$), *Key Schedule* ($PC\text{-}1$, *shifts*, $PC\text{-}2$), Fungsi Feistel $f$, 8 Kotak-S (*S-Boxes*), Permutasi $P$, dan analisis kelemahan ruang kunci $2^{56}$.
  - Detail spesifikasi AES-128: Aljabar Lapangan Terhingga (*Galois Field*) $GF(2^8)$, polinomial tak tereduksi $m(x) = x^8 + x^4 + x^3 + x + 1$, konstruksi aljabar S-Box via invers $GF(2^8)$ dan transformasi afina $\mathbb{F}_2$, 4 transformasi ronde (`SubBytes`, `ShiftRows`, `MixColumns`, `AddRoundKey`), serta *Key Expansion*.
  - Mode Operasi (*ECB*, *CBC*, *CTR*) dan skema padding PKCS#7.
  - Analisis Efek Salju (*Strict Avalanche Criterion* / SAC).
- **[`Panduan_Lengkap_DES_dan_AES.tex`](Panduan_Lengkap_DES_dan_AES.tex)**: Sumber kode LaTeX dokumen panduan.

---

### 2. 🧪 Jupyter Notebook Eksperimen (*From Scratch*)
- **[`01_DES_From_Scratch.ipynb`](01_DES_From_Scratch.ipynb)**:
  - Helper fungsi manipulasi bit (`bytes_to_bits`, `bits_to_bytes`, `permute`).
  - Tabel standar FIPS 46-3 ($IP, IP^{-1}, PC\text{-}1, PC\text{-}2, E, P, S_1 \dots S_8$).
  - Pembangkitan 16 subkunci ronde 48-bit.
  - Implementasi fungsi Feistel $f(R, K)$ dan 16 ronde enkripsi/dekripsi.
  - Validasi dengan **Vektor Uji Resmi NIST**.
  - Eksperimen grafik efek salju (*avalanche effect*) perubahan 1 bit.

- **[`02_AES_From_Scratch.ipynb`](02_AES_From_Scratch.ipynb)**:
  - Aritmetika Galois Field $GF(2^8)$: `gf_add`, `xtime`, `gf_mult` (*Russian Peasant*), dan `gf_inv` ($a^{254} \bmod m(x)$).
  - Pembangkitan S-Box dan Inverse S-Box secara aljabar murni tanpa tabel *hardcoded*.
  - Transformasi State Matrix $4 \times 4$: `SubBytes`, `ShiftRows`, `MixColumns` (perkalian matriks MDS), dan `AddRoundKey`.
  - *Key Expansion* AES-128 (`RotWord`, `SubWord`, `Rcon`).
  - Validasi dengan **Vektor Uji Resmi NIST FIPS-197 (Appendix B & C)**.
  - Eksperimen difusi kilat AES (*Wide Trail Strategy*).

- **[`03_Mode_Operasi_dan_Eksperimen_Lanjutan.ipynb`](03_Mode_Operasi_dan_Eksperimen_Lanjutan.ipynb)**:
  - Padding & Unpadding PKCS#7 *from scratch*.
  - Mode **ECB** (*Electronic Codebook*) beserta visualisasi kelemahan pola identik.
  - Mode **CBC** (*Cipher Block Chaining*) dengan $IV$ acak.
  - Mode **CTR** (*Counter Mode*) dan pemanfaatan block cipher sebagai stream cipher paralel.
  - Eksperimen propagasi kesalahan transmisi (*error propagation analysis*).
  - Matriks perbandingan menyeluruh DES vs AES.

---

## 🚀 Cara Menjalankan Eksperimen

Anda dapat membuka dan menjalankan setiap *notebook* di lingkungan Jupyter:
```bash
jupyter notebook
```
Buka file `01_DES_From_Scratch.ipynb`, `02_AES_From_Scratch.ipynb`, atau `03_Mode_Operasi_dan_Eksperimen_Lanjutan.ipynb` untuk mulai bereksperimen!
