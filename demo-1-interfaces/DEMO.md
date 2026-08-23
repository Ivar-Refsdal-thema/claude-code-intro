# Demo 1 — Terminal, VS Code, Desktop app

**Goal:** show the same Claude Code session working across the three interfaces
(slide 6). Don't rebuild the game three times — build it once, then reuse the
session/folder to show the other two UIs.

## Steps

1. Open a terminal in `demo-1-interfaces/tic-tac-toe/` and start Claude Code.
2. Paste the prompt below and let it build.
3. Once it's built and working, open the **same folder** in VS Code (Claude
   Code extension) and resume the session (`claude -c` or the extension's
   "resume" option) — point out the diff view and file tree updating live.
4. Open the **Desktop app**, point it at the same folder, resume again — show
   the GUI affordances (mode switch by click, no keyboard needed).

## Prompt to paste

```
Create a simple, fully playable tic-tac-toe game in Python that runs in the
terminal. Two players take turns entering a row and column, the board is
printed after each move, and it detects a win or a draw and ends the game.
```

## Talking points

- Terminal: full functionality, gets updates first, best for people who live
  in the shell.
- VS Code: same keyboard-driven interaction, but you see the file tree and
  diffs update in your normal editor.
- Desktop app: lowest barrier to entry, mouse-driven mode switching, good for
  non-coders or one-off tasks (e.g. installing something, pulling data from an
  API) where you don't need to touch the code afterwards.
