import json
import os
import uuid

def create_notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.12"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

def md_cell(source):
    return {
        "cell_type": "markdown",
        "id": uuid.uuid4().hex[:8],
        "metadata": {},
        "source": [line + "\n" for line in source.strip().split("\n")]
    }

def code_cell(source):
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": uuid.uuid4().hex[:8],
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source.strip().split("\n")]
    }

base_dir = r"c:\Users\MyBook Z Series\Desktop\Kriptografi\07 Block Cipher (DES & AES)"

# ==============================================================================
# NOTEBOOK 1: 01_DES_From_Scratch.ipynb
# ==============================================================================
nb1_cells = [
    md_cell("""# 🛡️ Data Encryption Standard (DES) from Scratch
### Mata Kuliah: MA4151 - Kriptografi
**Berbasis Teks Karakter Asli, Angka Desimal (0-255), dan Bit Biner (0/1)**

---

## 🎯 Tujuan Pembelajaran
1. Memahami bahwa **64 bit = 8 karakter teks** (misal kata `"KOMPUTER"`).
2. Mempelajari alur konversi: **Karakter $\\to$ Nilai Desimal (ASCII) $\\to$ 8 Bit Biner**.
3. Menguasai fungsi permutasi dan manipulasi bit DES:
   - Initial Permutation ($IP$) dan Inverse Initial Permutation ($IP^{-1}$)
   - Key Schedule ($PC\\text{-}1$, pergeseran kiri melingkar, $PC\\text{-}2$)
   - Fungsi Feistel $f(R, K)$ (Ekspansi $E$, XOR subkunci, 8 Kotak-S, Permutasi $P$)
   - 16 Ronde Feistel Enkripsi dan Dekripsi
4. Menjalankan eksperimen **Efek Salju (Avalanche Effect)** pada teks nyata."""),

    md_cell("""---
## 1. Konversi Teks $\\to$ Desimal $\\to$ Bit Biner (Bit Helpers)
Komputer menyimpan huruf sebagai angka desimal standar (ASCII $0-255$). Setiap angka desimal disimpan sebagai deretan 8 bit biner ($0$ dan $1$)."""),

    code_cell("""def text_to_bits(text: str) -> list[int]:
    \"\"\"Mengonversi teks string menjadi daftar bit biner (0 dan 1).\"\"\"
    data_bytes = text.encode('ascii')
    bits = []
    for b in data_bytes:
        for i in range(7, -1, -1):
            bits.append((b >> i) & 1)
    return bits

def bits_to_decimals(bits: list[int]) -> list[int]:
    \"\"\"Mengonversi daftar bit biner menjadi daftar angka desimal (0-255).\"\"\"
    decimals = []
    for i in range(0, len(bits), 8):
        val = 0
        for b in bits[i:i+8]:
            val = (val << 1) | b
        decimals.append(val)
    return decimals

def permute(bits: list[int], table: list[int]) -> list[int]:
    \"\"\"Menerapkan tabel permutasi (1-indexed) pada daftar bit.\"\"\"
    return [bits[idx - 1] for idx in table]

# Contoh Konversi Teks Nyata
teks_contoh = "KOMPUTER" # 8 karakter = 64 bit
bits_contoh = text_to_bits(teks_contoh)
desimal_contoh = bits_to_decimals(bits_contoh)

print(f"Teks Asli        : {teks_contoh} (Panjang: {len(teks_contoh)} huruf)")
print(f"Nilai Desimal    : {desimal_contoh}")
print(f"Bit Biner (64-bit): {' '.join(''.join(map(str, bits_contoh[i:i+8])) for i in range(0, 64, 8))}")"""),

    md_cell("""---
## 2. Tabel Permutasi Baku DES (Standar FIPS 46-3)"""),

    code_cell("""IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

E_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

S_BOXES = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

P_TABLE = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

print("Tabel standar DES siap!")"""),

    md_cell("""---
## 3. Pembangkitan Kunci Ronde & Fungsi Feistel $f(R, K)$"""),

    code_cell("""def des_generate_keys(key_bits: list[int]) -> list[list[int]]:
    permuted_key = permute(key_bits, PC1)
    c = permuted_key[:28]
    d = permuted_key[28:]
    subkeys = []
    for shift in SHIFTS:
        c = c[shift:] + c[:shift]
        d = d[shift:] + d[:shift]
        subkeys.append(permute(c + d, PC2))
    return subkeys

def des_f(r: list[int], subkey: list[int]) -> list[int]:
    expanded = permute(r, E_TABLE)
    xored = [bit ^ k for bit, k in zip(expanded, subkey)]
    sbox_out = []
    for i in range(8):
        chunk = xored[i * 6 : (i + 1) * 6]
        row = (chunk[0] << 1) | chunk[5]
        col = (chunk[1] << 3) | (chunk[2] << 2) | (chunk[3] << 1) | chunk[4]
        val = S_BOXES[i][row][col]
        for shift in (3, 2, 1, 0):
            sbox_out.append((val >> shift) & 1)
    return permute(sbox_out, P_TABLE)

def des_encrypt_block(pt_bits: list[int], subkeys: list[list[int]], verbose: bool = False) -> list[int]:
    bits = permute(pt_bits, IP)
    l, r = bits[:32], bits[32:]
    for round_idx, k in enumerate(subkeys, 1):
        f_res = des_f(r, k)
        l, r = r, [l_bit ^ f_bit for l_bit, f_bit in zip(l, f_res)]
        if verbose:
            print(f"Ronde {round_idx:2d}: L (desimal)={bits_to_decimals(l)}, R (desimal)={bits_to_decimals(r)}")
    return permute(r + l, IP_INV)

def des_decrypt_block(ct_bits: list[int], subkeys: list[list[int]]) -> list[int]:
    return des_encrypt_block(ct_bits, subkeys[::-1])"""),

    md_cell("""---
## 4. Eksekusi Enkripsi Teks Nyata: `"KOMPUTER"` dengan Kunci `"RAHASIA1"`"""),

    code_cell("""pesan_teks = "KOMPUTER"
kunci_teks = "RAHASIA1"

pt_bits = text_to_bits(pesan_teks)
k_bits = text_to_bits(kunci_teks)
subkeys = des_generate_keys(k_bits)

print("=== ENKRIPSI DES ===")
print(f"Pesan Asli   : '{pesan_teks}' -> Desimal: {bits_to_decimals(pt_bits)}")
print(f"Kunci Rahasia: '{kunci_teks}' -> Desimal: {bits_to_decimals(k_bits)}\\n")

print("--- Putaran 16 Ronde Feistel (Nilai Desimal Tiap 4 Byte) ---")
ct_bits = des_encrypt_block(pt_bits, subkeys, verbose=True)
ct_decimals = bits_to_decimals(ct_bits)

print("\\n=== HASIL AKHIR ===")
print(f"Ciphertext Desimal (8 Byte): {ct_decimals}")
print(f"Ciphertext Biner (64 Bit)  : {' '.join(''.join(map(str, ct_bits[i:i+8])) for i in range(0, 64, 8))}")

# Dekripsi
dec_bits = des_decrypt_block(ct_bits, subkeys)
dec_text = bytes(bits_to_decimals(dec_bits)).decode('ascii')
print(f"\\nHasil Dekripsi Kembali     : '{dec_text}' (100% Cocok!)")"""),

    md_cell("""---
## 5. Eksperimen Efek Salju (Avalanche Effect)"""),

    code_cell("""import matplotlib.pyplot as plt

def trace_des_round_bits(pt_bits, subkeys):
    bits = permute(pt_bits, IP)
    l, r = bits[:32], bits[32:]
    history = [l + r]
    for k in subkeys:
        f_res = des_f(r, k)
        l, r = r, [l_bit ^ f_bit for l_bit, f_bit in zip(l, f_res)]
        history.append(l + r)
    return history

pt1 = text_to_bits("KOMPUTER")
pt2 = text_to_bits("KOMPUTES") # 'R' (82) -> 'S' (83), beda tepat 1 bit!

h1 = trace_des_round_bits(pt1, subkeys)
h2 = trace_des_round_bits(pt2, subkeys)
diffs = [sum(b1 != b2 for b1, b2 in zip(s1, s2)) for s1, s2 in zip(h1, h2)]

print("Jumlah Bit Berubah di Setiap Ronde (dari 64 bit):")
for r, d in enumerate(diffs):
    print(f"Ronde {r:2d}: {d:2d} bit berubah ({(d/64)*100:5.1f}%)")

plt.figure(figsize=(9, 4.5))
plt.plot(range(17), diffs, marker='o', color='#1f77b4', linewidth=2, label='Bit Berubah (DES)')
plt.axhline(y=32, color='red', linestyle='--', label='Ideal SAC (50% = 32 bit)')
plt.title("Analisis Efek Salju (Avalanche Effect) pada DES", fontsize=12, fontweight='bold')
plt.xlabel("Ronde Feistel")
plt.ylabel("Jumlah Bit Berubah (dari 64 bit)")
plt.xticks(range(17))
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()""")
]

