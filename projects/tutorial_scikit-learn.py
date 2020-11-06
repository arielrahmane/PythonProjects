#		This scripts takes the data from the arrays X and Y to learn the height, weight and shoe size of males and females
#	being later able to predict the gender from a new input.

from sklearn import tree

#[Height, Weight, Shoe Size]
X = [[181, 80, 44], [177, 70, 43], [185, 90, 45], [166, 65, 38], [192, 93, 46], [170, 65, 39], [165, 60, 36], [175, 65, 39], [178, 63, 38]]
Y = ['male', 'male', 'male', 'male', 'female', 'male', 'female', 'female', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[160, 60, 40]])

print(prediction)