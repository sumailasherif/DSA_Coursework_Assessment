import csv
import statistics
import random
import time
from pathlib import Path
from timeit import default_timer as timer
import matplotlib.pyplot as plt

from selection_sort import selection_sort
from merge_sort import merge_sort
from random_arrays import generate_random_array, generate_sorted_array 



SIZES = [500, 1000, 2000, 4000, 8000]
RANDOM_TRIALS = 5
OUTPUT_DIR = Path(__file__).resolve().parent


def time_sort(sort_func, arr: list) -> float:
    start = timer()
    sort_func(arr)
    end = timer()
    return end - start

def average_time(sort_func, n: int, runs: int = RUNS) -> float:
    """Fresh random list each run, average the sort time only."""
    times = []
    for _ in range(runs):
        arr = generate_random_array(n)               
        times.append(time_sort(sort_func, arr))       
    return statistics.mean(times)


def run_benchmark(sizes: list[int] = SIZES) -> list[dict]:
    results = []
    for n in sizes:
        print(f"Benchmarking n = {n}...")
        results.append({
            "n": n,
            "selection_sort": average_time(selection_sort, n),
            "merge_sort": average_time(merge_sort, n),
        })
    return results
def print_growth_check(results: list[dict]) -> None:
    """n doubles -> selection time should x4 (O(n^2)), merge should be closer to x2 (O(n log n))."""
    print("\nDoubling check:")
    for prev, curr in zip(results, results[1:]):
        sel_ratio = curr["selection_sort"] / prev["selection_sort"]
        merge_ratio = curr["merge_sort"] / prev["merge_sort"]
        print(f"n={prev['n']} -> n={curr['n']}: selection x{sel_ratio:.2f}, merge x{merge_ratio:.2f}")
def save_results(results: list[dict], filename: str = "bench_mark_output.csv") -> None:
    fieldnames = ["n", "selection_sort", "merge_sort"]
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"Results saved to {filename}")

if __name__ == "__main__":
    data = run_benchmark()
    print_growth_check(data)
    save_results(data)