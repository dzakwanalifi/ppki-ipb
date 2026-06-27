# PPKI IPB Agent Skills

*Baca dokumen ini dalam [Bahasa Inggris](README.en.md).*

Kumpulan keahlian agen AI (*Agent Skills*) untuk *Pedoman Penulisan Karya Ilmiah (PPKI) IPB University 2024*. Proyek ini menyediakan instruksi dan skrip yang telah dikemas untuk memperluas kemampuan agen AI dalam penulisan akademik, pemformatan pias, dan validasi bahasa Indonesia.

[![AI Compatible](https://img.shields.io/badge/AI-Gemini%20CLI%20|%20Claude%20Code%20|%20Cursor-blueviolet)](https://github.com/google/gemini-cli)
[![Vercel Skills](https://img.shields.io/badge/Vercel-Skills-black)](https://skills.sh)

## 🚀 Pemasangan

Pasang keahlian PPKI ke proyek Anda menggunakan CLI Vercel Agent Skills:

```bash
npx skills add dzakwanalifi/ppki-ipb
```

*Mendukung 18+ agen AI termasuk Claude Code, Cursor, GitHub Copilot, dan Gemini CLI.*

### Pilihan Selama Pemasangan Interaktif

Saat menjalankan perintah pemasangan di atas, beberapa opsi berikut akan ditawarkan:
*   *Pemilihan Agen AI*: Sistem akan mendeteksi agen yang aktif (seperti *Cursor* atau *Claude Code*). Pilih agen dengan tombol spasi.
*   *Cakupan Pemasangan*: Pilih *Local* untuk mengaktifkan keahlian hanya pada proyek ini, atau *Global* untuk semua proyek di sistem Anda.
*   *Metode Penyalinan*: Pilih *Symlink* (tautan dinamis untuk pembaruan otomatis) atau *Copy* (salinan fisik berkas).

Anda juga dapat melewati menu interaktif dengan menambahkan parameter langsung:
*   *Instalasi Global*: `npx skills add dzakwanalifi/ppki-ipb -g`
*   *Instalasi Khusus Agen*: `npx skills add dzakwanalifi/ppki-ipb -a <nama-agen>` (misal: `-a claude-code`)
*   *Salin Tanpa Symlink*: `npx skills add dzakwanalifi/ppki-ipb --copy`
*   *Persetujuan Otomatis*: `npx skills add dzakwanalifi/ppki-ipb -y`

### Persiapan Agen AI

Keahlian (*skills*) PPKI dapat digunakan apabila salah satu agen AI berikut telah terpasang pada sistem:

#### 1. Claude Code
Alat bantu ini dapat dijalankan melalui antarmuka baris perintah (*CLI*) maupun antarmuka grafis (*GUI*):
*   *Versi GUI (Claude Desktop)*:
    Unduh aplikasi resmi melalui halaman [Halaman Unduhan Claude](https://claude.ai/download), lalu gunakan tab *Code*.
*   *Versi CLI (Terminal)*:
    *   *Windows (PowerShell)*: Jalankan `irm https://claude.ai/install.ps1 | iex`
    *   *macOS / Linux (Terminal)*: Jalankan `curl -fsSL https://claude.ai/install.sh | bash`

#### 2. Cursor (Editor AI)
*   Unduh dan pasang editor melalui situs resmi [Cursor](https://cursor.com).
*   Aktifkan fitur keahlian melalui menu *Settings > Rules* pada aplikasi *Cursor*.

#### 3. Antigravity / Gemini CLI
Alat bantu ini menyediakan versi antarmuka baris perintah (*CLI*) maupun grafis (*GUI*):
*   *Versi GUI (Antigravity)*:
    Unduh aplikasi desktop mandiri atau *Antigravity IDE* melalui [Situs Resmi Antigravity](https://antigravity.google/).
*   *Versi CLI*:
    Gunakan integrasi agen *Antigravity CLI* atau *Gemini CLI* resmi untuk mengeksekusi instruksi. Konfigurasi diletakkan pada direktori `.gemini` di dalam direktori profil pengguna.

#### 4. OpenAI Codex
Alat bantu ini menyediakan versi antarmuka grafis (*GUI*) maupun baris perintah (*CLI*):
*   *Versi GUI (Codex Desktop)*:
    Unduh aplikasi desktop mandiri melalui [Situs Resmi OpenAI Codex](https://chatgpt.com/codex).
*   *Versi CLI/Web*:
    Gunakan *Codex CLI* atau akses melalui halaman web resmi.

### Pemasangan bagi Pemula (Tanpa Node.js / npx)

Sistem yang belum memiliki *Node.js* atau *npx* dapat menggunakan salah satu metode di bawah ini:

#### Metode A: Memasang Node.js (Rekomendasi)

Pemasangan *Node.js* akan secara otomatis menyediakan perintah *npm* dan *npx*.

*   *Windows (via PowerShell/CMD)*:
    Jalankan perintah berikut:
    ```powershell
    winget install OpenJS.NodeJS
    ```
    Muat ulang *PowerShell* atau *CMD* setelah pemasangan selesai. Pilihan lain, unduh berkas pemasang *.msi* langsung dari situs resmi *nodejs.org*.

*   *macOS (via Terminal)*:
    Jalankan perintah berikut:
    ```bash
    brew install node
    ```
    Pilihan lain, unduh berkas pemasang *.pkg* langsung dari situs resmi *nodejs.org*.

Jalankan perintah utama di atas untuk menambahkan keahlian setelah pemasangan berhasil.

#### Metode B: Pemasangan Manual (Tanpa Pemasangan Node.js)

1.  Salin folder *skills/ppki-ipb* secara manual dari proyek ini.
2.  Tempel folder tersebut ke dalam direktori konfigurasi agen AI:
    *   *Cursor (Windows)*: `%USERPROFILE%\.cursor\skills\`
    *   *Cursor (macOS)*: `~/.cursor/skills/`
    *   *Claude Code (Windows)*: `%USERPROFILE%\.claude\skills\`
    *   *Claude Code (macOS)*: `~/.claude/skills/`
3.  Muat ulang aplikasi agen AI untuk menerapkan keahlian baru tersebut.

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
- **`cite_ppki.py`**: Konverter otomatis DOI menjadi format Daftar Pustaka IPB 2024 yang presisi.
- **`init_thesis.py`**: Scaffolder untuk menginisialisasi struktur folder skripsi/tesis standar IPB secara instan.

---

## 📂 Struktur

- `skills/ppki-ipb/SKILL.md`: Instruksi utama dan pemicu (*triggers*) untuk agen.
- `skills/ppki-ipb/references/`: Basis pengetahuan terstruktur per bab.
- `skills/ppki-ipb/assets/`: Skema JSON untuk *grounding* sitasi.
- `scripts/`: Alat otomatisasi berbasis Python.

---

## 📖 Konteks Ilmiah (PPKI 2024)

Inti kecerdasan ini mengikuti *Pedoman Penulisan Karya Ilmiah IPB University Edisi 2024* meskipun dibangun untuk agen AI:
- *Sistem*: Harvard (Nama-Tahun).
- *Gaya*: CSE 8th (Dimodifikasi).
- *Bahasa*: Indonesia Formal, Kalimat Pasif.

---
*Dikembangkan oleh dzakwanalifi bersama Gemini CLI Agent. Mengacu pada: Standar Vercel Agent Skills.*
