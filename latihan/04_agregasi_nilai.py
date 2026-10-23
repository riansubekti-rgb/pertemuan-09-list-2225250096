# Input: List nilai numerik
# Proses: Menghitung total, rata-rata, minimum, dan maksimum menggunakan fungsi agregasi bawaan
# Output: Menampilkan hasil agregasi data

nilai = [75, 80, 65, 90, 88]
print(f"Total = {sum(nilai)}")
print(f"Rata-rata = {sum(nilai)/len(nilai):.2f}")
print(f"Minimum = {min(nilai)}")
print(f"Maksimum = {max(nilai)}")