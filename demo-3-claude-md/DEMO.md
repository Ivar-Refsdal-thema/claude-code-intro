# Demo 3 — CLAUDE.md, docs/, .claude/

**Goal:** show how CLAUDE.md gets built and how it should evolve (slides
14–18), using `battery-stacker/` — a small, real, working project that has no
CLAUDE.md yet.

Before the session: `cd battery-stacker && pip install -r requirements.txt &&
pytest` to confirm everything works on the presenting machine.

## Steps

1. Open a terminal in `demo-3-claude-md/battery-stacker/`, start Claude Code.
2. Run `/init`. Read the generated CLAUDE.md together — point out what it got
   right (run/test commands, project layout) automatically from the code.
3. Prompt: *"Add a rule to CLAUDE.md: round-trip efficiency losses are applied
   on discharge only, not on charge — see `daily_dispatch` in model.py."* — the
   one non-obvious domain rule `/init` can't infer on its own. This is also a
   good moment to show `#` as a shortcut: type `# efficiency losses only apply
   on discharge, not charge` directly at the prompt to write straight into
   CLAUDE.md without opening the file.
4. Prompt: *"CLAUDE.md is getting long. Move the explanation of the dispatch
   algorithm into `docs/algorithm.md`, and leave a one-line pointer to it from
   CLAUDE.md."* — shows the CLAUDE.md/docs split from slide 15.
5. Show `.claude/settings.json` vs `.claude/settings.local.json`: the former
   is shared/checked in, the latter is personal and belongs in `.gitignore`.
6. Mention the same structure exists globally at `~/.claude/` for
   cross-project rules and personal habits (slide 17): project rules in the
   repo, personal habits at the user level.

## Talking points

- `/init` gives you a first draft, not a finished product — it should be
  iterated on, not left alone.
- Write what isn't obvious from the code: the *why*, not the *what*.
- If you've explained the same project-specific thing three times, it belongs
  in CLAUDE.md.
- Keep CLAUDE.md short — it's loaded into every single session, even before
  you've asked anything.
