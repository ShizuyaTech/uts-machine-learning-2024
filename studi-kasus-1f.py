mahasiswa_biaya = {
    "Ani": 30000,
    "Budi": 35000,
    "Joni": 20000,
    "Jono": 25000,
    "Lono": 15000
}

kedatangan_per_hari = {
    "Ani": {"Senin": 2, "Selasa": 0, "Rabu": 0, "Kamis": 0, "Jumat": 0, "Sabtu": 5, "Minggu": 0},
    "Budi": {"Senin": 0, "Selasa": 3, "Rabu": 0, "Kamis": 0, "Jumat": 0, "Sabtu": 0, "Minggu": 2},
    "Joni": {"Senin": 0, "Selasa": 0, "Rabu": 0, "Kamis": 0, "Jumat": 2, "Sabtu": 0, "Minggu": 0},
    "Jono": {"Senin": 0, "Selasa": 0, "Rabu": 4, "Kamis": 0, "Jumat": 0, "Sabtu": 0, "Minggu": 0},
    "Lono": {"Senin": 0, "Selasa": 0, "Rabu": 0, "Kamis": 1, "Jumat": 0, "Sabtu": 0, "Minggu": 0}
}

def hitung_total_biaya_seminggu(mahasiswa_biaya, kedatangan_per_hari):
    total_biaya_per_mahasiswa = {}
    
    for mahasiswa, biaya_per_kedatangan in mahasiswa_biaya.items():
        total_biaya = 0
        for hari, frekuensi in kedatangan_per_hari[mahasiswa].items():
            total_biaya += biaya_per_kedatangan * frekuensi
        total_biaya_per_mahasiswa[mahasiswa] = total_biaya
    
    return total_biaya_per_mahasiswa

total_biaya_per_mahasiswa = hitung_total_biaya_seminggu(mahasiswa_biaya, kedatangan_per_hari)

biaya_tertinggi = max(total_biaya_per_mahasiswa.values())
biaya_terendah = min(total_biaya_per_mahasiswa.values())

print(f"Biaya tertinggi yang dihabiskan oleh mahasiswa adalah Rp{biaya_tertinggi}.")
print(f"Biaya terendah yang dihabiskan oleh mahasiswa adalah Rp{biaya_terendah}.")
