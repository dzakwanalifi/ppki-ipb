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

    def run(self):
        self.check_forbidden_pronouns()
        self.check_terminology()
        self.check_citation_format()
        self.check_margins_mention()
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
