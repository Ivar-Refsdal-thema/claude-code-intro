# Demo 2 — Modes: Plan+Auto vs. Manual

**Goal:** show how much friction the mode choice adds or removes (slides 8–13),
using two comparable power-market tasks so the *process* difference is what
stands out, not the task difficulty.

## Task A — Plan mode + auto-accept

Folder: `demo-2-modes/task-a-zone-price-dashboard/`

1. Open a terminal there and start Claude Code.
2. Press **Shift+Tab** until you're in **Plan mode**.
3. Paste the prompt below. Read the plan out loud, approve it.
4. Press **Shift+Tab** again to switch to **auto-accept edits**, let it run to
   completion without approving each step.
5. Run `/context` afterwards — note how little back-and-forth there was.

```
Create a Streamlit dashboard `price_dashboard.py` for hourly zonal power
prices, matching the real THEMA price-forecast output format: a tab-separated
.txt file named like `REF_2030_Prices.txt` (scenario name, year, then
`_Prices.txt` — extract the year from the filename). The header row lists
zone codes as column names; each data row is one hour, with two leading index
columns (day-of-year, hour-of-day 1-24) followed by one quoted price column
per zone in EUR/MWh.

If no such files exist in the working directory, generate 2-3 sample files
for different years (e.g. REF_2030_Prices.txt, REF_2035_Prices.txt) covering
a full year of hourly data for this set of real European bidding-zone codes:
NO1-NO5, SE1-SE4, FIN, DK1-DK2, DEU, NLD, FRA, BEL, GBR, ESP, ITA_NORD, POL,
AUT, CHE — with realistic diurnal/seasonal price variation, plus an embedded
zone -> approximate (lat, lon) centroid lookup table for plotting.

The app should: scan the working directory for files matching
`*_<year>_Prices.txt` and let the user pick a year from a dropdown; load the
matching file and compute each zone's yearly average price; show a Plotly
geographic scatter map of Europe with one marker per zone, colored by yearly
average price with a colorbar/legend; and when a zone marker is
clicked/selected, show that zone's full-year hourly price line chart plus
basic stats (mean, min, max). Add a requirements.txt (streamlit, plotly,
pandas). Run with `streamlit run price_dashboard.py`.
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

Then, still in the same manual mode, paste this second prompt:

```
Now add a Streamlit app `merit_order_dashboard.py` that reads the plant CSV
and the hourly dispatch CSV produced by merit_order.py. Let the user pick an
hour (dropdown or slider) and show the merit order (supply) curve — plants
sorted by marginal cost, cumulative dispatched capacity on the x-axis,
marginal cost on the y-axis, drawn as a step curve — together with a
horizontal line at that hour's demand, marking their intersection as the
price cross (the system marginal price). Add streamlit and plotly to a
requirements.txt. Run with `streamlit run merit_order_dashboard.py`.
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
- Both tasks now involve generating sample data plus a two-view Streamlit
  dashboard (overview → drill-down) — that's what keeps them comparable in
  effort despite covering different power-market logic.
