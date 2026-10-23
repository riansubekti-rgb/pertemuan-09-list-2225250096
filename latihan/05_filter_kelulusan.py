# Input: List nilai ujian mahasiswa
# Proses: Melakukan iterasi dan seleksi untuk menyaring nilai >= 60
# Output: Menampilkan daftar nilai yang lulus dan jumlahnya

nilai = [75, 55, 80, 60, 45, 90]
lulus = []
for x in nilai:
    if x >= 60:
        lulus.append(x)
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")