from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.inspection import DecisionBoundaryDisplay

X = data[['Feature1','Feature2']].values
y = data['Target']

# splitting X and y into training and testing sets 60% and 40%, respectively


# create logistic regression object (model)


# train the model using the training sets


# sketch the decision boundary using DecisionBoundaryDisplay and the method from_estimator()
