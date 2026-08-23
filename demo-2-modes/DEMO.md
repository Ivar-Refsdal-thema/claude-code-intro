# Demo 2 — Modes: Plan+Auto vs. Manual

**Goal:** show how much friction the mode choice adds or removes (slides 8–13),
using two comparable power-market tasks so the *process* difference is what
stands out, not the task difficulty.

## Task A — Plan mode + auto-accept

Folder: `demo-2-modes/task-a-clean-spark-spread/`

1. Open a terminal there and start Claude Code.
2. Press **Shift+Tab** until you're in **Plan mode**.
3. Paste the prompt below. Read the plan out loud, approve it.
4. Press **Shift+Tab** again to switch to **auto-accept edits**, let it run to
   completion without approving each step.
5. Run `/context` afterwards — note how little back-and-forth there was.

```
Create a Python script `spark_spread.py` that reads an hourly CSV with columns
timestamp, power_price_eur_mwh, gas_price_eur_mwh, carbon_price_eur_t. Compute
the clean spark spread per hour as:
  power_price - (gas_price / thermal_efficiency) - carbon_price * emission_factor
Default thermal_efficiency=0.50 and emission_factor=0.202 (t CO2 per MWh gas
input), both overridable as CLI arguments. Write a new CSV with the spread
column added, and print summary stats (mean, min, max, % of hours positive).
If no input CSV is given, generate ~48 hours of realistic sample data first.
```

## Task B — Default manual mode

Folder: `demo-2-modes/task-b-merit-order/`

1. Open a terminal there and start Claude Code in the **default** mode (no
   auto-accept, no plan mode — just Shift+Tab back to normal if needed).
2. Paste the prompt below. Approve every file edit and command individually —
   narrate that this is the "safe but slower" mode from slide 10.

```
Create a Python script `merit_order.py`. It takes a CSV of power plants
(columns: name, capacity_mw, marginal_cost_eur_mwh) and an hourly demand CSV
(columns: timestamp, demand_mw). For each hour, dispatch plants in increasing
order of marginal cost until demand is met, and report which plants ran, their
output in MW, and the system marginal price (the marginal cost of the last
plant dispatched that hour). Write an hourly dispatch CSV and print the total
cost per day. If no input CSVs are given, generate small sample plant and
demand data first.
```

## Talking points

- Plan mode catches misunderstandings while they're still cheap to fix — read
  the plan before approving.
- Auto-accept is now Claude Code's default and, per Anthropic, is on average
  a better judge of what's safe to just do than constant manual approval.
- Manual mode is the safest default when you don't know the codebase well yet,
  but the friction is real — that's the point of this comparison.
- Bigger the task, the more plan mode pays off; for small tasks, auto mode
  alone is often enough.
