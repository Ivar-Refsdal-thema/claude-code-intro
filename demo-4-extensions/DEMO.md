# Demo 4 — MCP, skill, hook, subagent

**Goal:** show the four extension points from slides 19–23. Everything here is
created live — nothing is pre-built in this folder on purpose.

Run this demo from the repo root (`claude-code-intro/`) so the generated
`.claude/` and `.mcp.json` files land at the project root.

**Before the session:** run `claude mcp list` — if `github` is already
configured globally on your machine, the "add" step below won't look new.
Either run `claude mcp remove github` beforehand so the live add is genuine,
or swap in a different server name for the demo.

## 1. MCP

```bash
claude mcp add --scope project --transport http github https://api.githubcopilot.com/mcp/
```

Inside the session:

```
/mcp
```

Select `github`, complete the browser OAuth sign-in (no token typed or shown
on screen). Then from the shell:

```bash
claude mcp list
```

to show it's now tracked in `.mcp.json`. Mention Context7 as a contrast — it's
a claude.ai connector, needs no manual `add`, just shows up in `/mcp`.

## 2. Hook — notify when Claude is done

Paste into Claude Code:

```
Add a Claude Code hook to .claude/settings.json that fires on the Stop event
and shows a Windows toast notification with the text "Claude Code is done".
Use the BurntToast PowerShell module if it's installed; otherwise fall back
to a simple msg-style notification so it still works without BurntToast.
```

Then trigger it by finishing any turn and confirm the toast appears.

## 3. Skill — commit my way

Paste into Claude Code:

```
Create a Claude Code skill at .claude/skills/commit/SKILL.md called `commit`.
When invoked it should:
- run the project's test command if one is discoverable, and stop if tests fail
- stage only the files relevant to the change (never `git add -A`)
- write a Conventional Commits message: a type prefix (feat/fix/chore/docs/
  refactor/test), a short imperative summary line under 72 characters, and a
  body only if the change needs explaining
- NOT add any AI/co-author attribution line
- then create the commit and show the result
```

Demo it by making a trivial change somewhere in this repo and invoking the
skill (`/commit` or by describing the task), then inspect the resulting commit
message format.

## 4. Subagent — test runner

Paste into Claude Code:

```
Create a Claude Code subagent at .claude/agents/test-runner.md called
`test-runner`. Its job: auto-detect and run the project's test suite (pytest,
npm test, etc.), and report back a concise pass/fail summary with the names
and error messages of any failing tests. It must never edit code itself —
only report findings to the main session.
```

Demo it against `../demo-3-claude-md/battery-stacker/`: ask the main session
to delegate a test run to `test-runner` and confirm it reports results without
touching any files.

## Talking points

- A hook is code that always runs on an event — unlike a CLAUDE.md rule, it
  can't be missed or forgotten.
- You don't have to hand-write skills or agents — describe what you just did
  and ask Claude to turn it into one.
- MCP moves Claude from working on your code to working in the systems around
  it — be deliberate about which servers stay connected, they cost context.
