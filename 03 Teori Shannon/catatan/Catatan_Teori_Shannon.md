# Catatan Teori Shannon (Shannon's Theory of Secrecy Systems)

Berdasarkan slide perkuliahan **MA4151 Kriptografi** (Topik 3: *Teori Shannon*), disarikan dari karya monumental Claude Shannon (1949, *"Communication Theory of Secrecy Systems"*).

---

## 🗺️ Peta Konsep & Struktur Topik

Materi bab ini tersusun dalam 5 pilar utama yang saling berhubungan secara logis:

```
[1. Keamanan Sistem Kripto & Teori Peluang]
          │
          ├─ Computational vs Unconditional Security
          ├─ Perfect Secrecy (Shannon Theorem 3: |K| = |C| = |P|)
          │
          ▼
[2. Entropi & Teori Informasi]
          │
          ├─ Ukuran ketidakpastian / informasi: H(X) = - Σ p(x) log2 p(x)
          ├─ Kaitan dengan kompresi & Prefix-Free (Huffman Coding)
          │
          ▼
[3. Sifat-Sifat Matematika Entropi]
          │
          ├─ Ketaksamaan Jensen & Kecekungan log2(x)
          ├─ H(X) ≤ log2(n) (Maksimum saat seragam)
          ├─ Joint & Conditional Entropy: H(X, Y) = H(Y) + H(X|Y) ≤ H(X) + H(Y)
          │
          ▼
[4. Kunci Palsu (Spurious Keys) & Unicity Distance]
          │
          ├─ Key Equivocation: H(K|C) = H(K) + H(P) - H(C)
          ├─ Entropi Bahasa (HL) & Redundansi (RL = 1 - HL / log2|P|)
          ├─ Rata-rata Kunci Palsu (s_n)
          ├─ Jarak Unicity: n0 ≈ log2|K| / (RL * log2|P|)
          │
          ▼
[5. Sistem Kripto Perkalian (Product Ciphers)]
          │
          ├─ Komposisi Cipher Endomorfik: S1 × S2
          ├─ Komutatif & Asosiatif
          ├─ Idempoten (S^2 = S) vs Non-Idempoten (Dasar DES / SPN modern)
```

---

## Bagian 1: Keamanan Sempurna (*Perfect Secrecy*)

### 1.1 Klasifikasi Keamanan Sistem Kripto
Terdapat dua pendekatan utama dalam menilai keamanan cipher:
1. **Keamanan Komputasi (*Computational Security*)**:
   - Didasarkan pada besarnya usaha komputasi (*computational effort*) yang diperlukan penyerang.
   - Suatu sistem dikatakan aman secara komputasi jika algoritma pemecahan terbaik membutuhkan sedikitnya $N$ langkah operasi di mana $N$ sangat besar (*unreasonably large amount of computer time*).
   - Pendekatan alternatif: **Reduksi keamanan** ke persoalan matematika yang terbukti sulit (misalnya kesulitan faktorisasi integer besar pada RSA).
2. **Keamanan Tanpa Syarat (*Unconditional Security*)**:
   - Keamanan yang tetap bertahan **meskipun musuh memiliki sumber daya komputasi dan waktu tak terbatas**.
   - Analisis keamanan tanpa syarat tidak menggunakan teori kompleksitas, melainkan menggunakan **teori peluang**.

### 1.2 Model Peluang Sistem Kriptografi
Misalkan:
- $\mathcal{P}$: Ruang kata-asal (*plaintext*), dengan distribusi peluang $p_{\mathcal{P}}(x)$.
- $\mathcal{C}$: Ruang kata-sandi (*ciphertext*), dengan distribusi peluang $p_{\mathcal{C}}(y)$.
- $\mathcal{K}$: Ruang kunci (*key*), dengan distribusi peluang $p_{\mathcal{K}}(K)$.

Kunci $K$ dan plaintext $x$ diasumsikan independen (saling bebas) karena kunci dibangkitkan sebelum teks asal diketahui.

Distribusi marginal ciphertext $y$:
$$p_{\mathcal{C}}(y) = \sum_{\{K : y \in C(K)\}} p_{\mathcal{K}}(K) \cdot p_{\mathcal{P}}(d_K(y))$$

