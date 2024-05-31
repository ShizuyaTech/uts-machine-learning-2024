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

mahasiswa_terbanyak_datang = max(total_kedatangan, key=total_kedatangan.get)
jumlah_kedatangan_terbanyak = total_kedatangan[mahasiswa_terbanyak_datang]

print(f"Mahasiswa yang paling banyak datang ke kampus adalah {mahasiswa_terbanyak_datang} dengan {jumlah_kedatangan_terbanyak} kali kedatangan.")