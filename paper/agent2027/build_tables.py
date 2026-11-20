"""Regenerate the AGENT short-paper v3 table from regraded results summary.

Run at repo root:
    python scripts/aggregate.py v3
    python paper/agent2027/build_tables.py

The upstream aggregator checks each run's regrade.json against Valkyrie's
result before writing results/summary_v3.json. This renderer never infers
model correctness from the agent's final report.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUMMARY = ROOT / "results" / "summary_v3.json"
OUT = Path(__file__).resolve().parent / "tables" / "v3-primary.tex"

ORDER = [
    ("haiku45", "Claude Haiku 4.5"),
    ("sonnet46", "Claude Sonnet 4.6"),
    ("haiku55", "Claude Haiku 5.5"),
    ("sonnet55", "Claude Sonnet 5.5"),
    ("opus55", "Claude Opus 5.5"),
    ("gpt53codex", "GPT-5.3-Codex"),
    ("gpt54", "GPT-5.4"),
]
TASKS = ["commit_timeout", "stale_read", "partial_batch", "duplicate_delivery"]
data = json.loads(SUMMARY.read_text(encoding="utf-8"))
assert data["dataset_version"] == "v3"
rows = []
for key, name in ORDER:
    model = data["models"][key]
    n = model["trials"]
    assert n == 10, f"{key}: expected 10 complete runs, found {n}"
    counts = [model["passes_per_task"][task] for task in TASKS]
    assert all(isinstance(x, (int, float)) and x.is_integer() if isinstance(x, float) else isinstance(x, int) for x in counts)
    assert all(0 <= x <= n for x in counts)
    total = round(sum(counts))
    row = " & ".join(
        [name] + [f"{round(x)}/{n}" for x in counts] + [f"{total}/{n * len(TASKS)}"]
    ) + r" \\"
    rows.append(row)

lines = [
    "% Generated from results/summary_v3.json. Do not hand-edit counts.",
    "% CT=504 after payout saved; SR=old membership after role change; PB=two of three reservations saved before 504; DD=502 after account created.",
    r"\begin{table}[H]",
    r"\centering",
    r"\caption{Passes on the same four v3 tasks, ten runs per model. A pass means the saved records met the task rules. CT: HTTP 504 after a payout was saved; SR: old membership returned after a role change; PB: two of three reservations saved before HTTP 504; DD: HTTP 502 after an account was created. Claude and OpenAI models ran in different harnesses.}",
    r"\label{tab:v3}",
    r"\scriptsize",
    r"\setlength{\tabcolsep}{2.5pt}",
    r"\begin{tabular}{@{}lrrrrr@{}}",
    r"\toprule",
    r"Model & CT & SR & PB & DD & Total \\",
    r"\midrule",
    *rows,
    r"\bottomrule",
    r"\end{tabular}",
    r"\end{table}",
    "",
]
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Rendered {OUT.relative_to(ROOT)} from {SUMMARY.relative_to(ROOT)}")
