# PPKI IPB Agent Skills

A collection of AI agent skills for **IPB University Scientific Writing Standards (PPKI) 2024**. These skills provide packaged instructions and scripts to extend agent capabilities in academic writing, formatting, and Indonesian linguistic validation.

[![AI Compatible](https://img.shields.io/badge/AI-Gemini%20CLI%20|%20Claude%20Code%20|%20Cursor-blueviolet)](https://github.com/google/gemini-cli)
[![Vercel Skills](https://img.shields.io/badge/Vercel-Skills-black)](https://skills.sh)

## 🚀 Installation

Install the PPKI intelligence to your project using the Vercel Agent Skills CLI:

```bash
npx skills add dzakwanalifi/ppki-ipb
```

*Supports 18+ agents including Claude Code, Cursor, GitHub Copilot, and Gemini CLI.*

---

## 🧠 Available Skills

### `ppki-ipb`
Packaged instructions for IPB University's house style.
**Use when:**
- Writing or reviewing undergraduate theses, master's theses, or doctoral dissertations.
- Formatting margins, fonts, and document structures.
- Generating bibliographies according to IPB/APA 7th style.

**Capabilities:**
- **Layout Validation**: Ensures 4-3-3-3 cm margins and Times New Roman 12pt typography.
- **Terminology Enforcement**: Automatically uses "Prakata" instead of "Kata Pengantar" and "Simpulan" instead of "Kesimpulan".
- **Linguistic Quality**: Audits Indonesian passive voice and formal academic tone.

---

## 🛠️ Specialized Tools

This package includes deterministic scripts to ground agent outputs:

- **`search_ppki.py`**: BM25-powered knowledge retrieval from the official 2024 manual.
- **`check_kbbi.py`**: Direct integration with **KBBI Edition VI API** for formal word validation.
- **`lint_ppki.py`**: Active linter to check drafs for house style compliance.
- **`fix_ppki.py`**: Auto-fixer for terminology, margins, and passive voice conversion.
- **`cite_ppki.py`**: Automatic DOI-to-IPB 2024 citation converter.
- **`init_thesis.py`**: Scaffolder to instantly initialize a complete IPB thesis folder structure.

---

## 📂 Structure

- `skills/ppki-ipb/SKILL.md`: Main instructions and triggers for the agent.
- `skills/ppki-ipb/references/`: Structured knowledge base divided by chapters.
- `skills/ppki-ipb/assets/`: JSON schemas for citation grounding.
- `scripts/`: Python-based automation tools.

---

## 📖 Scientific Context (PPKI 2024)

While built for agents, the core intelligence follows the **Pedoman Penulisan Karya Ilmiah IPB University Edisi 2024**:
- **System**: Harvard (Name-Year).
- **Style**: CSE 8th (Modified).
- **Language**: Formal Indonesian, Passive Voice.

---
*Developed by dzakwanalifi in collaboration with Gemini CLI Agent. Kiblat: Vercel Agent Skills Standard.*