# ==============================================================================
# NOTEBOOK 2: 02_AES_From_Scratch.ipynb
# ==============================================================================
nb2_cells = [
    md_cell("""# 💎 Advanced Encryption Standard (AES / Rijndael) from Scratch
### Mata Kuliah: MA4151 - Kriptografi
**Berbasis Teks Karakter Asli, Matriks Desimal (0-255), dan Bit Biner (0/1)**

---

## 🎯 Tujuan Pembelajaran
1. Memahami bahwa **128 bit = 16 karakter teks** (misal kata `"KRIPTOGRAFI ITB!"`).
2. Menyusun 16 karakter teks dalam **Matriks State $4 \\times 4$** berurutan kolom demi kolom.
3. Mengimplementasikan operasi aljabar Lapangan Terhingga $GF(2^8)$ dan pembentukan Kotak-S secara matematis.
4. Menguasai 4 transformasi ronde AES dalam angka desimal biasa:
   - `SubBytes`
   - `ShiftRows`
   - `MixColumns`
   - `AddRoundKey`
5. Melakukan enkripsi teks nyata dan analisis difusi kilat."""),

    md_cell("""---
## 1. Fondasi Aritmetika Lapangan Galois $GF(2^8)$"""),

    code_cell("""# Aritmetika Lapangan Terhingga GF(2^8) (Desimal 0-255)

def xtime(a: int) -> int:
    hi_bit = a & 0x80
    shifted = (a << 1) & 0xFF
    return shifted ^ 0x1B if hi_bit else shifted

def gf_mult(a: int, b: int) -> int:
    \"\"\"Perkalian di GF(2^8) (Russian Peasant Multiplication).\"\"\"
    res = 0
    for _ in range(8):
        if b & 1:
            res ^= a
        a = xtime(a)
        b >>= 1
    return res

def gf_inv(a: int) -> int:
    \"\"\"Invers multiplikatif menggunakan a^(254) mod m(x).\"\"\"
    if a == 0:
        return 0
    res = 1
    base = a
    exp = 254
    while exp > 0:
        if exp & 1:
            res = gf_mult(res, base)
        base = gf_mult(base, base)
        exp >>= 1
    return res

# Pembangkitan S-Box Aljabar
S_BOX = [0] * 256
INV_S_BOX = [0] * 256
for i in range(256):
    inv = gf_inv(i)
    s = inv
    for shift in (1, 2, 3, 4):
        s ^= ((inv << shift) | (inv >> (8 - shift))) & 0xFF
    s ^= 0x63
    S_BOX[i] = s
    INV_S_BOX[s] = i

print(f"S-Box untuk desimal 0   : {S_BOX[0]}  (Biner: {S_BOX[0]:08b})")
print(f"S-Box untuk desimal 75  : {S_BOX[75]} (Biner: {S_BOX[75]:08b})")"""),

    md_cell("""---
## 2. Pembangkitan Matriks State $4 \\times 4$ dari Teks 16 Karakter"""),

    code_cell("""def text_to_state(text_16: str) -> list[list[int]]:
    \"\"\"Mengonversi 16 karakter teks menjadi matriks State 4x4 desimal (column-major).\"\"\"
    assert len(text_16) == 16, "Teks harus tepat 16 karakter."
    decimals = list(text_16.encode('ascii'))
    state = [[0] * 4 for _ in range(4)]
    for col in range(4):
        for row in range(4):
            state[row][col] = decimals[col * 4 + row]
    return state

def state_to_text(state: list[list[int]]) -> str:
    \"\"\"Mengonversi matriks State 4x4 kembali ke teks string.\"\"\"
    decimals = []
    for col in range(4):
        for row in range(4):
            decimals.append(state[row][col])
    return bytes(decimals).decode('ascii', errors='replace')

def print_state_decimal(state: list[list[int]], label: str = "State:"):
    print(label)
    for r in range(4):
        print("  [" + " ".join(f"{state[r][c]:3d}" for c in range(4)) + "]")

pesan_aes = "KRIPTOGRAFI ITB!" # 16 karakter
state_awal = text_to_state(pesan_aes)
print_state_decimal(state_awal, f"Matriks State Desimal untuk '{pesan_aes}':")"""),

    md_cell("""---
## 3. Empat Transformasi Ronde AES"""),

    code_cell("""def sub_bytes(state):
    for r in range(4):
        for c in range(4):
            state[r][c] = S_BOX[state[r][c]]

def inv_sub_bytes(state):
    for r in range(4):
        for c in range(4):
            state[r][c] = INV_S_BOX[state[r][c]]

def shift_rows(state):
    state[1] = state[1][1:] + state[1][:1] # Geser kiri 1
    state[2] = state[2][2:] + state[2][:2] # Geser kiri 2
    state[3] = state[3][3:] + state[3][:3] # Geser kiri 3

def inv_shift_rows(state):
    state[1] = state[1][3:] + state[1][:3]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][1:] + state[3][:1]

def mix_columns(state):
    for c in range(4):
        s0, s1, s2, s3 = state[0][c], state[1][c], state[2][c], state[3][c]
        state[0][c] = gf_mult(0x02, s0) ^ gf_mult(0x03, s1) ^ s2 ^ s3
        state[1][c] = s0 ^ gf_mult(0x02, s1) ^ gf_mult(0x03, s2) ^ s3
        state[2][c] = s0 ^ s1 ^ gf_mult(0x02, s2) ^ gf_mult(0x03, s3)
        state[3][c] = gf_mult(0x03, s0) ^ s1 ^ s2 ^ gf_mult(0x02, s3)

def inv_mix_columns(state):
    for c in range(4):
        s0, s1, s2, s3 = state[0][c], state[1][c], state[2][c], state[3][c]
        state[0][c] = gf_mult(0x0E, s0) ^ gf_mult(0x0B, s1) ^ gf_mult(0x0D, s2) ^ gf_mult(0x09, s3)
        state[1][c] = gf_mult(0x09, s0) ^ gf_mult(0x0E, s1) ^ gf_mult(0x0B, s2) ^ gf_mult(0x0D, s3)
        state[2][c] = gf_mult(0x0D, s0) ^ gf_mult(0x09, s1) ^ gf_mult(0x0E, s2) ^ gf_mult(0x0B, s3)
        state[3][c] = gf_mult(0x0B, s0) ^ gf_mult(0x0D, s1) ^ gf_mult(0x09, s2) ^ gf_mult(0x0E, s3)

def add_round_key(state, round_key):
    for r in range(4):
        for c in range(4):
            state[r][c] ^= round_key[r][c]

print("Transformasi ronde AES siap!")"""),

    md_cell("""---
## 4. Key Expansion & Algoritma Enkripsi AES-128 Lengkap"""),

    code_cell("""RCON = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

def aes_key_expansion(key_text_16: str) -> list[list[list[int]]]:
    decimals = list(key_text_16.encode('ascii'))
    w = [decimals[4*i : 4*i+4] for i in range(4)]
    for i in range(4, 44):
        temp = list(w[i-1])
        if i % 4 == 0:
            temp = [S_BOX[b] for b in (temp[1:] + temp[:1])]
            temp[0] ^= RCON[i // 4]
        w.append([w[i-4][j] ^ temp[j] for j in range(4)])
    round_keys = []
    for r in range(11):
        rk = []
        for row in range(4):
            rk.append([w[r*4 + col][row] for col in range(4)])
        round_keys.append(rk)
    return round_keys

def aes_encrypt_block(state: list[list[int]], round_keys: list[list[list[int]]], verbose: bool = False):
    st = [row[:] for row in state]
    add_round_key(st, round_keys[0])
    for r in range(1, 10):
        sub_bytes(st)
        shift_rows(st)
        mix_columns(st)
        add_round_key(st, round_keys[r])
        if verbose and r == 1:
            print_state_decimal(st, "State Desimal setelah Ronde 1:")
    # Ronde 10 (Tanpa MixColumns)
    sub_bytes(st)
    shift_rows(st)
    add_round_key(st, round_keys[10])
    return st

def aes_decrypt_block(state: list[list[int]], round_keys: list[list[list[int]]]):
    st = [row[:] for row in state]
    add_round_key(st, round_keys[10])
    for r in range(9, 0, -1):
        inv_shift_rows(st)
        inv_sub_bytes(st)
        add_round_key(st, round_keys[r])
        inv_mix_columns(st)
    inv_shift_rows(st)
    inv_sub_bytes(st)
    add_round_key(st, round_keys[0])
    return st"""),

    md_cell("""---
## 5. Eksekusi Enkripsi Teks Nyata: `"KRIPTOGRAFI ITB!"` dengan Kunci `"KUNCI RAHASIAKU!"`"""),

    code_cell("""pesan_aes = "KRIPTOGRAFI ITB!"
kunci_aes = "KUNCI RAHASIAKU!"

state_in = text_to_state(pesan_aes)
rkeys = aes_key_expansion(kunci_aes)

print("=== ENKRIPSI AES-128 ===")
print_state_decimal(state_in, f"State Teks Asli ('{pesan_aes}'):")
print_state_decimal(rkeys[0], f"Subkunci Ronde 0 K0 ('{kunci_aes}'):")

state_out = aes_encrypt_block(state_in, rkeys, verbose=True)

print_state_decimal(state_out, "\\nState Ciphertext Akhir (Desimal):")

# Dekripsi
state_decrypted = aes_decrypt_block(state_out, rkeys)
teks_kembali = state_to_text(state_decrypted)
print(f"\\nHasil Dekripsi Kembali: '{teks_kembali}' (100% Cocok!)")""")
]

# Write all notebooks
with open(os.path.join(base_dir, "01_DES_From_Scratch.ipynb"), "w", encoding="utf-8") as f:
    json.dump(create_notebook(nb1_cells), f, indent=1)

with open(os.path.join(base_dir, "02_AES_From_Scratch.ipynb"), "w", encoding="utf-8") as f:
    json.dump(create_notebook(nb2_cells), f, indent=1)

print("Semua notebook diperbarui dengan format teks & desimal yang ramah!")
