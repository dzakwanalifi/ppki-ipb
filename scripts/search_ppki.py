import os
import sys
import re
import math
from collections import Counter

class BM25Search:
    def __init__(self, directory="skills/ppki-ipb/references", k1=1.5, b=0.75):
        self.directory = directory
        self.k1 = k1
        self.b = b
        self.docs = []
        self.doc_names = []
        self.doc_lengths = []
        self.avg_dl = 0
        self.corpus_size = 0
        self.df = Counter()
        self.idf = {}
        self._initialize()

    def _tokenize(self, text):
        # Membersihkan markdown dan karakter non-alphanumeric
        text = re.sub(r'[^\w\s]', ' ', text.lower())
        return text.split()

    def _initialize(self):
        all_text_data = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        tokens = self._tokenize(content)
                        self.docs.append(Counter(tokens))
                        self.doc_names.append(os.path.relpath(path, self.directory))
                        self.doc_lengths.append(len(tokens))
                        all_text_data.append(content)
                        # Hitung Document Frequency
                        for token in set(tokens):
                            self.df[token] += 1
        
        self.corpus_size = len(self.docs)
        if self.corpus_size == 0: return

        self.avg_dl = sum(self.doc_lengths) / self.corpus_size
        
        # Hitung IDF (Inverse Document Frequency)
        for token, freq in self.df.items():
            self.idf[token] = math.log((self.corpus_size - freq + 0.5) / (freq + 0.5) + 1)

    def search(self, query, n=5):
        query_tokens = self._tokenize(query)
        scores = []

        for i in range(self.corpus_size):
            score = 0
            doc = self.docs[i]
            doc_len = self.doc_lengths[i]
            
            for token in query_tokens:
                if token in doc:
                    tf = doc[token]
                    idf = self.idf.get(token, 0)
                    # Rumus BM25
                    score += idf * (tf * (self.k1 + 1)) / (tf + self.k1 * (1 - self.b + self.b * (doc_len / self.avg_dl)))
            
            if score > 0:
                scores.append((self.doc_names[i], score))

        # Urutkan berdasarkan skor tertinggi
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:n]

def get_context(query, file_rel_path, directory="skills/ppki-ipb/references"):
    path = os.path.join(directory, file_rel_path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        # Cari potongan teks yang mengandung salah satu kata kunci query
        query_words = query.lower().split()
        for word in query_words:
            match = re.search(f"(?i).{{0,70}}{word}.{{0,70}}", content)
            if match:
                return f"...{match.group(0).replace(os.linesep, ' ')}..."
    return "Match found in document."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_ppki.py <query>")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    search_engine = BM25Search()
    results = search_engine.search(query)

    if not results:
        print(f"Tidak ditemukan hasil untuk: '{query}'")
    else:
        print(f"Hasil pencarian untuk: '{query}' (Terurut berdasarkan relevansi BM25):")
        print("-" * 60)
        for name, score in results:
            context = get_context(query, name)
            print(f"[{name}] (Skor: {score:.2f})")
            print(f"   {context}\n")
