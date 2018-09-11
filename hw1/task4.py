"""Task 4 Numpy and Vectorized Computing"""

import numpy

if __name__ == "__main__":
    x = numpy.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])

    y = x[:,2]; print(y)
    y = x[-1,:2]; print(y)
    y = x[:, [True, False, False, True]]; print(y)
    y = x[0:2, 0:2]; print(y)
    y = x[[0, 1, 2], [0, 1, 2]]; print(y)
    y = x[0]**2; print(y)
    y = x.max(axis=1); print(y)
    y = x[:2,:2]+x[:2,2:]; print(y)
    y = x[:2, :3].T; print(y)
    y = x[:2, :3].reshape((3, 2)); print(y)
    y = x[:, :2].dot([1, 1]); print(y)
    y = x[:, :2].dot([[3, 0], [0, 2]]); print(y)
