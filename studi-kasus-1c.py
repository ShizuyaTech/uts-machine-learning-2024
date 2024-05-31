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
    "Jono": {"Senin": 0, "Selasa": 0, "Rabu": 4, "Kamis": 0, "Jumat": 0, "Sabtu": 0, "Minggu": 1},
    "Lono": {"Senin": 0, "Selasa": 0, "Rabu": 0, "Kamis": 1, "Jumat": 0, "Sabtu": 0, "Minggu": 0}
}

def hitung_total_biaya_per_hari(mahasiswa_biaya, kedatangan_per_hari):
    biaya_per_hari = {"Senin": 0, "Selasa": 0, "Rabu": 0, "Kamis": 0, "Jumat": 0, "Sabtu": 0, "Minggu": 0}
    
    for mahasiswa, biaya_per_kedatangan in mahasiswa_biaya.items():
        for hari, frekuensi in kedatangan_per_hari[mahasiswa].items():
            biaya_per_hari[hari] += biaya_per_kedatangan * frekuensi
    
    return biaya_per_hari

total_biaya_per_hari = hitung_total_biaya_per_hari(mahasiswa_biaya, kedatangan_per_hari)

hari_biaya_lebih_dari_110000 = [hari for hari, biaya in total_biaya_per_hari.items() if biaya > 110000]

print("Hari-hari dengan total biaya lebih dari Rp 110.000:")
for hari in hari_biaya_lebih_dari_110000:
    print(f"{hari}: Rp{total_biaya_per_hari[hari]}")
