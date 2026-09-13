"""This helps us to builds random and sorted integers  for our testing."""
import random


def generate_random_array(n: int, low: int = 0, high: int = 10000) -> list[int]:
    """This function returns a list of n random integers between low and high (inclusive)."""
    return [random.randint(low, high) for _ in range(n)]


def generate_sorted_array(n: int) -> list[int]:
    """This function returns an already-sorted list of n integers, for best-case tests."""
    return list(range(n))