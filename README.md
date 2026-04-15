# PPKI IPB Agent Skills

Kumpulan keahlian agen AI (*Agent Skills*) untuk **Pedoman Penulisan Karya Ilmiah (PPKI) IPB University 2024**. Proyek ini menyediakan instruksi dan skrip terpaket untuk memperluas kemampuan agen AI dalam penulisan akademik, pemformatan pias, dan validasi bahasa Indonesia.

[![AI Compatible](https://img.shields.io/badge/AI-Gemini%20CLI%20|%20Claude%20Code%20|%20Cursor-blueviolet)](https://github.com/google/gemini-cli)
[![Vercel Skills](https://img.shields.io/badge/Vercel-Skills-black)](https://skills.sh)

## 🚀 Instalasi

Pasang kecerdasan PPKI ke proyek Anda menggunakan CLI Vercel Agent Skills:

```bash
npx skills add dzakwanalifi/ppki-ipb
```

*Mendukung 18+ agen AI termasuk Claude Code, Cursor, GitHub Copilot, dan Gemini CLI.*

---

## 🧠 Keahlian yang Tersedia

### `ppki-ipb`
Instruksi terpaket untuk gaya selingkung IPB University.
**Gunakan saat:**
- Menulis atau meninjau draf skripsi, tesis, atau disertasi.
- Mengatur margin, fon, dan struktur sistematika dokumen.
- Membuat daftar pustaka sesuai gaya IPB/APA 7th.

**Kemampuan:**
- **Validasi Tata Letak**: Memastikan pias 4-3-3-3 cm dan tipografi Times New Roman 12pt.
- **Penegakan Terminologi**: Mengotomatiskan penggunaan "Prakata" (bukan Kata Pengantar) dan "Simpulan" (bukan Kesimpulan).
- **Kualitas Kebahasaan**: Mengaudit penggunaan kalimat pasif dan nada akademik formal.

---

## 🛠️ Alat Khusus (Tools)

Paket ini menyertakan skrip deterministik untuk memastikan jawaban agen AI akurat:

- **`search_ppki.py`**: Pencarian basis pengetahuan berbasis BM25 dari pedoman resmi 2024.
- **`check_kbbi.py`**: Integrasi langsung dengan **API KBBI Edisi VI** untuk validasi kata baku.
- **`lint_ppki.py`**: Linter aktif untuk memeriksa kepatuhan draf terhadap gaya selingkung IPB.
- **`fix_ppki.py`**: Alat perbaikan otomatis untuk terminologi, pias, dan konversi kalimat pasif.
- **`init_thesis.py`**: Scaffolder untuk menginisialisasi struktur folder skripsi/tesis standar IPB secara instan.

---

## 📂 Struktur

- `skills/ppki-ipb/SKILL.md`: Instruksi utama dan pemicu (*triggers*) untuk agen.
- `skills/ppki-ipb/references/`: Basis pengetahuan terstruktur per bab.
- `skills/ppki-ipb/assets/`: Skema JSON untuk *grounding* sitasi.
- `scripts/`: Alat otomatisasi berbasis Python.

---

## 📖 Konteks Ilmiah (PPKI 2024)

Meskipun dibangun untuk agen AI, inti kecerdasan ini mengikuti **Pedoman Penulisan Karya Ilmiah IPB University Edisi 2024**:
- **Sistem**: Harvard (Nama-Tahun).
- **Gaya**: CSE 8th (Dimodifikasi).
- **Bahasa**: Indonesia Formal, Kalimat Pasif.

---
*Dikembangkan oleh dzakwanalifi bersama Gemini CLI Agent. Kiblat: Standar Vercel Agent Skills.*
