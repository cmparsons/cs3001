# -*- coding:utf-8 -*-

"""
Taken from: https://github.com/zhuang-hao-ming/c4.5-python
"""
import operator
import math


def get_majority_class(class_list):
    class_count = {}
    for item in class_list:
        if item in class_count:
            class_count[item] += 1
        else:
            class_count[item] = 1
    class_items = class_count.items()
    class_items = sorted(class_items, key=operator.itemgetter(1), reverse=True)
    return class_items[0][0]


def calculate_shannon_ent(data_set):
    num_of_samples = len(data_set)
    class_count = {}
    for sample in data_set:
        class_label = sample[-1]
        if class_label in class_count:
            class_count[class_label] += 1
        else:
            class_count[class_label] = 1
    ent = 0.0
    for key in class_count:
        prob = float(class_count[key]) / num_of_samples
        ent -= prob * math.log(prob, 2)
    return ent


def split_data_set(data_set, feature_idx, val):
    sub_data_set = []
    for sample in data_set:
        if sample[feature_idx] == val:
            reduce_sample = sample[:feature_idx] + sample[feature_idx+1:]
            sub_data_set.append(reduce_sample)
    return sub_data_set


def choose_best_feature_for_split(data_set):
    num_features = len(data_set[0]) - 1
    base_entropy = calculate_shannon_ent(data_set)
    best_info_gain_ration = 0.0
    best_feature_idx = -1
    for i in range(num_features):
        feature_list = [sample[i] for sample in data_set]
        unique_values = set(feature_list)
        new_entropy = 0.0
        split_info = 0.0
        for val in unique_values:
            sub_set = split_data_set(data_set, i, val)
            prob = float(len(sub_set)) / len(data_set)
            new_entropy += prob * calculate_shannon_ent(sub_set)
            split_info += -prob * math.log(prob, 2)
        if split_info == 0:
            continue
        info_gain = base_entropy - new_entropy
        info_gain_ration = info_gain / split_info
        if info_gain_ration > best_info_gain_ration:
            best_info_gain_ration = info_gain_ration
            best_feature_idx = i
    return best_feature_idx


def create_tree(data_set, labels):
    class_list = [item[-1] for item in data_set]
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(data_set[0]) == 1:
        return get_majority_class(class_list)
    best_feature_idx = choose_best_feature_for_split(data_set)
    best_feature_label = labels[best_feature_idx]
    del(labels[best_feature_idx])
    my_tree = {best_feature_label: {}}
    feature_vals = [sample[best_feature_idx] for sample in data_set]
    unique_vals = set(feature_vals)
    for val in unique_vals:
        sub_labels = labels[:]
        my_tree[best_feature_label][val] = create_tree(split_data_set(data_set, best_feature_idx, val), sub_labels)
    return my_tree


def main():
    tennis = [
        ['Sunny', 'Hot', 'High', 'False', 'No'],
        ['Sunny', 'Hot', 'High', 'True', 'No'],
        ['Overcast', 'Hot', 'High', 'False', 'Yes'],
        ['Rainy', 'Mild', 'High', 'False', 'Yes'],
        ['Rainy', 'Cool', 'Normal', 'False', 'Yes'],
        ['Rainy', 'Cool', 'Normal', 'True', 'No'],
        ['Overcast', 'Cool', 'Normal', 'True', 'Yes'],
        ['Sunny', 'Mild', 'High', 'False', 'No'],
        ['Sunny', 'Cool', 'Normal', 'False', 'Yes'],
        ['Rainy', 'Mild', 'Normal', 'False', 'Yes'],
        ['Sunny', 'Mild', 'Normal', 'True', 'Yes'],
        ['Overcast', 'Mild', 'High', 'True', 'Yes'],
        ['Overcast', 'Hot', 'Normal', 'False', 'Yes'],
        ['Rainy', 'Mild', 'High', 'True', 'No']
    ]

    tennis_labels = ['Outlook', 'Temperature', 'Humidity', 'Windy']

    basketball = [
        ['Home', 'Out', '1-NBC', 'Win'],
        ['Home', 'In', '1-NBC', 'Lose'],
        ['Away', 'Out', '2-ESPN', 'Win'],
        ['Away', 'Out', '3-FOX', 'Win'],
        ['Home', 'Out', '1-NBC', 'Win'],
        ['Away', 'Out', '4-ABC', 'Win'],
    ]

    basketball_labels = ['Home/Away', 'In Top 25?', 'Media', 'Win/Lose']

    decision_tree_tennis = create_tree(tennis, tennis_labels)
    decision_tree_basketball = create_tree(basketball, basketball_labels)
    print(decision_tree_tennis)
    print(decision_tree_basketball)


if __name__ == '__main__':
    main()
