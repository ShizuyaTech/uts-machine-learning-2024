kedatangan_per_hari = {
    "Ani": {"Senin": 2, "Selasa": 0, "Rabu": 0, "Kamis": 0, "Jumat": 0, "Sabtu": 5, "Minggu": 0},
    "Budi": {"Senin": 0, "Selasa": 3, "Rabu": 0, "Kamis": 0, "Jumat": 0, "Sabtu": 0, "Minggu": 2},
    "Joni": {"Senin": 0, "Selasa": 0, "Rabu": 0, "Kamis": 0, "Jumat": 2, "Sabtu": 0, "Minggu": 0},
    "Jono": {"Senin": 0, "Selasa": 0, "Rabu": 4, "Kamis": 0, "Jumat": 0, "Sabtu": 0, "Minggu": 0},
    "Lono": {"Senin": 0, "Selasa": 0, "Rabu": 0, "Kamis": 1, "Jumat": 0, "Sabtu": 0, "Minggu": 0}
}

def hitung_total_kedatangan_seminggu(kedatangan_per_hari):
    total_kedatangan_per_mahasiswa = {}
    
    for mahasiswa, kedatangan_harian in kedatangan_per_hari.items():
        total_kedatangan = sum(kedatangan_harian.values())
        total_kedatangan_per_mahasiswa[mahasiswa] = total_kedatangan
    
    return total_kedatangan_per_mahasiswa

total_kedatangan = hitung_total_kedatangan_seminggu(kedatangan_per_hari)

frekuensi_datang_tertinggi = max(total_kedatangan.values())
frekuensi_datang_terendah = min(total_kedatangan.values())

print(f"Frekuensi datang tertinggi adalah {frekuensi_datang_tertinggi} kali.")
print(f"Frekuensi datang terendah adalah {frekuensi_datang_terendah} kali.")
