def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr, val, start, end):
    if start == end:
        return start if arr[start] > val else start + 1

    if start > end:
        return start

    mid = (start + end) // 2

    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def binary_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)

        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]

    return arr


if __name__ == "__main__":
    import random
    import time

    arr = [random.randint(0, 10000) for _ in range(10000)]

    arr1 = arr.copy()
    arr2 = arr.copy()

    start = time.time()
    bubble_sort(arr1)
    end = time.time()
    print("Bubble:", end - start)

    start = time.time()
    binary_sort(arr2)
    end = time.time()
    print("Binary:", end - start)