Peluang bersyarat ciphertext jika plaintext diberikan:
$$p_{\mathcal{C}}(y|x) = \sum_{\{K : x = d_K(y)\}} p_{\mathcal{K}}(K)$$

Dengan **Teorema Bayes**, peluang penyerang menebak plaintext $x$ setelah mengamati ciphertext $y$:
$$p(x|y) = \frac{p_{\mathcal{P}}(x) \cdot p_{\mathcal{C}}(y|x)}{p_{\mathcal{C}}(y)} = \frac{p_{\mathcal{P}}(x) \sum_{\{K : x = d_K(y)\}} p_{\mathcal{K}}(K)}{\sum_{\{K : y \in C(K)\}} p_{\mathcal{K}}(K) p_{\mathcal{P}}(d_K(y))}$$

### 1.3 Definisi Keamanan Sempurna
> **Definisi:**
> Suatu sistem kripto memiliki **keamanan sempurna (*perfect secrecy*)** jika untuk setiap $x \in \mathcal{P}$ dan $y \in \mathcal{C}$:
> $$p_{\mathcal{P}}(x|y) = p_{\mathcal{P}}(x)$$
> *(Mengetahui ciphertext $y$ sama sekali tidak memberikan informasi tambahan mengenai plaintext $x$. Peluang a posteriori sama dengan peluang a priori).*

Ekivalen dengan pernyataan:
$$p_{\mathcal{C}}(y|x) = p_{\mathcal{C}}(y) \quad \text{untuk setiap } x \in \mathcal{P}, y \in \mathcal{C}$$

### 1.4 Teorema Shannon Mengenai Keamanan Sempurna
1. **Konsekuensi Ukuran Ruang Kunci**:
   Jika suatu sistem memiliki perfect secrecy, maka harus berlaku:
   $$|\mathcal{K}| \ge |\mathcal{C}| \ge |\mathcal{P}|$$
   *(Jumlah kemungkinan kunci minimal sebanyak jumlah teks sandi / teks asli).*

2. **Teorema Shannon (Theorem 3 di slide)**:
   Misalkan $(\mathcal{P}, \mathcal{C}, \mathcal{K}, \mathcal{E}, \mathcal{D})$ adalah sistem kripto dengan $|\mathcal{K}| = |\mathcal{C}| = |\mathcal{P}|$. Sistem ini memenuhi *perfect secrecy* **jika dan hanya jika**:
   1. Setiap kunci dipilih dengan peluang seragam:
      $$p_{\mathcal{K}}(K) = \frac{1}{|\mathcal{K}|}$$
   2. Untuk setiap pasangan $x \in \mathcal{P}$ dan $y \in \mathcal{C}$, terdapat tepat **satu kunci unik** $K$ sehingga $e_K(x) = y$.

**Contoh Riil**:
- **Sandi Geser (Shift Cipher)** pada satu karakter: Jika 26 kunci dipilih dengan probabilitas sama ($1/26$), sistem memenuhi perfect secrecy.
- **One-Time Pad (Vernam Cipher)**: Realisasi praktis paling terkenal untuk string biner panjang arbitrary, di mana kunci dibangkitkan benar-benar acak, panjangnya sama dengan panjang pesan, dan hanya digunakan sekali.

---

## Bagian 2: Entropi & Teori Informasi

Jika satu kunci digunakan berulang kali untuk mengenkripsi banyak pesan, bagaimana penyerang mengeksploitasinya? Shannon menjawab ini menggunakan konsep **Entropi** (1948).

### 2.1 Definisi Entropi
Entropi adalah ukuran rata-rata ketidakpastian atau informasi dari suatu variabel acak diskret $X$:
$$H(X) = - \sum_{i=1}^n p_i \log_2 p_i = \sum_{i=1}^n p_i \log_2 \left(\frac{1}{p_i}\right)$$
*(Diukur dalam satuan bit jika menggunakan logaritma basis 2).*

- Jika $p_i = 1$ untuk suatu nilai dan 0 untuk yang lain (kejadian pasti): $H(X) = 0$ (tidak ada ketidakpastian).
- Jika semua kejadian berdistribusi seragam ($p_i = 1/n$): $H(X) = \log_2 n$ (ketidakpastian maksimum).

