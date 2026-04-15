# AI Agent Repository for IPB University Scientific Writing Standards (PPKI)

[![AI Compatible](https://img.shields.io/badge/AI-Gemini%20CLI%20|%20Claude%20Code%20|%20Cursor-blueviolet)](https://github.com/google/gemini-cli)
[![Language: Indonesian](https://img.shields.io/badge/Language-Indonesian-red)](README.md)

## PREFACE

This repository is a digitalization of the **IPB University Scientific Writing Standards (PPKI) 2024 Edition**. By implementing *Agent Skill* technology and structured Markdown data, this repository serves as an automated reference for students and researchers at IPB University to produce scientific works that comply with the university's house style. This development is part of an effort to improve the quality and standardization of scientific works in the era of artificial intelligence.

---

## CHAPTER I INTRODUCTION

The demands of the times require a paradigm shift that scientific works must be published as widely as possible. In accordance with the mandate in the KKNI, the quality of undergraduate theses, master's theses, and doctoral dissertations must be suitable for publication in accredited national scientific journals and reputable international journals.

This repository transforms static documents into a knowledge base consumable by AI agents. Thus, AI agents can provide precise writing assistance, ranging from technical formatting to citation ethics, without compromising the author's academic integrity.

---

## CHAPTER II STRUCTURE AND AI AGENT COMPATIBILITY

This repository's structure is designed to support various AI platforms through an *AI-Native* configuration:

1. **Gemini CLI (`.gemini/`)**: An installable skill module for direct procedural instructions in the terminal.
2. **Claude Code (`CLAUDE.md`)**: Persistent memory configuration for the Claude terminal assistant.
3. **Cursor & Windsurf (`.cursor/rules/`)**: Modular rules based on glob patterns for automatic application in IDE environments.
4. **Universal Standard (`AGENTS.md`)**: A 2026 Linux Foundation universal standard readable by almost all modern AI agents (Codex, Copilot, Devin).
5. **Vercel Agent Skills**: Fully compatible with the `npx skills` distribution standard.

---

## CHAPTER III TECHNICAL WRITING STANDARDS (PPKI COMPLIANCE)

All AI agents using this repository are instructed to comply with the following technical provisions:

### 3.1 Margins and Layout
In accordance with Appendix 16 of the PPKI, the typing boundaries on A4 paper (80 grams) are set as follows:
- **Left Margin**: 4 cm (for binding space).
- **Top, Right, and Bottom Margins**: 3 cm each.
- **Line Spacing**: Single spacing (1.0).

### 3.2 Typography and Language
- **Font Type**: Times New Roman 12 points for the main text, and 14 points (Bold) for chapter titles.
- **Writing Style**: Must use formal Indonesian with an objective passive voice. The use of first-person pronouns (I/We) must be avoided.
- **Standard Terminology**: Must use the terms **Prakata** (not Preface/Foreword), **Simpulan** (not Conclusion), and **Daftar Pustaka** (not Bibliography/References).

---

## CHAPTER IV INSTALLATION GUIDE FOR YOUR PROJECT (ULTRA FAST)

The most modern way to install this PPKI intelligence is using the **Vercel Agent Skills CLI**. This command automatically installs *skills* to all AI agents (Cursor, Claude Code, Cline, etc.) simultaneously:

```bash
npx skills add dzakwanalifi/ppki-ipb
```

### Alternative Methods (Manual):

#### 4.1 For Cursor & Windsurf Users
```bash
npx degit dzakwanalifi/ppki-ipb/skills/ppki-ipb/references .cursor/rules --force
```

#### 4.2 For Claude Code Users
```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/dzakwanalifi/ppki-ipb/master/CLAUDE.md
```

---

## CHAPTER V OPERATIONAL GUIDE (TOOLS)

Searching for rules and language validation can be performed via the following terminal commands:

### 5.1 Knowledge Base Search (BM25)
```bash
python scripts/search_ppki.py "<keyword>"
```

### 5.2 Formal Word Check (KBBI VI)
```bash
python scripts/check_kbbi.py "<word>"
```
*This feature connects directly to the KBBI Edition VI API to ensure your diction meets national standards.*

### 5.3 House Style Validation (Linter)
```bash
python scripts/lint_ppki.py <target_file.md>
```

---

## CONCLUSION

The digitalization of the IPB 2024 PPKI into an AI agent repository is a strategic step in facilitating IPB University students to produce high-quality scientific works. With proper integration, the university's house style standards can be consistently maintained throughout all stages of writing.

---

## CREDITS & APPRECIATION

The development of this repository relies on the following external data support:
- **KBBI API (Edition VI)**: Provided by [raf555/kbbi-api](https://github.com/raf555/kbbi-api). Special thanks for providing modern and stable access to Indonesian language data.

---

## BIBLIOGRAPHY

IPB University. 2024. *Pedoman Penulisan Karya Ilmiah Edisi 2024*. Bogor (ID): IPB Press.

---
*Developed by dzakwanalifi in collaboration with Gemini CLI Agent as an AI-Ready repository standard for IPB University.*
