from django.shortcuts import render, redirect
from . import modul_domino

def meja_permainan(request):
    if 'pemain' not in request.session:
        kartu_semua = modul_domino.buat_dan_acak_kartu()
        request.session['pemain'] = kartu_semua[0:7]
        request.session['bot1'] = kartu_semua[7:14]
        request.session['bot2'] = kartu_semua[14:21]
        request.session['bot3'] = kartu_semua[21:28]
        request.session['meja_kiri'] = -1
        request.session['meja_kanan'] = -1
        request.session['kartu_di_meja'] = [] 
        request.session['pesan'] = "Game dimulai! Giliran Anda."
        request.session['pass_beruntun'] = 0
        request.session['game_over'] = False
        request.session['giliran'] = 1 

    if request.method == 'POST':
        aksi = request.POST.get('aksi')
        
        if aksi == 'reset':
            request.session.flush()
            return redirect('meja_permainan')
            
        if request.session.get('game_over'):
            return redirect('meja_permainan')
            
        pemain = request.session.get('pemain', [])
        kartu_di_meja = request.session.get('kartu_di_meja', [])
        meja_kiri = request.session.get('meja_kiri', -1)
        meja_kanan = request.session.get('meja_kanan', -1)
        pass_beruntun = request.session.get('pass_beruntun', 0)
        giliran = request.session.get('giliran', 1)
        
        def taruh_kartu(kartu, m_kiri, m_kanan, list_meja):
            k = int(kartu[1])
            n = int(kartu[3])
            if m_kiri == -1:
                list_meja.append([k, n])
                return k, n
            if k == m_kiri:
                list_meja.insert(0, [n, k])
                return n, m_kanan
            elif n == m_kiri:
                list_meja.insert(0, [k, n])
                return k, m_kanan
            elif k == m_kanan:
                list_meja.append([k, n])
                return m_kiri, n
            elif n == m_kanan:
                list_meja.append([n, k])
                return m_kiri, k
            return m_kiri, m_kanan

        pesan_log = ""
        
        # === GILIRAN 1: PEMAIN ===
        if giliran == 1 and aksi in ['main', 'pass']:
            if aksi == 'main':
                idx_raw = request.POST.get('kartu_idx')
                if idx_raw is None: return redirect('meja_permainan')
                
                idx = int(idx_raw)
                kartu_dipilih = pemain[idx]
                k = int(kartu_dipilih[1])
                n = int(kartu_dipilih[3])
                
                if meja_kiri != -1 and k != meja_kiri and n != meja_kiri and k != meja_kanan and n != meja_kanan:
                    request.session['pesan'] = f"❌ KARTU TIDAK VALID! Meja butuh angka {meja_kiri} atau {meja_kanan}."
                    request.session.modified = True
                    return redirect('meja_permainan')
                    
                kartu_dipilih = pemain.pop(idx)
                meja_kiri, meja_kanan = taruh_kartu(kartu_dipilih, meja_kiri, meja_kanan, kartu_di_meja)
                pesan_log = f"Anda main: {kartu_dipilih}"
                pass_beruntun = 0
                
            elif aksi == 'pass':
                pesan_log = "Anda: Pass"
                pass_beruntun += 1
                
            request.session['giliran'] = 2
            
        # === GILIRAN 2, 3, 4: BOT JALAN ===
        elif aksi == 'bot_jalan' and giliran in [2, 3, 4]:
            if giliran == 2:
                bot_tangan = request.session.get('bot1', [])
                nama = "Bot 1"
                next_giliran = 3
            elif giliran == 3:
                bot_tangan = request.session.get('bot2', [])
                nama = "Bot 2"
                next_giliran = 4
            else:
                bot_tangan = request.session.get('bot3', [])
                nama = "Bot 3"
                next_giliran = 1
                
            # PERBAIKAN BUG DISINI: Menggunakan _, _ agar tidak merusak posisi meja
            kb, _, _ = modul_domino.bot_jalan_cerdas(bot_tangan, meja_kiri, meja_kanan)
            
            if kb:
                meja_kiri, meja_kanan = taruh_kartu(kb, meja_kiri, meja_kanan, kartu_di_meja)
                pesan_log = f"{nama} main: {kb}"
                pass_beruntun = 0
            else:
                pesan_log = f"{nama}: Pass"
                pass_beruntun += 1
                
            if giliran == 2: request.session['bot1'] = bot_tangan
            elif giliran == 3: request.session['bot2'] = bot_tangan
            else: request.session['bot3'] = bot_tangan
            
            request.session['giliran'] = next_giliran

        # === PENGECEKAN MENANG / GUPLAH ===
        if len(pemain) == 0:
            pesan_log += " 🎉 SELAMAT! ANDA MENANG!"
            request.session['game_over'] = True
        elif len(request.session.get('bot1', ['-'])) == 0:
            pesan_log += " 😭 Bot 1 MENANG!"
            request.session['game_over'] = True
        elif len(request.session.get('bot2', ['-'])) == 0:
            pesan_log += " 😭 Bot 2 MENANG!"
            request.session['game_over'] = True
        elif len(request.session.get('bot3', ['-'])) == 0:
            pesan_log += " 😭 Bot 3 MENANG!"
            request.session['game_over'] = True
            
        if not request.session.get('game_over') and pass_beruntun >= 4:
            request.session['game_over'] = True
            p_anda = modul_domino.hitung_poin(pemain)
            p_b1 = modul_domino.hitung_poin(request.session.get('bot1', []))
            p_b2 = modul_domino.hitung_poin(request.session.get('bot2', []))
            p_b3 = modul_domino.hitung_poin(request.session.get('bot3', []))
            pesan_log += f"<br>🔒 GUPLAH! Poin: Anda({p_anda}) | B1({p_b1}) | B2({p_b2}) | B3({p_b3})."

        request.session['pemain'] = pemain
        request.session['meja_kiri'] = meja_kiri
        request.session['meja_kanan'] = meja_kanan
        request.session['kartu_di_meja'] = kartu_di_meja
        request.session['pass_beruntun'] = pass_beruntun
        request.session['pesan'] = pesan_log
        request.session.modified = True

    context = {
        'pemain': request.session.get('pemain', []),
        'jumlah_bot1': len(request.session.get('bot1', [])),
        'jumlah_bot2': len(request.session.get('bot2', [])),
        'jumlah_bot3': len(request.session.get('bot3', [])),
        'kartu_di_meja': request.session.get('kartu_di_meja', []),
        'pesan': request.session.get('pesan', ''),
        'game_over': request.session.get('game_over', False),
        'giliran': request.session.get('giliran', 1)
    }
    
    return render(request, 'game/meja.html', context)