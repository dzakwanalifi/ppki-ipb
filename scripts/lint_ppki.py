import os
import sys
import re

class PPKILinter:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, "r", encoding="utf-8") as f:
            self.content = f.read()
        self.errors = []

    def check_forbidden_pronouns(self):
        """Aturan: Menghindari kata ganti orang pertama (Saya, Kami, Kita)."""
        forbidden = [r"\bSaya\b", r"\bKami\b", r"\bKita\b"]
        for pattern in forbidden:
            matches = re.finditer(pattern, self.content, re.IGNORECASE)
            for match in matches:
                self.errors.append(f"[KEBAHASAAN] Ditemukan kata ganti terlarang: '{match.group(0)}'. Gunakan kalimat pasif.")

    def check_terminology(self):
        """Aturan: Menggunakan istilah baku IPB."""
        terms = {
            r"\bKata Pengantar\b": "Prakata",
            r"\bKesimpulan\b": "Simpulan",
            r"\bReferensi\b": "Daftar Pustaka"
        }
        for pattern, correct in terms.items():
            matches = re.finditer(pattern, self.content, re.IGNORECASE)
            for match in matches:
                self.errors.append(f"[TERMINOLOGI] Gunakan '{correct}' sebagai ganti '{match.group(0)}'.")

    def check_citation_format(self):
        """Aturan: Cek format sitasi dasar (Nama Tahun)."""
        # Mencari sitasi yang salah format, misal (Nama, Tahun) -> IPB tidak pakai koma
        wrong_citations = re.finditer(r"\(\w+, \d{4}\)", self.content)
        for match in wrong_citations:
            self.errors.append(f"[SITASI] Format salah: '{match.group(0)}'. IPB tidak menggunakan koma antara nama dan tahun. Contoh: (Suhardiyanto 2014).")

    def check_margins_mention(self):
        """Cek jika ada penyebutan margin yang salah (harus 4-3-3-3)."""
        if "margin" in self.content.lower():
            if not re.search(r"4.*3.*3.*3", self.content) and not re.search(r"4-3-3-3", self.content):
                self.errors.append("[FORMATTING] Pastikan margin mengikuti aturan IPB: Kiri 4cm, Atas/Kanan/Bawah 3cm (4-3-3-3).")

    def check_illustration_titles(self):
        """Aturan: Judul Tabel dan Gambar TIDAK diakhiri titik."""
        # Mencari pola "Tabel x.x Judul." atau "Gambar x.x Judul."
        titles = re.finditer(r"^(Tabel|Gambar)\s+\d+\.\d+.*?\.\s*$", self.content, re.MULTILINE)
        for match in titles:
            self.errors.append(f"[ILUSTRASI] Judul {match.group(1)} tidak boleh diakhiri tanda titik: '{match.group(0).strip()}'.")

    def check_technical_notation(self):
        """Aturan: Pengecekan angka, satuan, dan operator matematika."""
        # 1. Cek desimal titik (IPB pakai koma)
        # Mencari pola angka.angka (misal 0.24) - berisiko false positive untuk versi/coding
        dots = re.finditer(r"\b\d+\.\d+\b", self.content)
        for match in dots:
            # Kecualikan jika itu bagian dari penomoran (misal 1.1) atau versi
            if not re.search(r"^(Tabel|Gambar|Bab|##)\s", self.content[:match.start()].splitlines()[-1]):
                self.errors.append(f"[NOTASI] Gunakan koma sebagai pemisah desimal: '{match.group(0)}' (Standar IPB).")

        # 2. Cek spasi satuan (misal 100kg -> seharusnya 100 kg)
        units = re.finditer(r"\b\d+(kg|m|s|N|Hz|V|mol|cd|rd|sr)\b", self.content)
        for match in units:
            self.errors.append(f"[NOTASI] Tambahkan spasi antara angka dan satuan: '{match.group(0)}'.")

        # 3. Cek spasi operator (misal x=y -> seharusnya x = y)
        operators = re.finditer(r"\w[=\+\-\*\/]\w", self.content)
        for match in operators:
            self.errors.append(f"[NOTASI] Gunakan spasi sebelum dan sesudah operator: '{match.group(0)}'.")

    def run(self):
        self.check_forbidden_pronouns()
        self.check_terminology()
        self.check_citation_format()
        self.check_margins_mention()
        self.check_illustration_titles()
        self.check_technical_notation()
        return self.errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lint_ppki.py <target_file.md>")
        sys.exit(1)
    
    linter = PPKILinter(sys.argv[1])
    results = linter.run()
    
    if not results:
        print("✅ Dokumen memenuhi standar dasar PPKI IPB.")
    else:
        print(f"❌ Ditemukan {len(results)} potensi ketidaksesuaian PPKI:")
        for err in results:
            print(f"   - {err}")
