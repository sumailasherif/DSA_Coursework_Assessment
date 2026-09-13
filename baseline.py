import csv
import statistics
import random
import time
from pathlib import Path
from timeit import default_timer as timer
import matplotlib.pyplot as plt

from selection_sort import selection_sort
from merge_sort import merge_sort
from random_array_generator import generate_random_array



SIZES = [500, 1000, 2000, 4000, 8000]
RANDOM_TRIALS = 5
OUTPUT_DIR = Path(__file__).resolve().parent


def time_sort(sort_function, data):
    start = time.perf_counter()
    sort_function(data)
    end = time.perf_counter()
    return end - start
