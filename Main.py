from test import run_correctness_checks
from bench_mark_output import run_benchmark, print_growth_check, save_results
from Results_plot import plot_comparison

def main() -> None:
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