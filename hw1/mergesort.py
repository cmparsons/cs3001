"""
2a Merge Sort

NOTE: Recursive implementation which is not ideal for large datasets due to limited
stack space.
"""

import random


def merge(l1, l2):
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    elif l1[0] < l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    return [l2[0]] + merge(l1, l2[1:])


def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        return merge(merge_sort(l[:mid]), merge_sort(l[mid:]))
    return l


if __name__ == "__main__":
    a = [random.randint(0, 9) for _ in range(1000)]
    b = merge_sort(a)
    print("merge_sort is", "correct" if b == sorted(a) else "incorrect")
