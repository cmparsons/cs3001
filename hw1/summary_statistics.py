"""2b Summary Statistics"""

import numpy as np
import matplotlib.pyplot as plt
import math
import random

from mergesort import merge_sort


def get_max(l):
    current_max = l[0]
    for value in l:
        current_max = value if value > current_max else current_max
    return current_max


def get_min(l):
    current_min = l[0]
    for value in l:
        current_min = value if value < current_min else current_min
    return current_min


def get_mean(l):
    running_sum = 0
    for value in l:
        running_sum += value
    return running_sum / len(l)


def get_standard_deviation(l):
    mean = get_mean(l)
    s = 0
    for value in l:
        s += (value - mean)*(value - mean)

    return math.sqrt(s/(len(l) - 1))


def get_median(l):
    n = len(l)
    sorted_data = merge_sort(l)

    if n % 2 != 0:
        return sorted_data[(n+1)//2]

    return get_mean(sorted_data[(n//2):(n//2 + 2)])


def get_percentile(quartile, data):
    sorted_data = merge_sort(data)
    observation = int((quartile / 100) * (len(data) + 1))
    return sorted_data[observation]


def summary_statistics(l):
    mean = get_mean(l)
    sd = get_standard_deviation(l)
    return {
        'max': get_max(l),
        'min': get_min(l),
        'mean': mean,
        'median': get_median(l),
        'sd': sd,
        'mean+sd': mean + sd,
        'mean-sd': mean - sd,
        '75 perc': get_percentile(75, l),
        '25 perc': get_percentile(25, l)
    }


if __name__ == "__main__":
    listA = [random.randint(0, 9) for _ in range(1000)]
    listB = [random.gauss(5, 3) for _ in range(1000)]
    listC = [math.exp(random.gauss(1, 0.5)) for _ in range(1000)]

    ssA = summary_statistics(listA)
    ssB = summary_statistics(listB)
    ssC = summary_statistics(listC)

    summary_stats = [ssA, ssB, ssC]
    x_ticks = [0.25, 0.50, 0.75]

    marker_properties = {
        'max': {'color': 'black', 'marker': 'v'},
        'min': {'color': 'black', 'marker': '^'},
        'mean': {'color': 'blue', 'marker': '+'},
        'median': {'color': 'blue', 'marker': 'x'},
        'mean+sd': {'color': 'green', 'marker': 'v'},
        'mean-sd': {'color': 'green', 'marker': '^'},
        '75 perc': {'color': 'red', 'marker': 'v'},
        '25 perc': {'color': 'red', 'marker': '^'}
    }

    # Group each summary statistic to list of summary statistic values.
    # { 'max': [ssA['max'], ssB['max'], ssC['max']] }
    processed = {}
    for ss in summary_stats:
        for key, value in ss.items():
            # Skip standard deviation because it is not directly needed in figure
            if key != 'sd':
                if key not in processed:
                    processed[key] = [value]
                else:
                    processed[key].append(value)

    fig, ax = plt.subplots()

    for ss, ss_values in processed.items():
        plt.scatter([x_ticks[i] for i, _ in enumerate(ss_values)],
                    ss_values, c=marker_properties[ss]['color'], marker=marker_properties[ss]['marker'], label=ss)

    plt.xticks(x_ticks, ('Data 1', 'Data 2', 'Data 3'))
    ax.set_xlim(0, 1.25)

    ax.legend(loc='upper right')
    plt.savefig('hw1/plots/summary_statistics.png')
