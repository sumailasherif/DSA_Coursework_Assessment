from timeit import default_timer as timer

from selection_sort import selection_sort
from merge_sort import merge_sort
from random_arrays import generate_random_array
from test import run_correctness_checks
from bench_mark_output import run_benchmark, print_growth_check, save_results
from Results_plot import plot_comparison

def run_and_time(sort_func, arr: list, name: str)-> None:
    print("Step 1: Correctness checks")
    run_correctness_checks()

    print("\nStep 2: Benchmarking")
    results = run_benchmark()
    print_growth_check(results)
    save_results(results)

    print("\nStep 3: Plotting")
    plot_comparison(results)


if __name__ == "__main__":
    main()