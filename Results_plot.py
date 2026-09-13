import csv
import matplotlib.pyplot as plt


def load_results(filename: str = "bench_mark_output.csv") -> list[dict]:
    with open(filename) as f:
        reader = csv.DictReader(f)
        rows = [
            {k: (int(v) if k == "n" else float(v)) for k, v in row.items()}
            for row in reader
        ]
    return rows