# AGENTS.md - PPKI IPB University Writing Standards

This file provides universal context for AI agents working in this repository. 

## Project Identity
**Pedoman Penulisan Karya Ilmiah (PPKI) IPB University**.
A structured knowledge base and toolset for IPB's official writing standards (2024 Edition).

## Tech Stack
- **Knowledge Base**: Structured Markdown (`data/structured/`)
- **Tools**: Python 3.12, Gemini CLI Skills
- **Standards**: IPB University Style (4-3-3-3 margins, Times New Roman 12pt)

## Core Commands
- **Search**: `python scripts/search_ppki.py "<query>" -d data/structured`
- **Clean Data**: `python scripts/clean_md.py`
- **Split Data**: `python scripts/split_md.py`

## Critical Writing Rules (PPKI Compliance)
1. **Language**: Use formal, objective, and passive Indonesian (Bahasa Indonesia Formal).
2. **Terminology**:
   - Always use **"Prakata"** instead of "Kata Pengantar".
   - Always use **"Simpulan"** instead of "Kesimpulan".
3. **Layout**:
   - Margins: Left (4cm), Top (3cm), Right (3cm), Bottom (3cm).
   - Fonts: Times New Roman 12pt (Body), 14pt Bold (Chapter Titles).
4. **Citations**: Follow IPB/APA 7th style as documented in `data/structured/07_Bab_7_Daftar_Pustaka/`.

## Boundary Rules
- **NEVER** modify files in `data/raw/` (Original Source).
- **ALWAYS** check `data/structured/` before answering questions about IPB writing rules.
- **DO NOT** use first-person pronouns ("Saya", "Kami") in scientific documentation generated for this project.
