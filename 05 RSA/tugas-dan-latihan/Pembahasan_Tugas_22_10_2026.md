# TUGAS MA4151 KRIPTOGRAFI
**Topik:** Residu Kuadrat, Kriteria Euler, dan Simbol Legendre  
**Tanggal:** 22 Oktober 2026  
**Format Dokumen:** Lembar Pengerjaan PR / Solusi Lengkap Rinci

---

## Ringkasan Teori Dasar yang Digunakan

1. **Definisi Residu Kuadrat (QR):**  
   Misalkan $p$ bilangan prima ganjil dan $\gcd(a, p) = 1$. Bilangan $a$ disebut *residu kuadrat* (quadratic residue, QR) modulo $p$ jika terdapat bilangan bulat $x$ sehingga:
   $$x^2 \equiv a \pmod p$$
   Jika tidak ada $x$ yang memenuhi, maka $a$ disebut *bukan residu kuadrat* (quadratic non-residue, QNR) modulo $p$.

2. **Simbol Legendre:**  
   Untuk bilangan prima ganjil $p$ dan sembarang bilangan bulat $a$:
   $$\left(\frac{a}{p}\right) = \begin{cases} 
   1, & \text{jika } a \text{ adalah residu kuadrat modulo } p \text{ dan } p \nmid a \\
   -1, & \text{jika } a \text{ bukan residu kuadrat modulo } p \\
   0, & \text{jika } p \mid a
   \end{cases}$$

