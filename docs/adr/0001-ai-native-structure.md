# 1. AI-Native Repository Structure

Date: 2026-04-15

## Status
Accepted

## Context
Standard documentation (README only) is often insufficient for modern AI agents (Gemini CLI, Claude Code, Cursor, Copilot) to provide precise, project-specific guidance, especially for strict academic standards like IPB University's PPKI.

## Decision
We decided to adopt an **AI-Native Repository Structure** by implementing:
1. **Universal Context**: Using `AGENTS.md` (2026 Linux Foundation standard) for cross-tool compatibility.
2. **Tool-Specific Rules**: Implementing `CLAUDE.md` for terminal-based agents and `.cursor/rules/*.mdc` for IDE-based agents.
3. **Structured Knowledge Base**: Separating raw source data (`data/raw`) from machine-ready structured data (`data/structured`).
4. **Procedural Automation**: Encapsulating rules into a Gemini CLI `.skill` file.

## Consequences
- **Positive**: AI agents will provide 90%+ accurate formatting advice without manual prompting.
- **Positive**: The knowledge base is modular and searchable via `scripts/search_ppki.py`.
- **Negative**: Maintainers must keep multiple rule files (`CLAUDE.md`, `AGENTS.md`, `.cursor/rules`) in sync.
