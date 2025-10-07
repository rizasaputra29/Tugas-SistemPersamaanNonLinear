# Solver Sistem Persamaan Nonlinear

## Informasi Mahasiswa
- **Nama**: [Nama Lengkap Anda]
- **NIM**: 21120123140117
- **Mata Kuliah**: TSK21275 - Metode Numerik
- **Program Studi**: Teknik Komputer
- **Universitas**: Universitas Diponegoro

## Deskripsi
Implementasi solver untuk sistem persamaan nonlinear menggunakan berbagai metode numerik. Program ini dibuat sebagai tugas praktikum Modul 6 - Sistem Persamaan Nonlinear.

## Sistem Persamaan
```
f₁(x,y) = x² + xy - 10 = 0
f₂(x,y) = y + 3xy² - 57 = 0
```

**Solusi Sejati**: x = 2, y = 3

## Metode yang Diimplementasikan

### 1. Iterasi Titik Tetap - Jacobi
Menggunakan kombinasi fungsi iterasi g1A dan g2B (NIMx = 1):
- g1A: x = (10 - x²)/y
- g2B: y = √((57-y)/(3x))

Formula iterasi:
```
x(r+1) = g1(x(r), y(r))
y(r+1) = g2(x(r), y(r))
```

### 2. Iterasi Titik Tetap - Seidel (Gauss-Seidel)
Menggunakan kombinasi fungsi iterasi yang sama dengan Jacobi, tetapi dengan perbaikan:

Formula iterasi:
```
x(r+1) = g1(x(r), y(r))
y(r+1) = g2(x(r+1), y(r))  ← menggunakan x(r+1) yang baru
```

### 3. Newton-Raphson
Metode iterasi menggunakan turunan parsial (Determinan Jacobi):

Formula:
```
x(r+1) = x(r) - [u(r)·∂v/∂y - v(r)·∂u/∂y] / det
y(r+1) = y(r) + [u(r)·∂v/∂x - v(r)·∂u/∂x] / det

dimana det = ∂u/∂x · ∂v/∂y - ∂u/∂y · ∂v/∂x
```

### 4. Metode Secant
Aproksimasi metode Newton-Raphson dengan pendekatan beda hingga untuk turunan.

## Parameter
- **Tebakan Awal**: x₀ = 1.5, y₀ = 3.5
- **Toleransi (ε)**: 0.000001
- **Maksimum Iterasi**: 100

## Struktur File
```
.
├── solver_system.py                    # Program utama
├── README.md                           # Dokumentasi ini
└── Laporan_M06_Muhammad Riza Saputra_21120123140117.docx     # Laporan lengkap
```

## Cara Menjalankan Program

### Prasyarat
- Python 3.6 atau lebih tinggi
- Library: math (built-in)

### Instalasi
```bash
# Clone repository
git clone https://github.com/rizasaputra29/Tugas-SistemPersamaanNonLinear.git
cd Tugas-SistemPersamaanNonLinear

# Atau download langsung file solver_system.py
```

### Menjalankan Program
```bash
python solver_system.py
```

### Output Program
Program akan menampilkan:
1. Tabel iterasi untuk setiap metode
2. Status konvergensi (Konvergen/Divergen)
3. Solusi akhir (jika konvergen)
4. Verifikasi dengan substitusi ke f₁ dan f₂
5. Ringkasan perbandingan semua metode
6. Analisis konvergensi

## Hasil Eksperimen

### Ringkasan Konvergensi

| Metode | Status | Jumlah Iterasi | Solusi (x, y) |
|--------|--------|----------------|---------------|
| Jacobi (g1A, g2B) | Divergen/Konvergen | - | - |
| Seidel (g1A, g2B) | Divergen/Konvergen | - | - |
| Newton-Raphson | Konvergen | ~17 | (2.0, 3.0) |
| Secant | Konvergen | - | (2.0, 3.0) |

*Catatan: Jalankan program untuk melihat hasil lengkap*

## Analisis Konvergensi

### 1. Iterasi Titik Tetap (Jacobi & Seidel)
**Syarat Konvergen**:
```
|∂g₁/∂x| + |∂g₁/∂y| < 1
|∂g₂/∂x| + |∂g₂/∂y| < 1
```

**Kombinasi g1A dan g2B**:
- g1A berasal dari halaman 5 (diketahui divergen pada contoh)
- g2B berasal dari halaman 6 (diketahui konvergen pada contoh)
- Kombinasi ini perlu diuji untuk melihat perilaku konvergensinya

**Perbedaan Jacobi vs Seidel**:
- Jacobi menggunakan nilai iterasi sebelumnya untuk semua variabel
- Seidel langsung menggunakan nilai baru yang sudah dihitung
- Seidel umumnya lebih cepat konvergen (jika konvergen)

### 2. Newton-Raphson
**Kelebihan**:
- Konvergensi kuadratik (sangat cepat)
- Pasti konvergen jika tebakan awal cukup dekat dengan solusi

**Kekurangan**:
- Memerlukan perhitungan turunan parsial
- Komputasi determinan Jacobi bisa mahal

### 3. Metode Secant
**Karakteristik**:
- Tidak perlu turunan eksplisit
- Konvergensi superlinear (lebih lambat dari Newton-Raphson)
- Lebih praktis untuk fungsi kompleks

## Catatan Penting

### Pemilihan Fungsi Iterasi
Pemilihan kombinasi g1 dan g2 sangat mempengaruhi konvergensi:
- **g1A dan g2A**: Cenderung divergen (lihat hal. 5 dokumen)
- **g1B dan g2B**: Konvergen baik (lihat hal. 6 dokumen)
- **g1A dan g2B**: Perlu diuji (kasus NIMx = 1)

### Tebakan Awal
Tebakan awal sangat mempengaruhi:
- Kecepatan konvergensi
- Apakah metode akan konvergen atau tidak
- Iterasi yang dibutuhkan

---
© 2025 - Teknik Komputer, Universitas Diponegoro