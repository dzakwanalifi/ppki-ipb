---
name: ppki-ipb
description: Pedoman Penulisan Karya Ilmiah (PPKI) IPB University 2024. Use for formatting rules, citation styles (APA 7th), and academic writing standards at IPB.
---

# PPKI IPB Agent Skill (Vercel Skills Compatible)

Official AI-Native knowledge base for **Pedoman Penulisan Karya Ilmiah (PPKI) IPB University**.

## 🚀 When to use this skill
- formatting rules (margins 4-3-3-3, fonts TNR 12pt).
- citation and bibliography styles (IPB/APA-like).
- document structure (Prakata, Simpulan, Daftar Pustaka).
- technical writing for Skripsi, Tesis, or Disertasi.

## 📂 Knowledge Base Structure
This skill uses progressive disclosure via `references/`:
- `01_Bab_1_Pendahuluan`: Writing paradigms (IMRAD, etc.).
- `05_Bab_5_Tata_Tulis_Teknis/5.0_Ketentuan_Umum_Pengetikan.md`: Margins and fonts.
- `06_Bab_6_Tabel_dan_Gambar`: Standards for illustrations.
- `07_Bab_7_Daftar_Pustaka`: Citation rules (critical).

### 💎 PPKI Standards (JSON Schema)
Always refer to `assets/ppki_standards.json` when generating tables, figures, or references. It contains exact rules for punctuation, margins, and citation styles.

## 🛠️ Specialized Tools
- **Search**: `python scripts/search_ppki.py "<query>"`
- **Lint/Validate**: `python scripts/lint_ppki.py <target_file.md>`
- **KBBI Check**: `python scripts/check_kbbi.py "<kata>"`
  *Use this to verify if a word is formal/standard (baku) according to KBBI Edition VI.*

## 💡 Best Practices
- **Active Validation**: Before finishing a task, run the Linter on the output to ensure compliance.
- **Illustration Rules**: Tables have only 3 horizontal lines and NO vertical lines. Titles for Tables (above) and Figures (below) must NOT end with a period.
- **Tone**: Always maintain a formal, objective, and passive tone in Indonesian.
