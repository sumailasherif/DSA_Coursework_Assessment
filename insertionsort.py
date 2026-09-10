import random
import time
import statistics


my_array_1 = [64, 34, 56, 89, 100, 129, 500, 129, 45, 700, 25, 12, 22, 100, 11, 90, 5]

n = len(my_array_1)
for i in range(1,n):
    insert_index = i
    current_value = my_array_1.pop(i)
    for j in range(i-1, -1, -1):
        if my_array_1[j] > current_value:
            insert_index = j
    my_array_1.insert(insert_index, current_value)

print("Sorted array 1:", my_array_1)
my_array_2 = [64, 34, 56, 89, 100, 129, 500, 129, 45, 700, 25, 12, 22, 100, 123, 11, 90, 5]

n = len(my_array_2)
for i in range(1,n):
    insert_index = i
    current_value = my_array_2.pop(i)
    for j in range(i-1, -1, -1):
        if my_array_2[j] > current_value:
            insert_index = j
    my_array_2.insert(insert_index, current_value)

print("Sorted array 2:", my_array_2)

