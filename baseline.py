import csv
import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from insertion_sort import insertion_sort
from merge_sort import mergeSort



SIZES = [500, 1_000, 2_000, 4_000, 8_000]
RANDOM_TRIALS = 5
OUTPUT_DIR = Path(__file__).resolve().parent


def time_sort(sort_function, data):
    start = time.perf_counter()
    sort_function(data)
    end = time.perf_counter()
    return end - start
