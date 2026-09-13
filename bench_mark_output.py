import csv
import statistics
from timeit import default_timer as timer
from selection_sort import selection_sort
from merge_sort import merge_sort
from random_arrays import generate_random_array, generate_sorted_array 



SIZES = [500, 1000, 2000, 4000, 8000]
RANDOM_TRIALS = 5


def time_sort(sort_func, arr: list) -> float:
    start = timer()
    sort_func(arr)
    end = timer()
    return end - start

def average_time(sort_func, build_array, n: int, runs: int = RANDOM_TRIALS) -> float:
    
    times = []
    for _ in range(runs):
        arr = build_array(n)
        times.append(time_sort(sort_func, arr))
    return statistics.mean(times)

def run_benchmark(sizes: list[int] = SIZES) -> list[dict]:
    results = []
    for n in sizes:
        print(f"Benchmarking n = {n}...")
        results.append({
            "n": n,
            "selection_sort": average_time(selection_sort, generate_random_array, n),
            "merge_sort": average_time(merge_sort, generate_random_array, n),
            "selection_sort_sorted": average_time(selection_sort, generate_sorted_array, n),
        })
    return results
def print_growth_check(results: list[dict]) -> None:
    """n doubles -> O(n^2) ratios should sit near 4, O(n log n) ratios should sit just above 2."""
    print("\nDoubling check:")
    for prev, curr in zip(results, results[1:]):
        sel_ratio = curr["selection_sort"] / prev["selection_sort"]
        merge_ratio = curr["merge_sort"] / prev["merge_sort"]
        sorted_ratio = curr["selection_sort_sorted"] / prev["selection_sort_sorted"]
        print(f"n={prev['n']} -> n={curr['n']}: selection x{sel_ratio:.2f}, "
              f"merge x{merge_ratio:.2f}, selection (sorted) x{sorted_ratio:.2f}")


def save_results(results: list[dict], filename: str = "bench_mark_output.csv") -> None:
    fieldnames = ["n", "selection_sort", "merge_sort", "selection_sort_sorted"]
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"Results saved to {filename}")


if __name__ == "__main__":
     data = run_benchmark()
print_growth_check(data)
save_results(data)