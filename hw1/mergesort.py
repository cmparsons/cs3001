"""
2a Merge Sort

NOTE: Recursive implementation is not ideal for large datasets due to limited stack space.
"""

import random


def merge_rec(left, right):
    """Recursive Merge"""
    if left == []:
        return right
    elif right == []:
        return left
    elif left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


def merge_iter(left, right):
    """Iterative Merge"""
    i = 0  # pointer for left list
    j = 0  # pointer for right list

    result = []  # sorted result

    # Merge left and right lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Copy over remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        return merge_iter(merge_sort(l[:mid]), merge_sort(l[mid:]))
    return l


if __name__ == "__main__":
    a = [random.randint(0, 9) for _ in range(1000)]
    b = merge_sort(a)
    print("merge_sort is", "correct" if b == sorted(a) else "incorrect")
