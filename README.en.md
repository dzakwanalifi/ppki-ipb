# PPKI IPB Agent Skills

*Read this document in [Indonesian](README.md).*

A collection of AI agent skills for *IPB University Scientific Writing Standards (PPKI) 2024*. This project provides packaged instructions and scripts to extend agent capabilities in academic writing, formatting, and Indonesian linguistic validation.

[![AI Compatible](https://img.shields.io/badge/AI-Gemini%20CLI%20|%20Claude%20Code%20|%20Cursor-blueviolet)](https://github.com/google/gemini-cli)
[![Vercel Skills](https://img.shields.io/badge/Vercel-Skills-black)](https://skills.sh)

## 🚀 Installation

Install the PPKI skill to your project using the Vercel Agent Skills CLI:

```bash
npx skills add dzakwanalifi/ppki-ipb
```

*Supports 18+ agents including Claude Code, Cursor, GitHub Copilot, and Gemini CLI.*

### Options During Interactive Installation

When running the installation command above, you will be offered the following options:
*   *AI Agent Selection*: The system detects active agents (like *Cursor* or *Claude Code*). Select the desired agent using the spacebar.
*   *Installation Scope*: Choose *Local* to enable the skill only for this project, or *Global* for all projects on your system.
*   *Copy Method*: Choose *Symlink* (dynamic link for auto-updates) or *Copy* (physical copy of the files).

You can also bypass the interactive menu by appending CLI arguments directly:
*   *Global Installation*: `npx skills add dzakwanalifi/ppki-ipb -g`
*   *Agent-Specific Installation*: `npx skills add dzakwanalifi/ppki-ipb -a <agent-name>` (e.g., `-a claude-code`)
*   *Copy Without Symlink*: `npx skills add dzakwanalifi/ppki-ipb --copy`
*   *Automatic Approval*: `npx skills add dzakwanalifi/ppki-ipb -y`

### AI Agent Preparation

PPKI Agent Skills can be used if one of the following AI agents is installed on your system:

#### 1. Claude Code
This tool can be run via command line interface (CLI) or graphical user interface (GUI):
*   *GUI Version (Claude Desktop)*:
    Download the official application from the [Claude Download Page](https://claude.ai/download), then use the *Code* tab.
*   *CLI Version (Terminal)*:
    *   *Windows (PowerShell)*: Run `irm https://claude.ai/install.ps1 | iex`
    *   *macOS / Linux (Terminal)*: Run `curl -fsSL https://claude.ai/install.sh | bash`

#### 2. Cursor (AI Editor)
*   Download and install the editor from the official [Cursor website](https://cursor.com).
*   Enable the skills feature via the *Settings > Rules* menu in the *Cursor* application.

#### 3. Antigravity / Gemini CLI
This tool provides both CLI and GUI versions:
*   *GUI Version (Antigravity)*:
    Download the standalone desktop application or *Antigravity IDE* from the [Antigravity Official Site](https://antigravity.google/).
*   *CLI Version*:
    Use the official *Antigravity CLI* or *Gemini CLI* agent integration to execute instructions. The configuration is located in the `.gemini` directory within the user profile folder.

#### 4. OpenAI Codex
This tool provides both GUI and CLI versions:
*   *GUI Version (Codex Desktop)*:
    Download the standalone desktop application from the [OpenAI Codex Official Site](https://chatgpt.com/codex).
*   *CLI/Web Version*:
    Use *Codex CLI* or access via the official web page.

### Installation for Beginners (Without Node.js / npx)

Systems that do not have *Node.js* or *npx* can use one of the methods below:

#### Method A: Install Node.js (Recommended)

Installing *Node.js* will automatically provide *npm* and *npx* commands.

*   *Windows (via PowerShell/CMD)*:
    Run the following command:
    ```powershell
    winget install OpenJS.NodeJS
    ```
    Restart *PowerShell* or *CMD* after the installation is complete. Alternatively, download the *.msi* installer directly from the official *nodejs.org* website.

*   *macOS (via Terminal)*:
    Run the following command:
    ```bash
    brew install node
    ```
    Alternatively, download the *.pkg* installer directly from the official *nodejs.org* website.

Run the main command above to add the skills after the installation is successful.

#### Method B: Manual Installation (Without Node.js Installation)

1.  Copy the *skills/ppki-ipb* folder manually from this project.
2.  Paste the folder into the AI agent configuration directory:
    *   *Cursor (Windows)*: `%USERPROFILE%\.cursor\skills\`
    *   *Cursor (macOS)*: `~/.cursor/skills/`
    *   *Claude Code (Windows)*: `%USERPROFILE%\.claude\skills\`
    *   *Claude Code (macOS)*: `~/.claude/skills/`
3.  Restart the AI agent application to apply the new skill.

---

## 🧠 Available Skills

### `ppki-ipb`
Packaged instructions for IPB University's house style.
*Use when:*
- Writing or reviewing undergraduate theses, master's theses, or doctoral dissertations.
- Formatting margins, fonts, and document structures.
- Generating bibliographies according to IPB/APA 7th style.

*Capabilities:*
- *Layout Validation*: Ensures 4-3-3-3 cm margins and Times New Roman 12pt typography.
- *Terminology Enforcement*: Automatically uses "Prakata" instead of "Kata Pengantar" and "Simpulan" instead of "Kesimpulan".
- *Linguistic Quality*: Audits Indonesian passive voice and formal academic tone.

---

## 🛠️ Specialized Tools

This package includes deterministic scripts to ground agent outputs:

- *search_ppki.py*: BM25-powered knowledge retrieval from the official 2024 manual.
- *check_kbbi.py*: Direct integration with *KBBI Edition VI API* for formal word validation.
- *lint_ppki.py*: Active linter to check drafts for house style compliance.
- *fix_ppki.py*: Auto-fixer for terminology, margins, and passive voice conversion.
- *cite_ppki.py*: Automatic DOI-to-IPB 2024 citation converter.
- *init_thesis.py*: Scaffolder to instantly initialize a complete IPB thesis folder structure.

---

## 📂 Structure

- `skills/ppki-ipb/SKILL.md`: Main instructions and triggers for the agent.
- `skills/ppki-ipb/references/`: Structured knowledge base divided by chapters.
- `skills/ppki-ipb/assets/`: JSON schemas for citation grounding.
- `scripts/`: Python-based automation tools.

---

## 📖 Scientific Context (PPKI 2024)

The core intelligence follows the *Pedoman Penulisan Karya Ilmiah IPB University Edisi 2024* even though it is built for AI agents:
- *System*: Harvard (Name-Year).
- *Style*: CSE 8th (Modified).
- *Language*: Formal Indonesian, Passive Voice.

---
*Developed by dzakwanalifi in collaboration with Gemini CLI Agent. Based on: Vercel Agent Skills Standard.*
