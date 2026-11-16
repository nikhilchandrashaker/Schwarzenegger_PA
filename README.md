# California 2003 Recall Election: How Schwarzenegger Won

A data-first, neutral analysis of the October 7, 2003 recall of Gov. Gray Davis and the election of Arnold Schwarzenegger. It rests on certified county-level results (all 58 counties) from the California Secretary of State. It takes no position on whether the recall or its outcome was good or bad.

## Files

| File | What it is |
|---|---|
| `schwarzenegger_recall_2003_paper.docx` / `.md` | Full research paper (abstract, background, data, methods, results, six competing explanations, limitations, conclusion, references). Same text in both formats. |
| `schwarzenegger_recall_2003_dataset.xlsx` | Main dataset, 10 sheets (see below). Derived columns are live formulas. |
| `county_data.csv` | County-level data (58 rows) with derived variables, for R/Python/SQL. |
| `data_and_analysis.py` | Rebuilds `county_data.csv`, validates it against certified statewide totals, and runs all statistics. |
| `results.json` | Output of the script: correlations, regressions, regional summaries, margin tests. |
| `schwarzenegger_recall_2003.html` | Single-page visual summary (data story). Open in any browser. |
| `README.md` | This file. |

## Workbook sheets

`county_data` (official counts + derived shares) · `statewide_results` (certified totals with check column vs. county sums) · `region_summary` (9 analyst-defined regions) · `statewide_history` (turnout/registration 1990-2008) · `polls` · `exit_poll_reported` · `subgroup_survey` · `analysis_results` · `data_dictionary` · `sources`

## Reproduce

```bash
pip install pandas numpy
python data_and_analysis.py     # writes county_data.csv and results.json; prints validation
```

The script prints `VALIDATION mismatches: none` when county sums match the certified statewide totals.

## Key results

- Recall: 55.4% Yes (4,976,274) vs. 44.6% No (4,007,783); 9,413,494 ballots (61.2% of registered).
- Replacement: Schwarzenegger 4,206,284 (48.6%), Bustamante 2,724,874 (31.5%), McClintock 1,161,287 (13.4%), Camejo 242,247 (2.8%).
- Schwarzenegger won 50 of 58 counties; Bustamante 8 (all northern coastal/Bay Area).
- County recall support correlates +0.94 with Republican registration share (descriptive, not individual-level).
- Schwarzenegger still leads even if every McClintock and Camejo vote went to Bustamante (by 77,876).

## Data notes and caveats

- All counts are certified figures (certified Nov. 14, 2003). Election-night counts were partial and are not used.
- Candidate `*_pct_rep` columns are the SOS-reported percentages of governor-contest votes, rounded to 0.1 point. Derived `*_share_ballots` columns use total ballots as the denominator and run about 8% lower.
- Regions and voting-system labels are descriptive. The region grouping is the analyst's.
- Exit-poll findings and the subgroup survey are secondary (news reports/reproductions), not microdata, and are never used in calculations.
- The SOS registration table lists 5,429,356 Republican registrants; its historical table lists 5,429,256. The analysis uses 5,429,356.
- County-level associations do not identify how individual voters behaved (ecological fallacy).

## Source

California Secretary of State, *Statement of Vote, Statewide Special Election, October 7, 2003*: https://elections.cdn.sos.ca.gov/sov/2003-special/sov-complete.pdf (other sources are listed in the `sources` sheet and the paper's references).
