import sklearn.model_selection as model_selection
from sklearn.model_selection import train_test_split

X =  list(range(15))
print (X)
y = [x * x for x in X]
print (y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 10)
print ("X_train: ", X_train)
print ("y_train: ", y_train)
print("X_test: ", X_test)
print ("y_test: ", y_test)