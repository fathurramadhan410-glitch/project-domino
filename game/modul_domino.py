from random import randint #[cite: 30]

def buat_dan_acak_kartu():
    kartu = []
    for i in range(7):
        for j in range(i, 7):
            kartu.append("[" + str(i) + "|" + str(j) + "]") 
    
    for i in range(28):
        acak = randint(0, 27) #[cite: 30]
        sementara = kartu[i]
        kartu[i] = kartu[acak]
        kartu[acak] = sementara
        
    return kartu

def hitung_poin(tangan):
    total = 0
    for k in tangan:
        total += int(k[1]) + int(k[3]) 
    return total

# === INI ADALAH LOGIKA AI KOMPLEKS UNTUK "BIKINAN" ===
def bot_jalan_cerdas(tangan, ujung_kiri, ujung_kanan):
    # TAHAP 1: Bot menghitung jumlah setiap angka (0-6) yang dia pegang
    # Tujuannya untuk mencari tahu angka apa yang paling banyak dia miliki
    frekuensi = [0, 0, 0, 0, 0, 0, 0]
    for k in tangan: #[cite: 22]
        kiri = int(k[1])
        kanan = int(k[3])
        frekuensi[kiri] += 1
        frekuensi[kanan] += 1
        
    # TAHAP 2: Bot mencari semua kartu yang BISA jalan, dan memberikan "Nilai Taktik"
    langkah_valid = []
    for i in range(len(tangan)): #[cite: 22]
        kiri = int(tangan[i][1])
        kanan = int(tangan[i][3])
        
        if ujung_kiri == -1: # Jika bot jalan pertama kali
            nilai_taktik = frekuensi[kiri] + frekuensi[kanan]
            langkah_valid.append([i, kiri, kanan, nilai_taktik])
        else:
            # Simulasi jika kartu dimainkan di kiri atau kanan, apa hasil ujung meja yang baru?
            # Bot akan memberikan nilai tinggi jika ujung meja yang baru adalah angka jagoannya.
            if kiri == ujung_kiri:
                nilai_taktik = frekuensi[kanan] + frekuensi[ujung_kanan]
                langkah_valid.append([i, kanan, ujung_kanan, nilai_taktik])
            if kanan == ujung_kiri:
                nilai_taktik = frekuensi[kiri] + frekuensi[ujung_kanan]
                langkah_valid.append([i, kiri, ujung_kanan, nilai_taktik])
            if kiri == ujung_kanan:
                nilai_taktik = frekuensi[ujung_kiri] + frekuensi[kanan]
                langkah_valid.append([i, ujung_kiri, kanan, nilai_taktik])
            if kanan == ujung_kanan:
                nilai_taktik = frekuensi[ujung_kiri] + frekuensi[kiri]
                langkah_valid.append([i, ujung_kiri, kiri, nilai_taktik])
                
    # TAHAP 3: Jika tidak ada yang cocok, Bot terpaksa Pass
    if len(langkah_valid) == 0: #[cite: 20]
        return None, ujung_kiri, ujung_kanan
        
    # TAHAP 4: Analisis Keputusan (Memilih "Bikinan" Terbaik)
    langkah_terbaik = langkah_valid[0]
    for langkah in langkah_valid: #[cite: 22]
        # Pilih yang nilai taktiknya paling besar
        if langkah[3] > langkah_terbaik[3]:
            langkah_terbaik = langkah
        # Jika nilai taktiknya sama, buang kartu yang baloknya (titiknya) lebih besar
        # untuk meminimalisir kekalahan poin kalau terjadi Guplah
        elif langkah[3] == langkah_terbaik[3]: 
            kartu_lama = int(tangan[langkah_terbaik[0]][1]) + int(tangan[langkah_terbaik[0]][3])
            kartu_baru = int(tangan[langkah[0]][1]) + int(tangan[langkah[0]][3])
            if kartu_baru > kartu_lama:
                langkah_terbaik = langkah
                
    # TAHAP 5: Eksekusi Langkah
    idx = langkah_terbaik[0]
    kartu_dimainkan = tangan.pop(idx)
    
    # Mengembalikan kartu yang dibuang dan ujung meja yang sudah di "bikin" oleh bot
    return kartu_dimainkan, langkah_terbaik[1], langkah_terbaik[2] #[cite: 28]