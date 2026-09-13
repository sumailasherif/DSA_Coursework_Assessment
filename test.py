"""Correctness checks for selection sort and merge sort, run before any timing."""
from selection_sort import selection_sort
from merge_sort import merge_sort
from random_arrays import generate_random_array, generate_sorted_array


def get_test_cases() -> list[tuple[str, list]]:
    return [
        ("empty list", []),
        ("single element", [7]),
        ("already sorted", [1, 2, 3, 4, 5]),
        ("reverse sorted", [5, 4, 3, 2, 1]),
        ("repeated values", [3, 1, 2, 3, 1, 2]),
        ("negatives and repeats", [4, -2, 0, -5, 9, 4]),
        ("bigger sorted list", generate_sorted_array(50)),
        ("bigger random list", generate_random_array(200)),
    ]

def run_correctness_checks() -> None:
    for name, case in get_test_cases():
        expected = sorted(case)
        got_selection = selection_sort(case.copy())
        got_merge = merge_sort(case.copy())
        assert got_selection == expected, f"Selection sort failed on: {name}"
        assert got_merge == expected, f"Merge sort failed on: {name}"
    print("All correctness checks passed.")
if __name__ == "__main__":
    run_correctness_checks()