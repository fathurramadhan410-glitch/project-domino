# 🏆 Domino Island Web Game (UAS Project)

Aplikasi permainan **Kartu Domino (Gaple)** berbasis web yang dikembangkan menggunakan framework **Django (Python)** dengan antarmuka grafis (*Graphical User Interface*) interaktif yang terinspirasi dari game populer *Higgs Domino Island*.

---

## 👤 Identitas Pengembang
* **Nama:** Fathur Ramadhan
* **NIM:** C050425007
* **Program Studi:** Sarjana Terapan / D4 Sistem Informasi Kota Cerdas (Smart City Information Systems)
* **Kelas:** SIKC 3B
* **Mata Kuliah:** Pemrograman Berorientasi Objek (PBO)
* **Kampus:** Politeknik Negeri Banjarmasin

---

## 🎮 Profil Game
Project ini dibuat sebagai sarana **pembelajaran, eksplorasi logika pemrograman berorientasi objek**, Game ini dirancang murni untuk hiburan santai (*casual game*) dengan mensimulasikan permainan kartu domino tradisional beranggotakan **1 Pemain (User)** melawan **3 Bot AI cerdas** secara berurutan (*turn-based*).

---

## ✨ Fitur Game
1. **Sistem Giliran Otomatis (*Turn-Based*):** Alur permainan berjalan adil satu per satu antara pemain dan tiga bot secara bergantian.
2. **Kecerdasan Buatan Bot (AI Cerdas):** Bot dilengkapi modul logika cerdas untuk membaca kondisi meja dan menentukan langkah terbaik atau *Pass* secara otomatis.
3. **Validasi Kartu Pintar:** Sistem secara otomatis menolak kartu yang dibuang jika tidak cocok dengan angka ujung meja.
4. **Tombol *Pass* (Lewat):** Fasilitas bagi pemain maupun bot untuk melewati giliran apabila tidak memiliki kartu yang cocok.
5. **Deteksi Pemenang & Guplah:** Sistem otomatis mendeteksi pemain atau bot yang menghabiskan kartu lebih dulu (Menang) atau mengunci permainan saat tertutup (*Guplah*) dengan sistem perhitungan poin terkecil.
6. **Multimedia Interaktif:** Dilengkapi maskot visual animasi dealer (*Lady*) di pojok atas layar serta pemutar musik latar (*BGM*) kustom yang terus berjalan mulus (*seamless*) tanpa terputus saat halaman berganti.

---

## 📜 Peraturan Permainan
1. Permainan dibagikan sebanyak **7 kartu** untuk masing-masing pemain dan bot di awal ronde.
2. Pemain atau bot yang jalan pertama mencocokkan angka kartunya dengan angka terbuka di ujung kiri atau kanan meja.
3. **Aturan Tumpukan (Balak):** Kartu kembar/balak (seperti `[3|3]`) diletakkan secara vertikal (berdiri tegak), sedangkan kartu biasa diletakkan horizontal menyambung rapat.
4. Jika pemain tidak memiliki kartu yang cocok dengan angka di meja, pemain wajib mengeklik tombol **⏭️ SAYA PASS (LEWAT)**.
5. Permainan berakhir jika:
   * Ada pemain atau bot yang kartu di tangannya habis (Keluar sebagai **Pemenang**).
   * Meja terkunci secara total atau tidak ada yang bisa jalan sebanyak 4 kali putaran berturut-turut (**Guplah**, dimenangkan oleh pemilik total poin kartu terkecil).

---

## 💻 Teknologi Pemrograman & Arsitektur
* **Bahasa Pemrograman:** Python 3.13
* **Framework Web:** Django 6.x (Menggunakan pola arsitektur MVT - *Model-View-Template* dan pengelolaan *Django Sessions*)
* **Logika Inti:** Modul kustom berorientasi objek untuk pengacakan kartu dan algoritma keputusan bot.

---

## 🎨 Pewarnaan & Visual Antarmuka
* **Latar Belakang Meja:** Gradasi hijau kasino profesional (`#2E7D32` hingga `#1B5E20`) untuk menciptakan kesan meja permainan domino autentik.
* **Warna Kartu:** Desain ubin (*tile*) kartu berwarna putih klasik (`#fffdf5`) dengan garis pembatas hitam tegas dan teks angka merah tua (`#b71c1c`) agar sangat mudah dibaca.
* **Efek Interaktif:** Animasi tombol terangkat (*hover effect*) dan efek bayangan (*box-shadow*) lembut untuk memberikan pengalaman visual yang responsif.