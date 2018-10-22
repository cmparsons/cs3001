from sklearn import tree, preprocessing
import numpy as np
import graphviz

# enc = preprocessing.OneHotEncoder()

# feature_names = ['Outlook', 'Temperature', 'Humidity', 'Windy']

# outlook = ['Sunny', 'Overcast', 'Rainy']
# temp = ['Hot', 'Mild', 'Cool']
# humidity = ['High', 'Normal']
# windy = ['True', 'False']

# enc = preprocessing.OneHotEncoder(categories=[outlook, temp, humidity, windy])

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

train_x = preprocessing.OneHotEncoder().fit_transform(X)
train_y = preprocessing.LabelEncoder().fit_transform(Y)

clf = tree.DecisionTreeClassifier(criterion='gini')
clf = clf.fit(train_x, train_y)

feature_names = ['Overcast', 'Rainy', 'Sunny', 'Cool', 'Hot', 'Mild', 'High Humidity', 'Normal Humidity', 'Not Windy', 'Windy']
class_names = ['No', 'Yes']
dot_data = tree.export_graphviz(clf, out_file=None, feature_names=feature_names, class_names=class_names)
graph = graphviz.Source(dot_data, format='png')
graph.render("hw3/CART/tennis", cleanup=True, view=True)
