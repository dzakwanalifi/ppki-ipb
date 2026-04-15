import sys
import json
import urllib.request
import urllib.parse

def check_kbbi(word):
    """
    Mengecek kata di KBBI Edisi VI melalui API komunitas yang stabil.
    API Source: https://kbbi.raf555.dev/
    Original Repo: https://github.com/raf555/kbbi-api
    """
    encoded_word = urllib.parse.quote(word.lower())
    url = f"https://kbbi.raf555.dev/api/v1/entry/{encoded_word}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
            if not data.get("entries"):
                return f"❌ Kata '{word}' tidak ditemukan di KBBI VI."
            
            result = [f"📖 Hasil KBBI VI untuk: '{word}'"]
            for i, entry in enumerate(data["entries"], 1):
                lema = entry.get("entry", word)
                result.append(f"\n{i}. Lema: {lema}")
                for d in entry.get("definitions", []):
                    pos = f"[{d['label']}]" if d.get("label") else ""
                    result.append(f"   - {pos} {d['definition']}")
                    if d.get("examples"):
                        result.append(f"     Contoh: {', '.join(d['examples'])}")
            
            return "\n".join(result)
            
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"❌ Kata '{word}' tidak ditemukan di KBBI VI."
        return f"⚠️ Terjadi kesalahan server (HTTP {e.code})."
    except Exception as e:
        return f"⚠️ Gagal menghubungi API: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_kbbi.py <kata>")
        sys.exit(1)
    
    word_to_check = sys.argv[1]
    print(check_kbbi(word_to_check))
