# toolbelt

Small, dependency-free Python helpers: text, numbers, dates, durations, lists and a tiny user store.
Used as a test bed for automated issue fixing (PatchPilot on Rival CortexOne).

```bash
pip install -r requirements-dev.txt
pytest -q
```

| Module | What it does |
|---|---|
| `toolbelt/text.py` | `slugify`, `truncate` |
| `toolbelt/stats.py` | `mean`, `median`, `percent_change` |
| `toolbelt/dates.py` | `is_leap_year`, `days_in_month` |
| `toolbelt/durations.py` | `parse_duration`, `format_duration` |
| `toolbelt/lists.py` | `chunk`, `dedupe` |
| `toolbelt/users.py` | SQLite-backed user lookup |

The docstrings describe the intended behaviour. If the code and the docstring disagree, the docstring is right.
