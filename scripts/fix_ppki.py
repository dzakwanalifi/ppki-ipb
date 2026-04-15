import os
import sys
import json
from google import genai
from google.genai import types

class PPKIFixerLLM:
    def __init__(self, file_path):
        self.file_path = file_path
        # Mengambil API Key dari Environment Variable
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("❌ API Key tidak ditemukan. Pastikan GEMINI_API_KEY sudah diset di environment.")
        
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-3.1-flash-lite-preview"
        
        # Load skill instructions for system prompt
        skill_path = "skills/ppki-ipb/SKILL.md"
        with open(skill_path, "r", encoding="utf-8") as f:
            self.skill_instructions = f.read()
        
        # Load standards for grounding
        standards_path = "skills/ppki-ipb/assets/ppki_standards.json"
        with open(standards_path, "r", encoding="utf-8") as f:
            self.standards = f.read()

    def run_llm_fix(self):
        prompt = f"""
        Tugas Anda adalah sebagai Senior Editor Pedoman Penulisan Karya Ilmiah (PPKI) IPB University.
        Anda harus mengoreksi naskah dengan tingkat ketelitian 100%.
        
        PANDUAN UTAMA (SKILL INSTRUCTIONS):
        {self.skill_instructions}
        
        STANDAR TEKNIS (JSON):
        {self.standards}
        
        CONTOH PERBAIKAN (FEW-SHOT):
        - Input: "Saya melakukan pengamatan pada 10.5 kg sampel."
        - Output: "Pengamatan dilakukan pada 10,5 kg sampel." (Alasan: Pasif + Desimal Koma)
        
        - Input: "Tabel 1.1 Hasil Penelitian."
        - Output: "Tabel 1.1 Hasil Penelitian" (Alasan: Judul tabel di atas tanpa titik)
        
        PROSEDUR KERJA (CHAIN-OF-VERIFICATION):
        1. Identifikasi semua pelanggaran aturan (Saya/Kami, Istilah Baku, Desimal Titik, Judul Ber-titik).
        2. Lakukan perbaikan draf pertama.
        3. Verifikasi ulang draf tersebut terhadap Standar Teknis JSON.
        4. Pastikan makna asli tidak berubah, hanya gaya bahasanya saja.
        
        TEKS UNTUK DIKOREKSI:
        ---
        {self.content}
        ---
        
        Kembalikan output HANYA dalam format JSON:
        {{
            "fixed_content": "teks markdown akhir yang sudah diverifikasi",
            "changes_count": jumlah_perubahan,
            "detected_errors": ["list kesalahan yang ditemukan"],
            "explanation": "ringkasan perbaikan"
        }}
        """

        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )
            
            result = json.loads(response.text)
            self.content = result.get("fixed_content", self.content)
            return result.get("changes_count", 0), result.get("explanation", "")
            
        except Exception as e:
            print(f"⚠️ Error saat memanggil Gemini API: {str(e)}")
            return 0, str(e)

    def save(self, output_path=None):
        target = output_path if output_path else self.file_path
        with open(target, "w", encoding="utf-8") as f:
            f.write(self.content)
        return target

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fix_ppki.py <target_file.md> [output_file.md]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        fixer = PPKIFixerLLM(input_file)
        print(f"🤖 Mengoreksi menggunakan Gemini 3.1 Flash-Lite...")
        count, explanation = fixer.run_llm_fix()
        saved_path = fixer.save(output_file)
        
        if count > 0:
            print(f"✅ Berhasil melakukan {count} perbaikan otomatis.")
            print(f"📝 Penjelasan: {explanation}")
            print(f"📄 File tersimpan di: {saved_path}")
        else:
            print("✨ Dokumen sudah terlihat sangat bagus sesuai standar PPKI.")
    except Exception as e:
        print(str(e))