### 2.2 Entropi dan Huffman Coding
- Panjang representasi bit optimal untuk simbol berpeluang $p$ adalah sekitar $-\log_2 p$.
- Panjang rata-rata berbobot encoding $f$:
  $$l(f) = \sum_{x \in X} p(x)|f(x)|$$
- Kode dengan sifat **prefix-free** (tidak ada kata sandi yang menjadi awalan kata sandi lain) dapat didekode seketika (*instantaneous decoding*) tanpa ambigu.
- **Algoritma Huffman** menghasilkan kode prefix-free optimal dengan batas panjang rata-rata:
  $$H(X) \le l(f) < H(X) + 1$$

---

## Bagian 3: Sifat-Sifat Matematis Entropi

### 3.1 Alat Analisis: Ketaksamaan Jensen
Karena fungsi $f(t) = \log_2 t$ merupakan fungsi cekung tegas (*strictly concave*) pada interval $(0, \infty)$, menurut **Ketaksamaan Jensen**:
$$\sum_{i=1}^n a_i f(x_i) \le f\left(\sum_{i=1}^n a_i x_i\right) \quad \left(\text{dengan } \sum a_i = 1, a_i > 0\right)$$
Kesamaan berlaku jika dan hanya jika $x_1 = x_2 = \dots = x_n$.

### 3.2 Teorema Batas Entropi
1. **Batas Maksimum Entropi**:
   $$H(X) \le \log_2 n$$
   Kesamaan berlaku jika dan hanya jika distribusi seragam ($p_i = 1/n$).

2. **Entropi Bersama (*Joint Entropy*)**:
   $$H(X, Y) = -\sum_{x}\sum_{y} p(x,y) \log_2 p(x,y)$$
   Sifat subaditivitas:
   $$H(X, Y) \le H(X) + H(Y)$$
   Kesamaan berlaku jika dan hanya jika $X$ dan $Y$ saling bebas (*independen*).

3. **Entropi Bersyarat (*Conditional Entropy*)**:
   $$H(X|Y) = \sum_{y} p(y) H(X|y) = -\sum_{y}\sum_{x} p(y)p(x|y) \log_2 p(x|y)$$
   - Menghubungkan joint entropy:
     $$H(X, Y) = H(Y) + H(X|Y) = H(X) + H(Y|X)$$
   - *Conditioning reduces entropy* (observasi tidak pernah menambah ketidakpastian rata-rata):
     $$H(X|Y) \le H(X)$$
     dengan kesamaan berlaku j.h.j $X$ dan $Y$ independen.

---

## Bagian 4: Kunci Palsu (*Spurious Keys*) & Jarak Unicity (*Unicity Distance*)

### 4.1 Key Equivocation
Dalam sistem kripto, ketidakpastian kunci setelah musuh mengamati ciphertext disebut **Key Equivocation** $H(K|C)$:
$$H(K|C) = H(K) + H(P) - H(C)$$

*Bukti singkat*:
- Kunci $K$ dan plaintext $P$ menentukan ciphertext $C$ secara deterministik, sehingga $H(C|K, P) = 0 \implies H(K, P, C) = H(K, P) = H(K) + H(P)$.
- Kunci $K$ dan ciphertext $C$ juga menentukan plaintext $P$ secara tunggal, sehingga $H(P|K, C) = 0 \implies H(K, P, C) = H(K, C)$.
- Maka: $H(K|C) = H(K, C) - H(C) = H(K) + H(P) - H(C)$.

### 4.2 Entropi Bahasa dan Redundansi
Teks alami (seperti bahasa Inggris atau Indonesia) bukanlah karakter acak murni, melainkan memiliki korelasi struktural ($n$-gram).
- **Entropi per huruf dari bahasa alami $L$**:
  $$H_L = \lim_{n \to \infty} \frac{H(P^n)}{n}$$
  Untuk bahasa Inggris: huruf acak ber-entropi $\log_2 26 \approx 4.70\text{ bit/huruf}$. Namun, melalui eksperimen statistik $n$-gram, $H_L \approx 1.0 - 1.5\text{ bit/huruf}$ (diambil rata-rata $\approx 1.25\text{ bit/huruf}$).
