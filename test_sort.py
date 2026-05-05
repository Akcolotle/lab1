from Sorts import bubble_sort, binary_sort


def test_sorted_array():
    arr = [1, 2, 3, 4]
    assert bubble_sort(arr.copy()) == sorted(arr)
    assert binary_sort(arr.copy()) == sorted(arr)


def test_reverse_array():
    arr = [5, 4, 3, 2, 1]
    assert bubble_sort(arr.copy()) == sorted(arr)
    assert binary_sort(arr.copy()) == sorted(arr)


def test_random_array():
    arr = [3, 2, 4, 1]
    assert bubble_sort(arr.copy()) == sorted(arr)
    assert binary_sort(arr.copy()) == sorted(arr)


def test_duplicates():
    arr = [2, 2, 1, 1]
    assert bubble_sort(arr.copy()) == sorted(arr)
    assert binary_sort(arr.copy()) == sorted(arr)


def test_single_element():
    arr = [1]
    assert bubble_sort(arr.copy()) == [1]
    assert binary_sort(arr.copy()) == [1]