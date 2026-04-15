# Repositori Agen Kecerdasan Buatan (AI) Pedoman Penulisan Karya Ilmiah IPB University

[![AI Compatible](https://img.shields.io/badge/AI-Gemini%20CLI%20|%20Claude%20Code%20|%20Cursor-blueviolet)](https://github.com/google/gemini-cli)
[![Language: English](https://img.shields.io/badge/Language-English-blue)](README.en.md)

## PRAKATA

Repositori ini disusun sebagai digitalisasi dari **Pedoman Penulisan Karya Ilmiah (PPKI) IPB University Edisi 2024**. Melalui penerapan teknologi *Agent Skill* dan struktur data Markdown, repositori ini diharapkan dapat menjadi rujukan otomatis bagi mahasiswa dan peneliti di lingkungan IPB University dalam menyusun karya ilmiah yang sesuai dengan gaya selingkung universitas. Pengembangan ini merupakan bagian dari upaya peningkatan kualitas dan standarisasi karya ilmiah di era kecerdasan buatan.

---

## BAB I PENDAHULUAN

Tuntutan perkembangan zaman mengharuskan perubahan paradigma bahwa karya ilmiah harus terpublikasi seluas-luasnya. Selaras dengan amanat dalam KKNI, mutu skripsi, tesis, dan disertasi harus layak terbit di jurnal ilmiah nasional terakreditasi maupun internasional bereputasi. 

Repositori ini hadir untuk mentransformasikan dokumen statis menjadi basis pengetahuan yang dapat dikonsumsi oleh agen AI. Dengan demikian, agen AI dapat memberikan bantuan penulisan yang presisi, mulai dari tata tulis teknis hingga etika pengutipan, tanpa mengurangi integritas akademik penulis.

---

## BAB II STRUKTUR DAN KOMPATIBILITAS AGEN AI

Struktur repositori ini dirancang untuk mendukung berbagai platform kecerdasan buatan melalui konfigurasi *AI-Native*:

1. **Gemini CLI (`.gemini/`)**: Modul keahlian (*skill*) yang dapat diinstal untuk instruksi prosedural langsung di terminal.
2. **Claude Code (`CLAUDE.md`)**: Konfigurasi memori persisten untuk asisten terminal Claude.
3. **Cursor & Windsurf (`.cursor/rules/`)**: Aturan modular berbasis *glob-pattern* untuk penerapan otomatis di lingkungan IDE.
4. **Universal Standard (`AGENTS.md`)**: Standar universal Linux Foundation (2026) yang dapat dibaca oleh hampir seluruh agen AI modern (Codex, Copilot, Devin).

---

## BAB III KETENTUAN TEKNIS PENULISAN (PPKI COMPLIANCE)

Seluruh agen AI yang menggunakan repositori ini diinstruksikan untuk mematuhi ketentuan teknis berikut:

### 3.1 Pias (Margin) dan Tata Letak
Sesuai dengan Lampiran 16 PPKI, batas pengetikan naskah pada kertas A4 (80 gram) ditetapkan sebagai berikut:
- **Pias Kiri**: 4 cm (untuk ruang penjilidan).
- **Pias Atas, Kanan, dan Bawah**: masing-masing 3 cm.
- **Jarak Baris**: 1 spasi.

### 3.2 Tipografi dan Bahasa
- **Jenis Huruf**: Times New Roman ukuran 12 poin untuk teks utama, dan 14 poin (Tebal) untuk judul bab.
- **Gaya Bahasa**: Wajib menggunakan Bahasa Indonesia formal dengan kalimat pasif yang objektif. Penggunaan kata ganti orang pertama (Saya/Kami) harus dihindari.
- **Istilah Baku**: Wajib menggunakan istilah **Prakata** (bukan Kata Pengantar), **Simpulan** (bukan Kesimpulan), dan **Daftar Pustaka** (bukan Referensi).

---

## BAB IV PANDUAN PEMASANGAN KE PROYEK ANDA (ULTRA FAST)

Cara paling modern untuk memasang kecerdasan PPKI ini adalah menggunakan **Vercel Agent Skills CLI**. Perintah ini otomatis memasangkan *skills* ke seluruh AI (Cursor, Claude Code, Cline, dll.) secara sekaligus:

```bash
npx skills add dzakwanalifi/ppki-ipb
```

### Metode Alternatif (Manual):

#### 4.1 Untuk Pengguna Cursor & Windsurf
```bash
npx degit dzakwanalifi/ppki-ipb/skills/ppki-ipb/references .cursor/rules --force
```

#### 4.2 Untuk Pengguna Claude Code
```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/dzakwanalifi/ppki-ipb/master/CLAUDE.md
```

### 4.3 Untuk Pengguna Gemini CLI
Instal modul keahlian (*skill*) secara langsung dari repositori ini:
```bash
# Pastikan gemini-cli sudah terinstal
gemini skills install https://github.com/dzakwanalifi/ppki-ipb --scope workspace
/skills reload
```

### 4.4 Untuk AI Lain (AGENTS.md)
Gunakan standar universal untuk agen AI lainnya:
```bash
curl -o AGENTS.md https://raw.githubusercontent.com/dzakwanalifi/ppki-ipb/master/AGENTS.md
```

---

## BAB V PANDUAN OPERASIONAL PENCARIAN (SEARCH TOOL)

Pencarian aturan spesifik dalam basis pengetahuan dapat dilakukan melalui perintah terminal berikut:
```bash
python scripts/search_ppki.py "<kata_kunci>"
```
*Skrip ini menggunakan algoritma BM25 untuk mengurutkan hasil berdasarkan relevansi substansi dalam dokumen PPKI.*

---

## SIMPULAN

Penerapan digitalisasi PPKI IPB 2024 dalam bentuk repositori agen AI ini merupakan langkah strategis dalam memfasilitasi mahasiswa IPB University untuk menghasilkan karya ilmiah yang berkualitas tinggi. Dengan integrasi yang tepat, standar gaya selingkung universitas dapat dipertahankan secara konsisten di seluruh tahap penulisan.

---

## DAFTAR PUSTAKA

IPB University. 2024. *Pedoman Penulisan Karya Ilmiah Edisi 2024*. Bogor (ID): IPB Press.

---
*Dikembangkan oleh dzakwanalifi bersama Gemini CLI Agent sebagai standar repositori AI-Ready untuk IPB University.*