- **Redundansi Bahasa ($R_L$)**:
  $$R_L = 1 - \frac{H_L}{\log_2 |P|}$$
  Untuk bahasa Inggris: $R_L \approx 1 - \frac{1.25}{4.70} \approx 0.75$ ($75\%$ redundan).

### 4.3 Kunci Palsu (*Spurious Keys*)
Misalkan ciphertext sepanjang $n$ karakter dihasilkan dari satu kunci. Musuh dengan daya komputasi tak hingga mencoba semua kunci:
- Kunci yang menghasilkan teks terbaca (*meaningful*) disebut kandidat kunci.
- Karena hanya ada **1 kunci yang benar**, kunci-kunci lain yang juga menghasilkan teks bermakna disebut **kunci palsu (*spurious keys*)**.
- Himpunan kunci konsisten untuk ciphertext $y \in \mathcal{C}^n$:
  $$K(y) = \{K \in \mathcal{K} : \exists x \in \mathcal{P}^n, p(x) > 0, e_K(x) = y\}$$
  Jumlah kunci palsu untuk ciphertext $y$: $|K(y)| - 1$.
- **Rata-rata banyaknya kunci palsu ($\bar{s}_n$)**:
  $$\bar{s}_n = \sum_{y \in \mathcal{C}^n} p(y)|K(y)| - 1 \ge \frac{|\mathcal{K}|}{|\mathcal{P}|^{n \cdot R_L}} - 1$$

Ketika $n$ bertambah besar, penyebut $|\mathcal{P}|^{n R_L}$ melonjak eksponensial, sehingga $\bar{s}_n \to 0$.

### 4.4 Jarak Unicity (*Unicity Distance*)
> **Definisi:**
> **Jarak Unicity ($n_0$)** adalah panjang minimum ciphertext yang diperlukan oleh kriptanalis agar rata-rata jumlah kunci palsu berkurang mendekati 0 ($\bar{s}_n = 0$). Artinya, kunci dapat ditentukan secara unik (*tunggal*).

Dengan menyamakan $\bar{s}_n = 0$:
$$\frac{|\mathcal{K}|}{|\mathcal{P}|^{n_0 R_L}} \approx 1 \implies \log_2 |\mathcal{K}| - n_0 R_L \log_2 |\mathcal{P}| \approx 0$$
Diperoleh rumus **Jarak Unicity**:
$$n_0 \approx \frac{\log_2 |\mathcal{K}|}{R_L \log_2 |\mathcal{P}|}$$

**Contoh Penerapan pada Monoalphabetic Substitution Cipher**:
- Alphabet alfabetik standar: $|\mathcal{P}| = 26 \implies \log_2 26 \approx 4.70$.
- Ruang kunci: $|\mathcal{K}| = 26! \implies \log_2 (26!) \approx 88.4\text{ bit}$.
- Redundansi bahasa Inggris: $R_L \approx 0.75$.
$$n_0 \approx \frac{88.4}{0.75 \times 4.70} \approx 25 \text{ karakter}$$
*Kesimpulan*: Ciphertext substitusi sepanjang $\ge 25$ karakter secara teoretis sudah cukup untuk menentukan kunci secara unik tanpa ada kunci palsu.

---

## Bagian 5: Sistem Kripto Perkalian (*Product Ciphers*)

### 5.1 Cipher Endomorfik & Definisi Perkalian
Sistem kripto disebut **endomorfik** jika ruang pesan sama dengan ruang sandi ($\mathcal{C} = \mathcal{P}$).

Jika $S_1 = (\mathcal{P}, \mathcal{P}, \mathcal{K}_1, \mathcal{E}_1, \mathcal{D}_1)$ dan $S_2 = (\mathcal{P}, \mathcal{P}, \mathcal{K}_2, \mathcal{E}_2, \mathcal{D}_2)$ dua cipher endomorfik, perkalian $S_1 \times S_2$ didefinisikan sebagai komposisi:
- Ruang kunci: $\mathcal{K} = \mathcal{K}_1 \times \mathcal{K}_2$ dengan $p(K_1, K_2) = p(K_1) \cdot p(K_2)$.
- Enkripsi berantai: $e_{(K_1, K_2)}(x) = e_{K_2}(e_{K_1}(x))$.
- Dekripsi berantai: $d_{(K_1, K_2)}(y) = d_{K_1}(d_{K_2}(y))$.