3. **Kriteria Euler (Euler's Criterion):**  
   Untuk sembarang bilangan prima ganjil $p$ dan bilangan bulat $a$ dengan $\gcd(a, p) = 1$:
   $$\left(\frac{a}{p}\right) \equiv a^{\frac{p-1}{2}} \pmod p$$

---

## PEMBAHASAN SOAL

---

### Soal 1
> **Gunakan kriteria Euler untuk menentukan apakah $5$ residu kuadrat modulo $11$. Jika ya, tentukan semua $x$ dengan $x^2 \equiv 5 \pmod{11}$.**

#### Langkah 1: Menerapkan Kriteria Euler
Diketahui:
- $p = 11$ (prima ganjil)
- $a = 5$
- Eksponen: $\frac{p-1}{2} = \frac{11-1}{2} = 5$

Kita hitung nilai $5^5 \pmod{11}$:
$$\begin{aligned}
5^1 &\equiv 5 \pmod{11} \\
5^2 &= 25 = 2 \times 11 + 3 \equiv 3 \pmod{11} \\
5^4 &= (5^2)^2 \equiv 3^2 = 9 \equiv -2 \pmod{11} \\
5^5 &= 5^4 \times 5^1 \equiv (-2) \times 5 = -10 \equiv 1 \pmod{11}
\end{aligned}$$

Karena:
$$5^{\frac{11-1}{2}} = 5^5 \equiv 1 \pmod{11}$$
maka menurut kriteria Euler:
$$\left(\frac{5}{11}\right) = 1$$
**Kesimpulan 1:** $5$ adalah **residu kuadrat** modulo $11$.

#### Langkah 2: Menentukan Semua Solusi $x^2 \equiv 5 \pmod{11}$
Kita mencari $x \in \{0, 1, 2, \ldots, 10\}$ yang memenuhi $x^2 \equiv 5 \pmod{11}$:
- $1^2 = 1 \not\equiv 5$
- $2^2 = 4 \not\equiv 5$
- $3^2 = 9 \not\equiv 5$
- $4^2 = 16 = 11 + 5 \equiv 5 \pmod{11}$ $\quad \checkmark$ (Solusi pertama: $x_1 = 4$)

Karena $\mathbb{Z}_{11}$ adalah lapangan, solusi kuadratik modulo prima tepat memiliki dua akar yang saling aditif invers:
$$x_2 \equiv -x_1 \equiv -4 \equiv 11 - 4 = 7 \pmod{11}$$

**Verifikasi:**
$$7^2 = 49 = 4 \times 11 + 5 \equiv 5 \pmod{11} \quad \checkmark$$

**Jawaban Akhir Soal 1:**  
$5$ adalah residu kuadrat modulo $11$, dan himpunan semua solusinya adalah:
$$x \equiv 4 \pmod{11} \quad \text{dan} \quad x \equiv 7 \pmod{11}$$

---

### Soal 2
> **Tentukan apakah $7$ residu kuadrat modulo $19$. (*Petunjuk: hitung $7^3 \bmod 19$ lebih dulu.*) Jika ya, carilah akarnya.**

#### Langkah 1: Menghitung $7^3 \pmod{19}$ sesuai Petunjuk
- $7^1 \equiv 7 \pmod{19}$
- $7^2 = 49 = 2 \times 19 + 11 \equiv 11 \equiv -8 \pmod{19}$
- $7^3 = 7^2 \times 7 \equiv 11 \times 7 = 77$
  Karena $77 = 4 \times 19 + 1 = 76 + 1$, maka:
  $$7^3 \equiv 1 \pmod{19}$$

#### Langkah 2: Menguji dengan Kriteria Euler
Untuk $p = 19$, eksponen pada kriteria Euler adalah:
$$\frac{p-1}{2} = \frac{19-1}{2} = 9$$
Dengan memanfaatkan hasil $7^3 \equiv 1 \pmod{19}$:
$$7^9 = (7^3)^3 \equiv 1^3 \equiv 1 \pmod{19}$$
Karena $7^{\frac{19-1}{2}} \equiv 1 \pmod{19}$, maka:
$$\left(\frac{7}{19}\right) = 1$$
**Kesimpulan 1:** $7$ adalah **residu kuadrat** modulo $19$.

#### Langkah 3: Mencari Akar dari $x^2 \equiv 7 \pmod{19}$
Kita dapat memanfaatkan petunjuk $7^3 \equiv 1 \pmod{19}$ secara aljabar:
$$7 \equiv 7 \times 1 \equiv 7 \times 7^3 = 7^4 = (7^2)^2 \pmod{19}$$
Artinya:
$$x \equiv \pm 7^2 \pmod{19}$$
Kita hitung nilainya:
$$x_1 \equiv 7^2 = 49 \equiv 11 \pmod{19}$$
Akar kedua:
$$x_2 \equiv -x_1 \equiv -11 \equiv 19 - 11 = 8 \pmod{19}$$

**Verifikasi:**
- $11^2 = 121 = 6 \times 19 + 7 = 114 + 7 \equiv 7 \pmod{19} \quad \checkmark$
- $8^2 = 64 = 3 \times 19 + 7 = 57 + 7 \equiv 7 \pmod{19} \quad \checkmark$

**Jawaban Akhir Soal 2:**  
$7$ adalah residu kuadrat modulo $19$. Akarnya adalah:
$$x \equiv 8 \pmod{19} \quad \text{dan} \quad x \equiv 11 \pmod{19}$$

---

### Soal 3
> **Tentukan apakah $2, 3,$ dan $6$ residu kuadrat modulo $17$. Hitung $2^8$ dan $3^8$ saja, lalu simpulkan nilai untuk $6$ tanpa menghitung $6^8$.**

Diketahui: $p = 17$, sehingga $\frac{p-1}{2} = \frac{17-1}{2} = 8$.

#### Langkah 1: Menghitung $2^8 \pmod{17}$
$$\begin{aligned}
2^4 &= 16 \equiv -1 \pmod{17} \\
2^8 &= (2^4)^2 \equiv (-1)^2 = 1 \pmod{17}
\end{aligned}$$
Karena $2^8 \equiv 1 \pmod{17}$, maka:
$$\left(\frac{2}{17}\right) = 1 \implies \mathbf{2 \text{ adalah residu kuadrat modulo } 17}.$$

#### Langkah 2: Menghitung $3^8 \pmod{17}$
$$\begin{aligned}
3^2 &= 9 \\
3^4 &= 9^2 = 81 = 4 \times 17 + 13 \equiv 13 \equiv -4 \pmod{17} \\
3^8 &= (3^4)^2 \equiv (-4)^2 = 16 \equiv -1 \pmod{17}
\end{aligned}$$
Karena $3^8 \equiv -1 \pmod{17}$, maka:
$$\left(\frac{3}{17}\right) = -1 \implies \mathbf{3 \text{ bukan residu kuadrat modulo } 17}.$$

#### Langkah 3: Menyimpulkan Nilai untuk $6$ Tanpa Menghitung $6^8$
Karena $6 = 2 \times 3$, menurut sifat multiplikatif simbol Legendre:
$$\left(\frac{6}{17}\right) = \left(\frac{2 \times 3}{17}\right) = \left(\frac{2}{17}\right) \times \left(\frac{3}{17}\right)$$
Substitusikan hasil dari Langkah 1 dan 2:
$$\left(\frac{6}{17}\right) = (1) \times (-1) = -1$$
*(Atau melalui perpangkatan: $6^8 = (2 \times 3)^8 = 2^8 \times 3^8 \equiv 1 \times (-1) = -1 \pmod{17}$).*

**Jawaban Akhir Soal 3:**  
- $2$ adalah **residu kuadrat** modulo $17$.
- $3$ adalah **bukan residu kuadrat** modulo $17$.
- $6$ adalah **bukan residu kuadrat** modulo $17$.

---

### Soal 4
> **Hitung $\left(\frac{10}{23}\right)$ menggunakan kriteria Euler dengan teknik kuadrat berulang ($10^2, 10^4, 10^8, \ldots$).**

Diketahui: $p = 23$.  
Eksponen Kriteria Euler:
$$\frac{p-1}{2} = \frac{23-1}{2} = 11$$
Kita nyatakan eksponen $11$ dalam representasi biner (penjumlahan pangkat 2):
$$11 = 8 + 2 + 1 = 2^3 + 2^1 + 2^0$$
Maka:
$$10^{11} \equiv 10^8 \times 10^2 \times 10^1 \pmod{23}$$

#### Langkah 1: Teknik Kuadrat Berulang (Repeated Squaring) Modulo $23$
1. **$10^1$:**
   $$10^1 \equiv 10 \pmod{23}$$
2. **$10^2$:**
   $$10^2 = 100$$
   $100 = 4 \times 23 + 8 \implies 10^2 \equiv 8 \pmod{23}$
3. **$10^4$:**
   $$10^4 = (10^2)^2 \equiv 8^2 = 64 \pmod{23}$$
   $64 = 2 \times 23 + 18 \implies 10^4 \equiv 18 \equiv -5 \pmod{23}$
4. **$10^8$:**
   $$10^8 = (10^4)^2 \equiv (-5)^2 = 25 \pmod{23}$$
   $25 = 23 + 2 \implies 10^8 \equiv 2 \pmod{23}$

#### Langkah 2: Mengalikan Suku-Suku Biner
$$\begin{aligned}
10^{11} &= 10^8 \times 10^2 \times 10^1 \\
&\equiv 2 \times 8 \times 10 \pmod{23} \\
&\equiv 16 \times 10 \pmod{23} \\
&= 160 \pmod{23}
\end{aligned}$$
Kita bagi $160$ dengan $23$:
$$160 = 6 \times 23 + 22 = 138 + 22$$
Sehingga:
$$10^{11} \equiv 22 \equiv -1 \pmod{23}$$

#### Langkah 3: Kesimpulan Simbol Legendre
Berdasarkan Kriteria Euler:
$$\left(\frac{10}{23}\right) \equiv 10^{\frac{23-1}{2}} = 10^{11} \equiv -1 \pmod{23}$$
Karena nilai simbol Legendre harus berupa $\pm 1$, maka:
$$\left(\frac{10}{23}\right) = -1$$

**Jawaban Akhir Soal 4:**  
$$\left(\frac{10}{23}\right) = -1$$
(Artinya $10$ bukan residu kuadrat modulo $23$).

---

### Soal 5
> **Tentukan apakah $-1$ residu kuadrat modulo $29$ dan modulo $31$. Kemudian buktikan secara umum bahwa $-1$ residu kuadrat modulo $p$ jika dan hanya jika $p \equiv 1 \pmod 4$. Untuk $p = 29$, carilah satu $x$ dengan $x^2 \equiv -1$.**

#### Bagian 1: Pengujian Modulo $29$ dan Modulo $31$
Gunakan Kriteria Euler $\left(\frac{-1}{p}\right) \equiv (-1)^{\frac{p-1}{2}} \pmod p$:
1. **Untuk $p = 29$:**
   $$\frac{p-1}{2} = \frac{29-1}{2} = 14 \quad (\text{genap})$$
   $$\left(\frac{-1}{29}\right) \equiv (-1)^{14} = 1 \pmod{29} \implies \left(\frac{-1}{29}\right) = 1$$
   Jadi, **$-1$ adalah residu kuadrat modulo $29$**.

2. **Untuk $p = 31$:**
   $$\frac{p-1}{2} = \frac{31-1}{2} = 15 \quad (\text{ganjil})$$
   $$\left(\frac{-1}{31}\right) \equiv (-1)^{15} = -1 \pmod{31} \implies \left(\frac{-1}{31}\right) = -1$$
   Jadi, **$-1$ bukan residu kuadrat modulo $31$**.

#### Bagian 2: Bukti Umum ($-1$ residu kuadrat $\pmod p \iff p \equiv 1 \pmod 4$)
Misalkan $p$ bilangan prima ganjil.
Menurut Kriteria Euler:
$$\left(\frac{-1}{p}\right) \equiv (-1)^{\frac{p-1}{2}} \pmod p$$
Karena $(-1)^k$ bernilai $1$ jika $k$ genap dan bernilai $-1$ jika $k$ ganjil:

- **$(\Rightarrow)$ Pembuktian arah "hanya jika":**
  Andaikan $-1$ adalah residu kuadrat modulo $p$. Maka $\left(\frac{-1}{p}\right) = 1$.
  Menurut kriteria Euler:
  $$(-1)^{\frac{p-1}{2}} \equiv 1 \pmod p$$
  Jika $\frac{p-1}{2}$ ganjil, maka $(-1)^{\frac{p-1}{2}} = -1$, sehingga $-1 \equiv 1 \pmod p \implies 2 \equiv 0 \pmod p \implies p \mid 2$. Hal ini kontradiksi karena $p$ prima ganjil.
  Maka $\frac{p-1}{2}$ haruslah genap.
  Artinya terdapat bilangan bulat $k$ sehingga:
  $$\frac{p-1}{2} = 2k \implies p - 1 = 4k \implies p = 4k + 1 \equiv 1 \pmod 4$$

- **$(\Leftarrow)$ Pembuktian arah "jika":**
  Misalkan $p \equiv 1 \pmod 4$. Maka $p = 4k + 1$ untuk suatu bilangan bulat $k$.
  Maka eksponennya:
  $$\frac{p-1}{2} = \frac{(4k + 1) - 1}{2} = 2k \quad (\text{genap})$$
  Sehingga:
  $$\left(\frac{-1}{p}\right) \equiv (-1)^{2k} = 1 \pmod p$$
  Karena $p > 2$, nilai $1$ dan $-1$ tidak kongruen modulo $p$, sehingga $\left(\frac{-1}{p}\right) = 1$.
  Artinya $-1$ adalah residu kuadrat modulo $p$.

$\blacksquare$ Terbukti bahwa $-1$ residu kuadrat modulo $p$ jika dan hanya jika $p \equiv 1 \pmod 4$.

#### Bagian 3: Mencari satu $x$ dengan $x^2 \equiv -1 \pmod{29}$
Persamaan yang ingin diselesaikan:
$$x^2 \equiv -1 \equiv 28 \pmod{29}$$
Kita uji kuadrat dari bilangan bulat positif kecil:
$$\begin{aligned}
10^2 &= 100 = 3 \times 29 + 13 \equiv 13 \\
11^2 &= 121 = 4 \times 29 + 5 \equiv 5 \\
12^2 &= 144
\end{aligned}$$
Perhatikan bahwa:
$$144 = 5 \times 29 - 1 = 145 - 1 \implies 12^2 \equiv -1 \pmod{29}$$

**Verifikasi:**
$$12^2 = 144 = 4 \times 29 + 28 \equiv 28 \equiv -1 \pmod{29} \quad \checkmark$$

*(Catatan: akar lainnya adalah $x \equiv -12 \equiv 17 \pmod{29}$, di mana $17^2 = 289 = 10 \times 29 - 1 \equiv -1 \pmod{29}$).*

**Jawaban Akhir Soal 5:**  
- Modulo $29$: $-1$ adalah **residu kuadrat**.
- Modulo $31$: $-1$ adalah **bukan residu kuadrat**.
- Satu nilai $x$ yang memenuhi $x^2 \equiv -1 \pmod{29}$ adalah **$x = 12$** (atau $x = 17$).

---

### Soal 6
> **Misalkan $p \equiv 3 \pmod 4$ dan $a$ residu kuadrat modulo $p$. Tunjukkan bahwa $x \equiv a^{\frac{p+1}{4}}$ memenuhi $x^2 \equiv a \pmod p$. Terapkan pada $p = 23, a = 2$ (periksa lebih dulu bahwa $2$ residu kuadrat), dan tentukan semua akarnya.**

#### Bagian 1: Pembuktian Rumus Akar Kuadrat
**Bukti:**
1. Karena $p \equiv 3 \pmod 4$, maka $p = 4k + 3$ untuk suatu $k \in \mathbb{Z}$.
   Maka:
   $$\frac{p+1}{4} = \frac{4k+4}{4} = k + 1 \in \mathbb{Z}$$
   sehingga eksponen $\frac{p+1}{4}$ terdefinisi dengan baik sebagai bilangan bulat.
2. Diberikan $x \equiv a^{\frac{p+1}{4}} \pmod p$. Kita kuadratkan kedua ruas:
   $$x^2 \equiv \left(a^{\frac{p+1}{4}}\right)^2 \equiv a^{\frac{2(p+1)}{4}} = a^{\frac{p+1}{2}} \pmod p$$
3. Uraikan eksponen $\frac{p+1}{2}$:
   $$\frac{p+1}{2} = \frac{(p-1) + 2}{2} = \frac{p-1}{2} + 1$$
   Maka:
   $$x^2 \equiv a^{\frac{p-1}{2} + 1} \equiv a^{\frac{p-1}{2}} \cdot a^1 \pmod p$$
4. Karena $a$ adalah residu kuadrat modulo $p$, berdasarkan Kriteria Euler berlaku:
   $$a^{\frac{p-1}{2}} \equiv 1 \pmod p$$
5. Substitusikan kembali:
   $$x^2 \equiv (1) \cdot a \equiv a \pmod p$$
$\blacksquare$ Terbukti bahwa $x \equiv a^{\frac{p+1}{4}} \pmod p$ memenuhi $x^2 \equiv a \pmod p$.

---

#### Bagian 2: Penerapan pada $p = 23, a = 2$

##### 1. Pemeriksaan Apakah $2$ Residu Kuadrat Modulo $23$
Eksponen Kriteria Euler: $\frac{p-1}{2} = \frac{23-1}{2} = 11$.
Kita hitung $2^{11} \pmod{23}$:
$$\begin{aligned}
2^5 &= 32 = 23 + 9 \equiv 9 \pmod{23} \\
2^{10} &= (2^5)^2 \equiv 9^2 = 81 = 3 \times 23 + 12 \equiv 12 \pmod{23} \\
2^{11} &= 2 \times 2^{10} \equiv 2 \times 12 = 24 = 23 + 1 \equiv 1 \pmod{23}
\end{aligned}$$
Karena $2^{\frac{23-1}{2}} \equiv 1 \pmod{23}$, terbukti bahwa:
$$\left(\frac{2}{23}\right) = 1 \implies \mathbf{2 \text{ adalah residu kuadrat modulo } 23}.$$

##### 2. Menghitung Nilai Akar $x$
Perhatikan bahwa $23 = 4(5) + 3 \equiv 3 \pmod 4$.
Gunakan rumus yang telah dibuktikan:
$$x \equiv a^{\frac{p+1}{4}} = 2^{\frac{23+1}{4}} = 2^{\frac{24}{4}} = 2^6 \pmod{23}$$
Hitung nilai $2^6$:
$$2^6 = 64$$
$$64 = 2 \times 23 + 18 = 46 + 18$$
Maka diperoleh akar pertama:
$$x_1 \equiv 18 \pmod{23}$$

Akar kedua diperoleh dari simetri modulo $p$:
$$x_2 \equiv -x_1 \equiv -18 \equiv 23 - 18 = 5 \pmod{23}$$

##### 3. Verifikasi Hasil
- $5^2 = 25 = 23 + 2 \equiv 2 \pmod{23} \quad \checkmark$
- $18^2 = 324 = 14 \times 23 + 2 = 322 + 2 \equiv 2 \pmod{23} \quad \checkmark$

**Jawaban Akhir Soal 6:**  
Semua akar dari $x^2 \equiv 2 \pmod{23}$ adalah:
$$x \equiv 5 \pmod{23} \quad \text{dan} \quad x \equiv 18 \pmod{23}$$

---

### Soal 7
> **Buktikan: jika $a$ residu kuadrat modulo $p$, maka $a^{\frac{p-1}{2}} \equiv 1 \pmod p$. Buktikan juga bahwa untuk sembarang $a$ dengan $p \nmid a$, nilai $a^{\frac{p-1}{2}}$ hanya mungkin $1$ atau $-1$.**

#### Bagian 1: Bukti bahwa $a$ residu kuadrat $\implies a^{\frac{p-1}{2}} \equiv 1 \pmod p$
**Bukti:**
1. Karena $a$ adalah residu kuadrat modulo $p$, berdasarkan definisi terdapat bilangan bulat $x$ sedemikian sehingga:
   $$x^2 \equiv a \pmod p$$
2. Karena $p \nmid a$, maka $p \nmid x$ (sebab jika $p \mid x$, maka $p \mid x^2 \implies p \mid a$, kontradiksi). Artinya $\gcd(x, p) = 1$.
3. Pangkatkan kedua ruas dengan $\frac{p-1}{2}$:
   $$a^{\frac{p-1}{2}} \equiv (x^2)^{\frac{p-1}{2}} \equiv x^{2 \cdot \frac{p-1}{2}} = x^{p-1} \pmod p$$
4. Menurut **Teorema Kecil Fermat (Fermat's Little Theorem)**, karena $p$ prima dan $\gcd(x, p) = 1$, berlaku:
   $$x^{p-1} \equiv 1 \pmod p$$
5. Oleh karena itu:
   $$a^{\frac{p-1}{2}} \equiv 1 \pmod p$$
$\blacksquare$ Terbukti.

---

#### Bagian 2: Bukti bahwa untuk sembarang $a$ dengan $p \nmid a$, nilai $a^{\frac{p-1}{2}} \equiv \pm 1 \pmod p$
**Bukti:**
1. Misalkan $y = a^{\frac{p-1}{2}}$.
2. Berdasarkan Teorema Kecil Fermat, untuk sembarang $a$ dengan $\gcd(a, p) = 1$:
   $$a^{p-1} \equiv 1 \pmod p$$
3. Tuliskan kembali sebagai:
   $$a^{p-1} - 1 \equiv 0 \pmod p$$
4. Bentuk di ruas kiri merupakan selisih dua kuadrat:
   $$\left(a^{\frac{p-1}{2}}\right)^2 - 1 = (y^2 - 1) = (y - 1)(y + 1)$$
   Sehingga:
   $$(y - 1)(y + 1) \equiv 0 \pmod p$$
   Artinya:
   $$p \mid (y - 1)(y + 1)$$
5. Karena $p$ adalah bilangan prima, menurut **Lemma Euclid** (jika $p \mid AB$, maka $p \mid A$ atau $p \mid B$):
   $$p \mid (y - 1) \quad \text{atau} \quad p \mid (y + 1)$$
6. Ini berarti:
   $$y - 1 \equiv 0 \pmod p \implies y \equiv 1 \pmod p$$
   atau
   $$y + 1 \equiv 0 \pmod p \implies y \equiv -1 \pmod p$$
7. Mengingat $y = a^{\frac{p-1}{2}}$, maka nilai $a^{\frac{p-1}{2}} \pmod p$ hanya mungkin bernilai $1$ atau $-1$.

$\blacksquare$ Terbukti.

---

### Soal 8
> **Buktikan bahwa terdapat tepat $\frac{p-1}{2}$ residu kuadrat taknol modulo $p$. Lalu gunakan fakta bahwa polinomial berderajat $d$ atas $\mathbb{Z}_p$ memiliki paling banyak $d$ akar untuk membuktikan bahwa bukan residu kuadrat pasti memenuhi $a^{\frac{p-1}{2}} \equiv -1$ (bagian "hanya jika" pada kriteria Euler).**

#### Bagian 1: Bukti Terdapat Tepat $\frac{p-1}{2}$ Residu Kuadrat Taknol Modulo $p$
**Bukti:**
1. Himpunan seluruh kelas residu taknol modulo $p$ adalah $\mathbb{Z}_p^\times = \{1, 2, 3, \ldots, p-1\}$.
2. Seluruh kemungkinan residu kuadrat taknol diperoleh dari kuadrat elemen-elemen di $\mathbb{Z}_p^\times$:
   $$\{1^2, 2^2, 3^2, \ldots, (p-1)^2\} \pmod p$$
3. Perhatikan bahwa untuk setiap $k \in \{1, 2, \ldots, p-1\}$:
   $$(p - k)^2 = p^2 - 2pk + k^2 \equiv k^2 \pmod p$$
   Artinya, setiap bilangan dan invers aditifnya memiliki nilai kuadrat yang sama:
   $$1^2 \equiv (p-1)^2, \quad 2^2 \equiv (p-2)^2, \quad \ldots, \quad \left(\frac{p-1}{2}\right)^2 \equiv \left(\frac{p+1}{2}\right)^2 \pmod p$$
   Oleh karena itu, seluruh nilai kuadrat tercakup dalam himpunan:
   $$S = \left\{1^2, 2^2, 3^2, \ldots, \left(\frac{p-1}{2}\right)^2\right\}$$
4. Sekarang kita tunjukkan bahwa ke-$\frac{p-1}{2}$ elemen dalam $S$ **saling berbeda** modulo $p$:
   Andaikan terdapat $u, v \in \{1, 2, \ldots, \frac{p-1}{2}\}$ dengan $u \neq v$ sedemikian sehingga:
   $$u^2 \equiv v^2 \pmod p$$
   Maka:
   $$u^2 - v^2 \equiv 0 \pmod p \implies (u - v)(u + v) \equiv 0 \pmod p \implies p \mid (u - v)(u + v)$$
   Karena $p$ prima, maka $p \mid (u - v)$ atau $p \mid (u + v)$.
   Namun, perhatikan rentang nilai $u$ dan $v$:
   - $1 \le u, v \le \frac{p-1}{2} \implies -( \frac{p-1}{2} - 1) \le u - v \le \frac{p-1}{2} - 1 < p$. Karena $u \neq v$, maka $u - v \neq 0$, sehingga $p \nmid (u - v)$.
   - $1 + 1 \le u + v \le \frac{p-1}{2} + \left(\frac{p-1}{2} - 1\right) = p - 2 < p$. Karena $u + v > 0$ dan $u + v < p$, maka $p \nmid (u + v)$.
   Kontradiksi!
5. Jadi, tidak ada dua elemen di $S$ yang kongruen modulo $p$.
   Akibatnya, himpunan $S$ menghasilkan tepat $\frac{p-1}{2}$ nilai residu kuadrat taknol yang berbeda modulo $p$.

$\blacksquare$ Terbukti terdapat tepat $\frac{p-1}{2}$ residu kuadrat taknol modulo $p$.

---

#### Bagian 2: Bukti bahwa Bukan Residu Kuadrat Memenuhi $a^{\frac{p-1}{2}} \equiv -1 \pmod p$
**Bukti:**
1. Tinjau polinomial pada lapangan $\mathbb{Z}_p$:
   $$f(x) = x^{\frac{p-1}{2}} - 1 \in \mathbb{Z}_p[x]$$
   Derajat dari polinomial $f(x)$ adalah $d = \frac{p-1}{2}$.
2. **Teorema Lagrange**: Suatu polinomial taknol berderajat $d$ atas lapangan $\mathbb{Z}_p$ memiliki **paling banyak $d$ akar** di $\mathbb{Z}_p$.
   Dengan demikian, kongruensi:
   $$x^{\frac{p-1}{2}} - 1 \equiv 0 \pmod p \iff x^{\frac{p-1}{2}} \equiv 1 \pmod p$$
   memiliki paling banyak $\frac{p-1}{2}$ solusi yang berbeda modulo $p$.
3. Berdasarkan Soal 7 (Bagian 1), setiap residu kuadrat taknol $r \in S$ memenuhi:
   $$r^{\frac{p-1}{2}} \equiv 1 \pmod p$$
   Dari Bagian 1, terdapat tepat $\frac{p-1}{2}$ residu kuadrat yang berbeda di $\mathbb{Z}_p^\times$.
4. Karena sudah ada tepat $\frac{p-1}{2}$ residu kuadrat yang menjadi akar dari $f(x)$, dan $f(x)$ hanya dapat memiliki paling banyak $\frac{p-1}{2}$ akar, maka:
   **Akar-akar dari $x^{\frac{p-1}{2}} \equiv 1 \pmod p$ tepat adalah semua residu kuadrat modulo $p$**.
   Tidak ada elemen lain di $\mathbb{Z}_p^\times$ yang dapat memenuhi persamaan tersebut.
5. Sekarang, misalkan $a$ adalah bukan residu kuadrat (QNR) modulo $p$ dengan $p \nmid a$:
   - Karena $a$ bukan residu kuadrat, maka $a$ bukan merupakan akar dari $f(x)$, sehingga:
     $$a^{\frac{p-1}{2}} \not\equiv 1 \pmod p$$
   - Berdasarkan Soal 7 (Bagian 2), untuk sembarang $a \in \mathbb{Z}_p^\times$, nilai $a^{\frac{p-1}{2}} \pmod p$ hanya mungkin bernilai $1$ atau $-1$.
   - Karena $a^{\frac{p-1}{2}} \not\equiv 1 \pmod p$, maka satu-satunya kemungkinan nilai yang tersisa adalah:
     $$a^{\frac{p-1}{2}} \equiv -1 \pmod p$$

$\blacksquare$ Terbukti secara lengkap bahwa jika $a$ bukan residu kuadrat modulo $p$, maka $a^{\frac{p-1}{2}} \equiv -1 \pmod p$.

---

### Soal 9
> **Buktikan sifat perkalian simbol Legendre, $\left(\frac{ab}{p}\right) = \left(\frac{a}{p}\right)\left(\frac{b}{p}\right)$, dengan kriteria Euler. Simpulkan tiga akibat: hasil kali dua non-residu, residu dengan non-residu, dan dua residu. Beri contoh dengan $p = 7$.**

#### Bagian 1: Bukti Sifat Perkalian Simbol Legendre
**Bukti:**
Menurut Kriteria Euler, untuk sembarang bilangan bulat $c$ dan prima ganjil $p$:
$$\left(\frac{c}{p}\right) \equiv c^{\frac{p-1}{2}} \pmod p$$
Terapkan untuk $c = ab$:
$$\left(\frac{ab}{p}\right) \equiv (ab)^{\frac{p-1}{2}} \pmod p$$
Gunakan sifat distributif eksponen terhadap perkalian:
$$(ab)^{\frac{p-1}{2}} = a^{\frac{p-1}{2}} \cdot b^{\frac{p-1}{2}}$$
Terapkan kembali Kriteria Euler pada masing-masing faktor:
$$a^{\frac{p-1}{2}} \equiv \left(\frac{a}{p}\right) \pmod p \quad \text{dan} \quad b^{\frac{p-1}{2}} \equiv \left(\frac{b}{p}\right) \pmod p$$
Sehingga kita peroleh hubungan kongruensi:
$$\left(\frac{ab}{p}\right) \equiv \left(\frac{a}{p}\right)\left(\frac{b}{p}\right) \pmod p$$
Perhatikan bahwa nilai dari simbol Legendre $\left(\frac{ab}{p}\right)$ dan $\left(\frac{a}{p}\right)\left(\frac{b}{p}\right)$ hanya berada dalam himpunan $\{-1, 0, 1\}$.
Selisih dari kedua besaran tersebut:
$$\Delta = \left(\frac{ab}{p}\right) - \left(\frac{a}{p}\right)\left(\frac{b}{p}\right) \in \{-2, -1, 0, 1, 2\}$$
Karena $\Delta \equiv 0 \pmod p$, maka $p \mid \Delta$.
Mengingat $p$ bilangan prima ganjil ($p \ge 3$), satu-satunya kelipatan $p$ di dalam rentang rentang $[-2, 2]$ adalah $0$.
Oleh karena itu:
$$\Delta = 0 \implies \left(\frac{ab}{p}\right) = \left(\frac{a}{p}\right)\left(\frac{b}{p}\right)$$
$\blacksquare$ Terbukti sifat perkalian simbol Legendre.

---

#### Bagian 2: Tiga Akibat Sifat Perkalian
Misalkan $a, b \not\equiv 0 \pmod p$:

1. **Hasil kali dua residu kuadrat (QR $\times$ QR):**
   $$\left(\frac{a}{p}\right) = 1 \quad \text{dan} \quad \left(\frac{b}{p}\right) = 1 \implies \left(\frac{ab}{p}\right) = (1)(1) = 1$$
   **Akibat:** Hasil kali dua residu kuadrat adalah **residu kuadrat (QR)**.

2. **Hasil kali residu kuadrat dengan bukan residu kuadrat (QR $\times$ QNR):**
   $$\left(\frac{a}{p}\right) = 1 \quad \text{dan} \quad \left(\frac{b}{p}\right) = -1 \implies \left(\frac{ab}{p}\right) = (1)(-1) = -1$$
   **Akibat:** Hasil kali residu kuadrat dengan bukan residu kuadrat adalah **bukan residu kuadrat (QNR)**.

3. **Hasil kali dua bukan residu kuadrat (QNR $\times$ QNR):**
   $$\left(\frac{a}{p}\right) = -1 \quad \text{dan} \quad \left(\frac{b}{p}\right) = -1 \implies \left(\frac{ab}{p}\right) = (-1)(-1) = 1$$
   **Akibat:** Hasil kali dua bukan residu kuadrat adalah **residu kuadrat (QR)**.

---

#### Bagian 3: Contoh Konkret dengan $p = 7$
Untuk $p = 7$, kita cari terlebih dahulu semua kuadrat taknol modulo $7$:
$$\begin{aligned}
1^2 &\equiv 1 \pmod 7 \\
2^2 &\equiv 4 \pmod 7 \\
3^2 &= 9 \equiv 2 \pmod 7 \\
4^2 &= 16 \equiv 2 \pmod 7 \\
5^2 &= 25 \equiv 4 \pmod 7 \\
6^2 &= 36 \equiv 1 \pmod 7
\end{aligned}$$
Dari perhitungan di atas diperoleh:
- Himpunan **Residu Kuadrat (QR)**:
  $$R = \{1, 2, 4\} \quad \implies \left(\frac{a}{7}\right) = 1, \quad \forall a \in R$$
- Himpunan **Bukan Residu Kuadrat (QNR)**:
  $$N = \{3, 5, 6\} \quad \implies \left(\frac{b}{7}\right) = -1, \quad \forall b \in N$$

Mari kita buktikan ketiga akibat tersebut dengan contoh:

1. **Contoh QR $\times$ QR = QR:**
   - Ambil $a = 2 \in R$ dan $b = 4 \in R$.
   - $ab = 2 \times 4 = 8 \equiv 1 \pmod 7$.
   - Karena $1 \in R$, maka $ab$ adalah residu kuadrat.
   - Sesuai rumus: $\left(\frac{8}{7}\right) = \left(\frac{2}{7}\right)\left(\frac{4}{7}\right) = (1)(1) = 1$. $\quad \checkmark$

2. **Contoh QR $\times$ QNR = QNR:**
   - Ambil $a = 2 \in R$ dan $b = 3 \in N$.
   - $ab = 2 \times 3 = 6 \pmod 7$.
   - Karena $6 \in N$, maka $ab$ adalah bukan residu kuadrat.
   - Sesuai rumus: $\left(\frac{6}{7}\right) = \left(\frac{2}{7}\right)\left(\frac{3}{7}\right) = (1)(-1) = -1$. $\quad \checkmark$

3. **Contoh QNR $\times$ QNR = QR:**
   - Ambil $a = 3 \in N$ dan $b = 5 \in N$.
   - $ab = 3 \times 5 = 15 = 2 \times 7 + 1 \equiv 1 \pmod 7$.
   - Karena $1 \in R$, maka $ab$ adalah residu kuadrat!
   - Sesuai rumus: $\left(\frac{15}{7}\right) = \left(\frac{3}{7}\right)\left(\frac{5}{7}\right) = (-1)(-1) = 1$. $\quad \checkmark$
   - *(Contoh lain: ambil $a = 3, b = 6 \in N \implies ab = 18 \equiv 4 \pmod 7$, dan $4 \in R$).*

---
**Selesai.**
