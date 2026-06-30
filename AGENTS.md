# AGENTS.md - PPKI IPB University Writing Standards

This file provides universal context for AI agents working in this repository. 

## Project Identity
**Pedoman Penulisan Karya Ilmiah (PPKI) IPB University**.
Developed by **dzakwanalifi**.
A structured knowledge base and toolset for IPB's official writing standards (2024 Edition).

## Tech Stack
- **Knowledge Base**: Structured Markdown (`skills/ppki-ipb/references/`)
- **Tools**: Python 3.12, Vercel Agent Skills
- **Standards**: IPB University Style (4-3-3-3 margins, Times New Roman 12pt)

## Core Commands
- Search: `python scripts/search_ppki.py "<query>"`
- Thesis Scaffolder: `python scripts/init_thesis.py "<name>"`
- Auto-Fixer: `python scripts/fix_ppki.py "<file>"`
- Citation Converter: `python scripts/cite_ppki.py "<DOI>"`
- Lint/Validate: `python scripts/lint_ppki.py "<file>"`
- KBBI Check: `python scripts/check_kbbi.py "<kata>"`


## Critical Writing Rules (PPKI Compliance)
1. *Language*: Use formal, objective, and passive Indonesian (Bahasa Indonesia Formal). The writing style must be:
   - *Lugas & Sederhana*: Straightforward, direct, avoiding wordiness (bertele-tele), and simple enough to be easily understood.
   - *Objektif & Non-Sastrawi*: Purely scientific, factual, and neutral, without emotional language, metaphors, or poetic elements.
   - *Bebas Taksa (Unambiguous)*: Clear and precise, preventing any double interpretation (multitafsir).
   - *Struktur Kalimat Efektif*: Avoid starting sentences with prepositions like *Dari*, *Dalam*, *Untuk*, *Dengan* if they obscure the subject. Place the subject at the beginning of the sentence.
   - *Objective Diction*: Use neutral, objective words like *menunjukkan* (shows) instead of subjective/opinionated words like *membuktikan* (proves), unless there is a formal mathematical proof. Avoid subjective adjectives, superlatives, or exaggerated overclaims (e.g., *sangat bagus*, *luar biasa*, *terbaik*, *sangat efektif*). Examples to avoid:
      - *membuktikan* -> use *menunjukkan* or *mengindikasikan*
      - *sangat bagus* / *luar biasa* / *terbaik* -> avoid entirely; state the factual results or data instead
      - *sangat efektif* -> use *efektif* (accompanied by quantitative metrics, e.g., *efektif dengan tingkat akurasi sebesar 90%*)
      - *menakjubkan* / *buruk sekali* / *mengerikan* -> avoid entirely as they are emotional words
      - *menurut saya* / *tampaknya* / *mungkin* -> use fact-based statements (e.g., *Berdasarkan data...*, *Hasil pengujian mengindikasikan...*)
   - *Standard Numeric Expressions*: Use standard Indonesian quantifiers like *sebesar* or *sebanyak* instead of colloquial prepositions like *di* when presenting statistical/numerical values (e.g., *sebesar 0,9839* instead of *di 0,9839*).
2. *Sentence Structure*: Use varied sentence lengths (variatif) to avoid monotony.
3. *No Conjunctions at Start*: DO NOT use conjunctions at the very beginning of a paragraph. This includes intra-sentence conjunctions (*dan*, *serta*, *atau*, *tetapi*, *melainkan*, *sedangkan*, *sehingga*, *karena*, *sebab*, *agar*, *supaya*, *bahwa*, *jika*, *apabila*) and inter-sentence conjunctions (*namun*, *akan tetapi*, *oleh karena itu*, *oleh sebab itu*, *dengan demikian*, *selain itu*, *sebaliknya*, *meskipun demikian*).
4. *Formatting*: DO NOT use bold styling (`**bold**` or `__bold__`). Italic styling (`*italic*` or `_italic_`) is allowed.
5. *Terminology*:
   - Always use *Prakata* instead of "Kata Pengantar".
   - Always use *Simpulan* instead of "Kesimpulan".
6. *Layout*:
   - Margins: Left (4cm), Top (3cm), Right (3cm), Bottom (3cm).
   - Fonts: Times New Roman 12pt (Body), 14pt Bold (Chapter Titles).
7. *Citations*: Follow IPB/APA 7th style as documented in `skills/ppki-ipb/references/07_Bab_7_Daftar_Pustaka/`.
   - DO NOT write *et al.* in italics; it must be written in standard roman font (e.g., et al. without markdown asterisks).
   - DO NOT use a comma between the author's name and the year in in-text citations (e.g., `(BPS 2016)` instead of `(BPS, 2016)`).
   - When citing multiple sources, list them in *chronological order* (oldest to newest), separated by a semicolon (e.g., `(Suhardjito 2008; Hutagaol 2009; Mandang 2010)`).
   - Use `dan` for Indonesian text and `and` for English text when citing works by two authors (e.g., `(Naim dan Keraf 2012)` vs `(Naim and Keraf 2012)`).
8. *Abstrak & Abstract*:
   - Must contain: background (latar belakang), objectives (tujuan), methods (metode), results focusing on new findings (hasil), and implications (implikasi).
   - Word count: Under 200 words, written in a single paragraph.
   - English version (*Abstract*) must be written using *past tense* for the research methods and results.
