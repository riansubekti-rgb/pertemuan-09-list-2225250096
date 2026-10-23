def rata_rata(data):
    # lengkapi
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    # lengkapi
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil

# Pilihan Test Case Wajib (bisa diubah manual untuk menguji tabel test case)
# Pilih salah satu data di bawah ini untuk diuji:
# nilai = [60, 70, 80]  # Untuk uji rata-rata (70.00), min/max (60/80), jumlah lulus (3)[cite: 5]
# nilai = [59, 60, 61]  # Untuk uji batas kelulusan (2 lulus)[cite: 5]
# nilai = []            # Untuk uji penanganan list kosong (tidak error)[cite: 5]

# Atau gunakan input manual dari terminal:
input_user = input("Masukkan data test case (contoh: 60 70 80 atau 59 60 61, kosongkan untuk []): ")
if input_user.strip() == "":
    nilai = []
else:
    nilai = [int(x) for x in input_user.replace(',', ' ').split()]

# gunakan fungsi dan tampilkan ringkasan
lulus = nilai_lulus(nilai)
banyak_data = len(nilai)

print(f"\n--- HASIL TEST CASE ---")
print(f"Data          : {nilai}")
print(f"Banyak data   : {banyak_data}")
if banyak_data > 0:
    print(f"Total         : {sum(nilai)}")
    print(f"Rata-rata     : {rata_rata(nilai):.2f}")
    print(f"Minimum       : {min(nilai)}")
    print(f"Maksimum      : {max(nilai)}")
else:
    print(f"Total         : 0")
    print(f"Rata-rata     : {rata_rata(nilai):.2f} (Aman, tidak error)")
    print(f"Minimum       : -")
    print(f"Maksimum      : -")
print(f"Nilai lulus   : {lulus}")
print(f"Jumlah lulus  : {len(lulus)}")
print(f"Belum lulus   : {banyak_data - len(lulus)}")