### 5.2 Sifat-Sifat Aljabar Sistem Perkalian
1. **Asosiatif**: Selalu berlaku untuk semua sistem kripto: $(S_1 \times S_2) \times S_3 = S_1 \times (S_2 \times S_3)$.
2. **Komutatif**: Umumnya tidak komutatif ($S_1 \times S_2 \neq S_2 \times S_1$), tetapi ada pasangan tertentu yang komutatif:
   - Contoh: Sandi Perkalian/Multiplikatif ($M$) dan Sandi Geser ($S$) bersifat komutatif:
     $$M \times S = S \times M = \text{Sandi Affine}$$
3. **Idempoten**:
   Suatu cipher $S$ dikatakan **idempoten** jika:
   $$S^2 = S \times S = S$$
   - Jika suatu cipher idempoten, mengenkripsinya berkali-kali menggunakan kunci berbeda **tidak menambah keamanan sama sekali** karena ekivalen dengan satu kali enkripsi dengan kunci baru.
   - **Contoh cipher idempoten**: Sandi Geser, Substitusi Monoalfabetik, Affine, Hill Cipher, Vigenère, dan Permutasi.

### 5.3 Signifikansi untuk Kriptografi Modern (DES & SPN)
Jika sistem kripto **tidak idempoten** ($S^2 \neq S$), iterasi perkalian:
$$S^k \quad (k \ge 2)$$
berpotensi **meningkatkan kekuatan keamanan secara drastis**.

Konsep Shannon ini menjadi fondasi langsung arsitektur cipher modern:
- **Substitution-Permutation Network (SPN)**: Mengombinasikan komponen substitusi non-linear (S-Box / *confusion*) dan transposisi linear (P-Box / *diffusion*).
- **Data Encryption Standard (DES)** dan **AES**: Menerapkan konsep perkalian sistem tak-idempoten dengan melakukan iterasi ronde (16 ronde pada DES, 10-14 ronde pada AES).

---

## 📌 Ringkasan Rumus Kunci Ujian / Review Cepat

| Parameter / Konsep | Rumus Matematis | Keterangan |
| :--- | :--- | :--- |
| **Keamanan Sempurna** | $p(x\|y) = p(x)$ atau $p(y\|x) = p(y)$ | Informasi ciphertext tidak membocorkan plaintext |
| **Syarat Shannon** | $|\mathcal{K}\| \ge \|\mathcal{C}\| \ge \|\mathcal{P}\|$ dan $p(K) = \frac{1}{\|\mathcal{K}\|}$ | Setiap pasangan $(x, y)$ memiliki kunci unik tunggal |
| **Entropi** | $H(X) = -\sum p_i \log_2 p_i$ | Satuan bit, bernilai maksimum jika seragam |
| **Joint Entropy** | $H(X, Y) = H(Y) + H(X\|Y) \le H(X) + H(Y)$ | Kesamaan tercapai j.h.j $X, Y$ independen |
| **Key Equivocation** | $H(K\|C) = H(K) + H(P) - H(C)$ | Ketidakpastian kunci setelah observasi sandi |
| **Redundansi Bahasa** | $R_L = 1 - \frac{H_L}{\log_2 \|\mathcal{P}\|}$ | Untuk bhs. Inggris $\approx 0.75$ |
| **Ekspektasi Kunci Palsu** | $\bar{s}_n \ge \frac{\|\mathcal{K}\|}{\|\mathcal{P}\|^{n \cdot R_L}} - 1$ | Mendekati 0 saat panjang ciphertext $n$ membesar |
| **Jarak Unicity** | $n_0 \approx \frac{\log_2 \|\mathcal{K}\|}{R_L \log_2 \|\mathcal{P}\|}$ | Panjang ciphertext agar kunci dapat dipastikan unik |
| **Cipher Idempoten** | $S^2 = S$ | Iterasi berganda tidak menambah keamanan |