9. *Italics for Foreign Words*: Foreign terms, regional language words, and biological scientific names must be written in italics.
10. *Number Spelling*: Numbers from one to nine expressing quantities must be spelled out as words (e.g., *satu*, *dua*), except when indicating specific measurement units (e.g., *3 kg*, *5 m*). Numbers cannot start a sentence (rephrase the sentence to avoid beginning with a digit).
    - In text, numerical ranges must be separated by the word *sampai* (e.g., *tahun 1974 sampai 1978*), not hyphens or dashes.
    - Semicolons must separate numbers in a decimal list (e.g., *3,4; 0,5; 4,5*).
    - Thousands separator (dot) is used only for numbers with more than four digits (e.g., *37.412*). Four-digit numbers do not use a dot in body text (e.g., *3764*).
11. *Capitalization in Headings*: Chapter titles must be written in all-capital letters (uppercase). Sub-chapter titles must use capitalization only on the first letter of each word, except for grammatical particles and prepositions (such as *di*, *ke*, *dari*, *dan*, *yang*, *untuk*) unless they start the title.
12. *LaTeX Compatibility for Word*: Mathematical formulas must be written in a format compatible with Microsoft Word's LaTeX converter. DO NOT use full block environments like `\begin{equation}` or `\begin{align}`. For matrices, DO NOT use `\begin{matrix}` or `\begin{pmatrix}`; instead, use the simplified `\matrix{}` syntax wrapped in standard brackets, for example: `[\matrix{a & b \\ c & d}]` or `(\matrix{a & b \\ c & d})`.
13. *DILARANG KERAS Menggunakan Gaya Kepenulisan AI (ZERO-TOLERANCE WP:AISIGNS)*: Seluruh hasil penulisan harus bersih 100% dari jejak kepenulisan generatif AI. Pelanggaran terhadap aturan ini merupakan kegagalan fatal kepatuhan PPKI. Patuhi larangan-larangan keras berikut secara mutlak:
    - *Larangan Kosakata AI (Prohibited AI Vocabulary)*: DILARANG menggunakan kata pengisi klise AI baik dalam bahasa Inggris maupun padanan bahasa Indonesianya. Hindari kata-kata seperti: *delve* (*menyelami*, *menelusuri lebih dalam*), *tapestry* (*anyaman*, *rajutan*, *tapestri*), *testament* (*bukti nyata*, *saksi nyata*), *pivotal* / *crucial* / *key* (*sangat penting*, *kunci*, *krusial*), *underscore* / *highlight* (*menggarisbawahi*, *menyoroti*), *foster* (*membina*, *memupuk*, *menumbuhkan*), *intricate* / *complexities* (*seluk-beluk*, *kerumitan*, *kompleksitas*), *landscape* (*lanskap* dalam makna kiasan), *enhance* (*meningkatkan*, *menyempurnakan*), *robust* (*kuat*, *kokoh*, *tangguh*), *vibrant* (*semarak*, *hidup*), *groundbreaking* / *renowned* (*terobosan*, *terkemuka*).
    - *Larangan Kopula Kompleks (Pretentious Copulas)*: DILARANG mengganti kata hubung/kopula sederhana (*adalah*, *merupakan*, atau langsung predikat) dengan kata kerja kompleks yang bersifat promosi/subjektif seperti *berfungsi sebagai*, *berperan sebagai*, *menawarkan*, *menyajikan*, *merepresentasikan*, atau *menandai*.
    - *Larangan Paralelisme Negatif (No Negative Parallelisms)*: DILARANG menggunakan gaya kontras buatan seperti "Bukan hanya X, melainkan juga Y" atau "Tidak sekadar X, tetapi Y". Nyatakan fakta secara langsung dan positif.
    - *Larangan Aturan Tiga (No Rule of Threes)*: DILARANG keras mengelompokkan kata sifat, manfaat, atau frasa penjelas dalam rangkaian tiga unsur berturut-turut (misal: *cepat, tepat, dan akurat*). Variasikan jumlah perincian.
    - *Larangan Penyimpulan Paragraf (No Compulsive Summaries)*: DILARANG menambahkan kalimat penyimpulan pengulangan di akhir paragraf biasa (misal diawali dengan *secara keseluruhan*, *simpulannya*, *dengan demikian*). Paragraf harus diakhiri dengan analisis data atau transisi logis yang mengalir.
    - *Larangan Klaim Bombastis dan Atribusi Samar (No Puffery & Weasel Words)*: DILARANG menggunakan klaim signifikansi berlebih (*warisan abadi*, *sejarah kaya*) dan atribusi tanpa rujukan spesifik (*para ahli berpendapat*, *laporan menunjukkan*). Setiap klaim wajib menyertakan sitasi ilmiah yang valid.


## Boundary Rules
- *NEVER* modify files in `data/raw/` (Original Source).
- *ALWAYS* check `skills/ppki-ipb/references/` before answering questions about IPB writing rules.
- *DO NOT* use first-person pronouns ("Saya", "Kami") in scientific documentation generated for this project.
- Always adhere to the formatting rules (no bold, only italic) when generating user-facing documents or responses.
