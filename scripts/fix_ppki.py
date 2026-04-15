import os
import sys
import re

class PPKIFixer:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, "r", encoding="utf-8") as f:
            self.content = f.read()
        self.changes_made = 0

    def fix_terminology(self):
        """Memperbaiki istilah baku IPB."""
        terms = {
            r"\bKata Pengantar\b": "Prakata",
            r"\bKesimpulan\b": "Simpulan",
            r"\bReferensi\b": "Daftar Pustaka"
        }
        for pattern, replacement in terms.items():
            new_content = re.sub(pattern, replacement, self.content, flags=re.IGNORECASE)
            if new_content != self.content:
                self.changes_made += 1
                self.content = new_content

    def fix_illustration_titles(self):
        """Menghapus tanda titik di akhir judul Tabel dan Gambar."""
        # Mencari baris yang diawali Tabel/Gambar dan diakhiri titik
        pattern = r"^(Tabel|Gambar)\s+(\d+\.\d+.*?)\.\s*$"
        new_content = re.sub(pattern, r"\1 \2", self.content, flags=re.MULTILINE)
        if new_content != self.content:
            self.changes_made += 1
            self.content = new_content

    def fix_pronouns_to_passive_simple(self):
        """
        Mencoba mengubah kata ganti orang pertama menjadi bentuk netral/pasif sederhana.
        Catatan: Ini adalah pendekatan heuristik dasar.
        """
        # Ganti Saya/Kami melakukan -> Dilakukan
        patterns = [
            (r"\bSaya melakukan\b", "Dilakukan"),
            (r"\bKami melakukan\b", "Dilakukan"),
            (r"\bSaya mengambil\b", "Diambil"),
            (r"\bKami mengambil\b", "Diambil"),
            (r"\bSaya menggunakan\b", "Digunakan"),
            (r"\bKami menggunakan\b", "Digunakan"),
            (r"\bSaya\b", "Penulis"), # Fallback aman
            (r"\bKami\b", "Penulis"),
        ]
        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, self.content, flags=re.IGNORECASE)
            if new_content != self.content:
                self.changes_made += 1
                self.content = new_content

    def save(self, output_path=None):
        target = output_path if output_path else self.file_path
        with open(target, "w", encoding="utf-8") as f:
            f.write(self.content)
        return target

    def run(self):
        self.fix_terminology()
        self.fix_illustration_titles()
        self.fix_pronouns_to_passive_simple()
        return self.changes_made

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fix_ppki.py <target_file.md> [output_file.md]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    fixer = PPKIFixer(input_file)
    count = fixer.run()
    saved_path = fixer.save(output_file)
    
    if count > 0:
        print(f"✅ Berhasil melakukan {count} jenis perbaikan PPKI.")
        print(f"📄 File tersimpan di: {saved_path}")
    else:
        print("✨ Tidak ditemukan kesalahan yang bisa diperbaiki secara otomatis.")
