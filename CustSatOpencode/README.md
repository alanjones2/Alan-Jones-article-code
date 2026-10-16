# StepSavvy customer satisfaction analysis

Open **[the HTML business report](reports/customer_satisfaction_report.html)** in a browser. It includes an inline satisfaction chart, rankings, source-linked review evidence, a prioritised action plan and methodological limitations. It works offline and supports printing.

## Rebuild

The project was initialised with `uv init`. The analysis uses Python 3.13+ and only the standard library, so no additional libraries are required.

```bash
uv run python analyse.py
```

Run from this directory. The script resolves input and output paths relative to itself.

## Deliverables

- `reports/customer_satisfaction_report.html` — self-contained business report.
- `reports/satisfaction_chart.svg` — standalone, accessible comparison chart.
- `data/reviews.csv` — all original comments, ratings and manually assigned themes.
- `data/product_summary.csv` — ranked product metrics.
- `data/analysis.json` — full-precision metrics, rating distributions, concern counts and review records.
- `analyse.py` — parsing, analysis and report generation.

The primary source is `data/shoes.md`. Positive means 4–5 stars; low means 1–2 stars; 3 stars is neutral. Products are ranked by mean rating, preserving ties. The sample contains only four reviews per product, so results are directional.

Qualitative themes and narrative interpretations were authored for this supplied dataset. The script checks product names, review counts and comment anchors before reusing those annotations. If the source changes, review **all** annotations, report narrative and recommendations before rebuilding; anchor checks do not detect every possible edit. The generated date reflects the build date, not the review period. Each report records the source SHA-256 for traceability.
