"""Reads benchmark results and draws the comparison graph."""
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


def plot_comparison(rows: list[dict], output: str = "sorting_comparison.png") -> None:
    sizes = [r["n"] for r in rows]

    plt.plot(sizes, [r["selection_sort"] for r in rows], marker="o", color="#C0392B", label="Selection Sort (random)")
    plt.plot(sizes, [r["merge_sort"] for r in rows], marker="o", color="#16A085", label="Merge Sort (random)")
    plt.plot(sizes, [r["selection_sort_sorted"] for r in rows], marker="o", color="#F39C12", label="Selection Sort (already sorted)")

    plt.xlabel("Input size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Selection Sort vs Merge Sort")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output, dpi=150)
    print(f"Graph saved to {output}")



if __name__ == "__main__":
    data = load_results()
    plot_comparison(data)