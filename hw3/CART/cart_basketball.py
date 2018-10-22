from sklearn import tree, preprocessing
import graphviz
import numpy as np

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

# enc = preprocessing.LabelEncoder()
# label_encoder = enc.fit(X[:, 0])
# # print(label_encoder.classes_)
# integer_classes = label_encoder.transform(label_encoder.classes_)
# # print(integer_classes)
# X[:, 0] = label_encoder.transform(X[:, 0])
# print(X)

# enc = preprocessing.LabelEncoder()
# label_encoder = enc.fit(X[:, 1])
# # print(label_encoder.classes_)
# integer_classes = label_encoder.transform(label_encoder.classes_)
# # print(integer_classes)
# X[:, 1] = label_encoder.transform(X[:, 1])
# print(X)

train_x = preprocessing.OrdinalEncoder().fit_transform(X)
train_y = preprocessing.LabelEncoder().fit_transform(Y)

clf = tree.DecisionTreeClassifier(criterion='gini')
clf = clf.fit(train_x, train_y)

dot_data = tree.export_graphviz(clf, out_file=None, feature_names=['Is Home', 'In Top 25', 'Media'], class_names=['Lose', 'Win'])
graph = graphviz.Source(dot_data, format='png')
graph.render("hw3/CART/basketball", cleanup=True, view=True)
