# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Rian Subekti  
NIM: 2225250096  
Kelas: 3F 

## Tujuan
Mengolah kumpulan data numerik dengan list Python.

## Struktur Program
- Folder `latihan/`: Berisi file-file latihan dasar terkait pembuatan list, pengaksesan indeks, teknik slicing, serta fungsi-fungsi agregasi dasar sebelum masuk ke studi kasus utama.
- Folder `praktik/`: Berisi file `analisis_nilai_mahasiswa.py` yang mengimplementasikan fungsi `rata_rata(data)` dan `nilai_lulus(data, batas=60)` untuk memproses data nilai mahasiswa secara spesifik.
## Cara Menjalankan
python3 analisis_nilai_mahasiswa.py

## Hasil Pengujian
| Program / Kuis | Input | Keluaran yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|---|
| `analisis_nilai_mahasiswa.py` | Data: `[60, 70, 80]` | Rata-rata: `70.00` | Rata-rata: `70.00` | Lulus |
| `analisis_nilai_mahasiswa.py` | Data: `[60, 70, 80]` | Minimum / Maksimum: `60 / 80` | Min: `60`, Max: `80` | Lulus |
| `analisis_nilai_mahasiswa.py` | Data: `[60, 70, 80]` | Jumlah lulus: `3` | Jumlah lulus: `3` | Lulus |
| `analisis_nilai_mahasiswa.py` | Data: `[59, 60, 61]` | Batas kelulusan: `2 lulus` | Jumlah lulus: `2` (`[60, 61]`) | Lulus |
| `analisis_nilai_mahasiswa.py` | Data: `[]` | Penanganan list kosong: Tidak error | Rata-rata: `0` (Tidak error) | Lulus |

## Refleksi
- Pemahaman: Saya memahami cara mengakses elemen menggunakan indeks/list serta menerapkan perulangan dan fungsi agregasi dasar untuk mengolah data numerik secara efisien.
- Perbaikan Kesalahan: Saya berhasil memperbaiki kesalahan pembagian dengan nol saat list kosong dengan menambahkan kondisi `if len(data) == 0:` pada fungsi `rata_rata(data)`.

## Sumber
Bahan_Ajar_Pertemuan_09_List_Array_VSCode_GitHub (1)