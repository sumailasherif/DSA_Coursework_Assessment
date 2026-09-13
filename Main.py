from timeit import default_timer as timer, main, main

from selection_sort import selection_sort
from merge_sort import merge_sort
from random_arrays import generate_random_array
from test import run_correctness_checks
from bench_mark_output import run_benchmark, print_growth_check, save_results
from Results_plot import plot_comparison

def run_and_time(sort_func, arr: list, name: str)-> None:
    start = timer()
    sort_func(arr)
    end = timer()
    print(f"{name} took {end - start:.6f} seconds on n = {len(arr)}")

    def show_menu(n: int) -> None:
    print(f"\nCurrent value of n = {n}")
    print("1. Run Selection Sort")
    print("2. Run Merge Sort")
    print("3. Compare Selection Sort and Merge Sort")
    print("4. Choose a new value of n")
    print("5. Run full benchmark and generate chart")
    print("6. Exit")

    print("\nStep 2: Benchmarking")
    results = run_benchmark()
    print_growth_check(results)
    save_results(results)

    print("\nStep 3: Plotting")
    plot_comparison(results)


if __name__ == "__main__":
    main()