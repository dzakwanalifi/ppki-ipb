---
name: ppki-ipb
description: Pedoman Penulisan Karya Ilmiah (PPKI) IPB University 2024. Use for formatting rules, citation styles (APA 7th), academic writing standards, and evaluating/reviewing/improving Indonesian writing using EYD V.
---

# PPKI IPB Agent Skill (Vercel Skills Compatible)

Official AI-Native knowledge base for **Pedoman Penulisan Karya Ilmiah (PPKI) IPB University**.

## 🚀 When to use this skill
- formatting rules (margins 4-3-3-3, fonts TNR 12pt).
- citation and bibliography styles (IPB/APA-like).
- document structure (Prakata, Simpulan, Daftar Pustaka).
- technical writing for Skripsi, Tesis, or Disertasi.
- reviewing, scoring, correcting, or improving Indonesian writing (KTI, essays, reports) using EYD V, grammar, punctuation, diction, and academic tone.

## 📂 Knowledge Base Structure
This skill uses progressive disclosure via `references/`:
- `01_Bab_1_Pendahuluan`: Writing paradigms (IMRAD, etc.).
- `04_Bab_4_Kebahasaan`: Indonesian grammar, diksi, and style rules.
- `04_Bab_4_Kebahasaan/language-review-guide.md`: Guidance for language evaluation.
- `04_Bab_4_Kebahasaan/eyd-v/`: Full official guidelines of EYD V (PUEBI replacement).
- `05_Bab_5_Tata_Tulis_Teknis/5.0_Ketentuan_Umum_Pengetikan.md`: Margins and fonts.
- `06_Bab_6_Tabel_dan_Gambar`: Standards for illustrations.
- `07_Bab_7_Daftar_Pustaka`: Citation rules (critical).

### 💎 PPKI Standards (JSON Schema)
Always refer to `assets/ppki_standards.json` when generating tables, figures, or references. It contains exact rules for punctuation, margins, and citation styles.

## 🛠️ Specialized Tools
- **Search**: `python scripts/search_ppki.py "<query>"`
- **Lint/Validate**: `python scripts/lint_ppki.py <target_file.md>`
- **Auto-Fixer**: `python scripts/fix_ppki.py <target_file.md>`
  *Automatically corrects terminology, removes periods from titles, and converts first-person pronouns to neutral/passive.*
- **Thesis Scaffolder**: `python scripts/init_thesis.py <project_name>`
  *Initializes a complete IPB thesis folder structure with 7 main sections and placeholder files.*
- **Citation Converter**: `python scripts/cite_ppki.py <DOI>`
  *Fetches metadata via CrossRef and generates a perfectly formatted IPB 2024 citation string.*
- **KBBI Check**: `python scripts/check_kbbi.py "<kata>"`
  *Use this to verify if a word is formal/standard (baku) according to KBBI Edition VI.*

## 🔍 Language Evaluation Workflow
When asked to evaluate or improve Indonesian writing quality:
1. Identify the text type (essay, KTI, abstract, report).
2. Load relevant EYD V rules under `04_Bab_4_Kebahasaan/eyd-v/` and review the guidelines in `04_Bab_4_Kebahasaan/language-review-guide.md`.
3. Evaluate from highest to lowest impact: meaning clarity, academic tone, sentence structure, paragraph flow, then EYD mechanics.
4. Output a correction table:
   | Kutipan | Masalah | Rujukan | Perbaikan |
   | --- | --- | --- | --- |
5. Provide overall quality rating (Sangat Baik / Baik / Cukup / Perlu Revisi Besar), top 3 recurring errors, and a revised sample paragraph.

## 💡 Best Practices
- **Active Validation**: Before finishing a task, run the Linter on the output to ensure compliance.
- **Illustration Rules**: Tables have only 3 horizontal lines and NO vertical lines. Titles for Tables (above) and Figures (below) must NOT end with a period.
- **Technical Notation**: Use comma (,) for decimals. Add a space between number and unit (e.g., 100 kg). Variables should be *italicized*, but units must be upright.
- **Tone**: Always maintain a formal, objective, and passive tone in Indonesian. Avoid first-person pronouns.

