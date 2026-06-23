# Dossier frontmatter contract

A `dossier.md` begins with a YAML frontmatter block (between `---` fences) and a
free-form Markdown body. Frontmatter is the queryable machine state; the body is
append-only narrative.

## Required fields by status
- `scouted`: id, title, status, created, event{type,summary,impact_window}, tickers, sources
- `researched`: all of the above + hypothesis{statement,direction,confidence}, plan{ticker,action,entry{time,target_price},exit{time,target_price},expected_profit_pct}, research{strategy,models,last_updated}
- `scheduled`: same fields as researched (status flips once plan times are in the future)
- `simulated`: all research fields + simulation{ran_at,fills,realized_profit_pct,outcome,matched_hypothesis}
- `analyzed`: all simulated fields + postmortem{ran_at,root_cause,lessons}

## Enums
- status: scouted|researched|scheduled|simulated|analyzed
- event.type: geopolitical|economic|earnings|product|macro|regulatory|ipo
- hypothesis.direction: long|short
- plan.action: buy|sell|short
- simulation.outcome: win|loss|neutral
- simulation.matched_hypothesis: yes|no|partial
- postmortem.root_cause: wrong-assumption|missing-info|timing|data|priced-in

All timestamps are ISO-8601 UTC (suffix `Z`).
