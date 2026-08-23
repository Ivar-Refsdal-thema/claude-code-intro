# Claude Code intro — live demo kit

Companion repo for the "Introduksjon til Claude Code" course. Four demos, each in
its own folder with a `DEMO.md` presenter script and copy-paste prompts.

| # | Folder | Shows | Deck slides |
|---|--------|-------|-------------|
| 1 | [`demo-1-interfaces/`](demo-1-interfaces/DEMO.md) | Terminal, VS Code, Desktop app — same session, three UIs | 6–7 |
| 2 | [`demo-2-modes/`](demo-2-modes/DEMO.md) | Plan mode + auto-accept vs. fully manual mode | 8–13 |
| 3 | [`demo-3-claude-md/`](demo-3-claude-md/DEMO.md) | `/init`, CLAUDE.md, docs/, .claude/ structure | 14–18 |
| 4 | [`demo-4-extensions/`](demo-4-extensions/DEMO.md) | MCP, a skill, a hook, a subagent | 19–23 |

Run them in order. Each `DEMO.md` has the exact prompt(s) to paste and a short
regie note on what to narrate while Claude works.

## Quick reference (slide 25 cheat sheet)

- **Shift+Tab** — cycle normal → auto-accept → plan mode
- **Esc** — interrupt immediately; **Esc Esc** — rewind the conversation
- **/clear** — wipe context, new task; **/compact** — summarize and keep going
- **/context** — see what's filling the context window
- **/init** — generate a first-draft CLAUDE.md
- **/model** — switch model mid-session; **/mcp**, **/hooks** — manage extensions
- **#** — write a line straight into CLAUDE.md without opening it
- **!** — run a shell command without leaving Claude Code
