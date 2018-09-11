""" 2c Hist with Rescale"""

import matplotlib.pyplot as plt
import math
import random

from summary_statistics import get_max


def my_hist_with_rescale(l):
    max_value = get_max(l)
    rescaled = [int((x / max_value) * 9) for x in l]
    occurrences = [0] * 10

    for value in rescaled:
        occurrences[value] += 1

    return occurrences


if __name__ == "__main__":
    listA = [random.randint(0, 9) for _ in range(1000)]
    listB = [random.gauss(5, 3) for _ in range(1000)]
    listC = [math.exp(random.gauss(1, 0.5)) for _ in range(1000)]

    countA = my_hist_with_rescale(listA)
    countB = my_hist_with_rescale(listB)
    countC = my_hist_with_rescale(listC)

    x_values = list(range(10))

    fig, ax = plt.subplots()

    ax.plot(x_values, countA, 'ro-', label="Rescaled data 1")
    ax.plot(x_values, countB, 'g+-.', label="Rescaled data 2")
    ax.plot(x_values, countC, 'bx:', label="Rescaled data 3")

    plt.xlabel('Value')
    plt.ylabel('Frequency')

    ax.legend(loc='upper right', shadow=True)

    plt.savefig('hw1/plots/history_with_rescale.png')
    # plt.show()
