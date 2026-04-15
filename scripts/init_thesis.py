import os
import sys

def init_thesis(project_name="my_thesis"):
    """
    Menginisialisasi struktur proyek skripsi/tesis sesuai standar PPKI IPB 2024.
    """
    structure = {
        "00_Bagian_Awal": [
            "01_Halaman_Sampul.md",
            "02_Halaman_Pengesahan.md",
            "03_Abstrak.md",
            "04_Prakata.md",
            "05_Daftar_Isi.md"
        ],
        "01_Bab_1_Pendahuluan": [
            "1.1_Latar_Belakang.md",
            "1.2_Perumusan_Masalah.md",
            "1.3_Tujuan.md",
            "1.4_Manfaat.md"
        ],
        "02_Bab_2_Tinjauan_Pustaka": [
            "2.1_Landasan_Teori.md"
        ],
        "03_Bab_3_Metode": [
            "3.1_Waktu_dan_Tempat.md",
            "3.2_Alat_dan_Bahan.md",
            "3.3_Prosedur_Kerja.md",
            "3.4_Analisis_Data.md"
        ],
        "04_Bab_4_Hasil_dan_Pembahasan": [
            "4.1_Hasil.md",
            "4.2_Pembahasan.md"
        ],
        "05_Bab_5_Simpulan_dan_Saran": [
            "5.1_Simpulan.md",
            "5.2_Saran.md"
        ],
        "06_Bagian_Akhir": [
            "Daftar_Pustaka.md",
            "Lampiran.md",
            "Riwayat_Hidup.md"
        ]
    }

    if os.path.exists(project_name):
        return f"❌ Folder '{project_name}' sudah ada."

    os.makedirs(project_name)
    
    # Tambahkan file aturan (AGENTS.md kustom untuk proyek tersebut)
    with open(os.path.join(project_name, "AGENTS.md"), "w", encoding="utf-8") as f:
        f.write("# Project Rules\nAlways follow PPKI IPB 2024 standards.\nMargins: 4-3-3-3 cm.\nLanguage: Formal Indonesian, Passive Voice.")

    for folder, files in structure.items():
        folder_path = os.path.join(project_name, folder)
        os.makedirs(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, "w", encoding="utf-8") as f:
                header = file.replace(".md", "").replace("_", " ")
                f.write(f"# {header}\n\n[Tuliskan konten di sini sesuai pedoman PPKI IPB]\n")

    return f"✅ Berhasil menginisialisasi proyek: {project_name}\n🚀 AI sekarang bisa membantu Anda menulis per bab di folder tersebut."

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "my_thesis"
    print(init_thesis(name))
