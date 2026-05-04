# Collatz (3n+1) — `collatz.py`

Explores the **Collatz conjecture**: from a positive integer `n`, if `n` is even divide by 2, if odd use `3n + 1`, repeat until you reach 1. For each starting value in a chosen range, the script records step index (`x`) and value (`y`), writes paired CSV files under `./data/`, and supports a **Streamlit** UI or a **terminal** workflow.

## Requirements

- Python 3.10+
- `streamlit`, `pandas`, `numpy` (see imports in `collatz.py`)

```bash
pip install streamlit pandas numpy
```

## Data folder

CSVs are created as `./data/<n>_x_data_points.csv` and `./data/<n>_y_data_points.csv`. Run from this directory (`3n+1`) so relative paths work. Create `data` if needed:

```bash
mkdir data
```

## Streamlit

```bash
streamlit run collatz.py
```

Enter a start and end range, click **Run** to generate files, choose matching x/y files, then **Chart** to plot. **Delete files** removes CSVs in `./data/` and reruns the app. If no CSVs exist yet, the app stops with an info message instead of failing on empty options.

## Command line

```bash
python collatz.py
```

Prompts for a range, runs Collatz, lists CSVs, then loops: pick a pair by number, optionally delete all CSVs, start over with a new range, or exit.

## Behavior notes

- Each `collatz()` run clears `all_x_points` / `all_y_points` before computing so a new range does not mix with previous in-memory sequences.
- Streamlit warns if the end value is smaller than the start before running.

## License / context

Part of a personal **Cybersecurity** learning repository; this folder is for math visualization practice, not production security tooling.
