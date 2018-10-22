"""
Using package: https://pypi.org/project/decision-tree-id3/
"""

from id3 import Id3Estimator, export_graphviz
import numpy as np
import subprocess

tennis_feature_names = ['Outlook', 'Temperature', 'Humidity', 'Windy']

X = np.array([
    ['Sunny', 'Hot', 'High', 'False'],
    ['Sunny', 'Hot', 'High', 'True'],
    ['Overcast', 'Hot', 'High', 'False'],
    ['Rainy', 'Mild', 'High', 'False'],
    ['Rainy', 'Cool', 'Normal', 'False'],
    ['Rainy', 'Cool', 'Normal', 'True'],
    ['Overcast', 'Cool', 'Normal', 'True'],
    ['Sunny', 'Mild', 'High', 'False'],
    ['Sunny', 'Cool', 'Normal', 'False'],
    ['Rainy', 'Mild', 'Normal', 'False'],
    ['Sunny', 'Mild', 'Normal', 'True'],
    ['Overcast', 'Mild', 'High', 'True'],
    ['Overcast', 'Hot', 'Normal', 'False'],
    ['Rainy', 'Mild', 'High', 'True'],
])

Y = np.array([
    'No',
    'No',
    'Yes',
    'Yes',
    'Yes',
    'No',
    'Yes',
    'No',
    'Yes',
    'Yes',
    'Yes',
    'Yes',
    'Yes',
    'No',
])

clf = Id3Estimator()
clf.fit(X, Y)

export_graphviz(clf.tree_, "hw3/ID3/tennis.dot", feature_names=tennis_feature_names)
subprocess.run(['dot', '-Tpng', 'hw3/ID3/tennis.dot', '-o', 'hw3/ID3/tennis.png'])
subprocess.run(['rm', 'hw3/ID3/tennis.dot'])
