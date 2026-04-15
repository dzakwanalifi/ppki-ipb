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
- `07_Bab_7_Daftar_Pustaka`: Citation rules (critical).

### 💎 Citation Standard (JSON Schema)
Always refer to `assets/citation_schemas.json` when generating or correcting references. It contains exact templates for Journals, Books, and Theses.

## 🛠️ Specialized Tools
- **Search**: `python scripts/search_ppki.py "<query>"`
- **Lint/Validate**: `python scripts/lint_ppki.py <target_file.md>`
  *Use this to check user drafts for passive voice, terminology (Prakata/Simpulan), and citation errors.*

## 💡 Best Practices
- **Active Validation**: Before finishing a task, run the Linter on the output to ensure compliance.
- **Citation Grounding**: Use the JSON examples as a guide for punctuation (no dots in initials).
- **Tone**: Always maintain a formal, objective, and passive tone in Indonesian.
