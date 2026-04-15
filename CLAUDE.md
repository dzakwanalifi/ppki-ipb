# CLAUDE.md - Project Knowledge & Commands

## Project: PPKI IPB University Writing Standards

## Build and Search Commands
- Search rules: `python scripts/search_ppki.py "<query>"`
- Thesis Scaffolder: `python scripts/init_thesis.py "<name>"`
- Auto-Fixer: `python scripts/fix_ppki.py "<file>"`
- Citation Converter: `python scripts/cite_ppki.py "<DOI>"`
- Lint/Validate: `python scripts/lint_ppki.py "<file>"`
- KBBI Check: `python scripts/check_kbbi.py "<kata>"`
- Repack skill: `node C:\Users\dzakw\AppData\Local\nvm\v22.14.0\node_modules\@google\gemini-cli\bundle\builtin\skill-creator\scripts\package_skill.cjs ppki-ipb .`

## Style Guidelines
- **Language**: Formal Indonesian (Bahasa Indonesia Formal).
- **Voice**: Passive voice only (e.g., "Penelitian dilakukan" instead of "Kami meneliti").
- **Key Terms**:
  - `Prakata` (NOT `Kata Pengantar`)
  - `Simpulan` (NOT `Kesimpulan`)
  - `Daftar Pustaka` (NOT `Referensi`)

## Architecture
- `skills/ppki-ipb/references/`: Primary knowledge base for writing standards.
- `scripts/`: Tooling for searching and cleaning the knowledge base.
- `.gemini/`: Packaged skills for Gemini CLI.

## Core Rules
- Margin: Left 4cm, others 3cm.
- Font: Times New Roman 12pt (Body).
- Citation: IPB/APA 7th.
