#For our insertion Sort,our time complexity are as follows:
    #1. Best case:    O(n)   when the list is already sorted.
    #2. Average case: O(n^2)
    #3. Worst case:   O(n^2)
    #And moreover, our Space complexity is O(1) because we are sorting the list in place and not using any additional data structures that grow with input size.
def insertion_sort(values: list[int]) -> list[int]:
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1

        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = key

    return values
