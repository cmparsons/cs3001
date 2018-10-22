"""
Using package: https://pypi.org/project/decision-tree-id3/
"""

from id3 import Id3Estimator, export_graphviz
import numpy as np
import subprocess

basketball_feature_names = ["HomeOrAway", "InTop25", "Media"]

X = np.array([
    ['Home', 'Out', '1-NBC'],
    ['Home', 'In', '1-NBC'],
    ['Away', 'Out', '2-ESPN'],
    ['Away', 'Out', '3-FOX'],
    ['Home', 'Out', '1-NBC'],
    ['Away', 'Out', '4-ABC'],
])

Y = np.array([
    'Win',
    'Lose',
    'Win',
    'Win',
    'Win',
    'Win',
])

clf = Id3Estimator()
clf.fit(X, Y)

export_graphviz(clf.tree_, 'hw3/ID3/basketball.dot', feature_names=basketball_feature_names)
subprocess.run(['dot', '-Tpng', 'hw3/ID3/basketball.dot', '-o', 'hw3/ID3/basketball.png'])
subprocess.run(['rm', 'hw3/ID3/basketball.dot'])
