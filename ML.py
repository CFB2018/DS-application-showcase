
    # Objective: Create a ML pipeline to predict first stage landing.
    
    # Perform EDA and determine training labels (dataset_part_2.csv)
    # Create a column for the class, standardize the data, split into training/test data 
    # & find best hyperparameter for SVM, Classification Trees and Logistic Regression
    
    
# Import required libraries, modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import confusion_matrix 


# Define a function to plot the confusion matrix
def plot_confusion_matrix(y_true, y_pred, title='Confusion Matrix'):
    cm = confusion_matrix(y_true, y_pred)
    ax = plt.subplot()
    sns.heatmap(cm, annot=True, ax=ax, fmt='d', cmap='Blues');  # fmt='d' for integer annotations
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title(title)  # Set the title here
    ax.xaxis.set_ticklabels(['Did Not Land', 'Landed']); 
    ax.yaxis.set_ticklabels(['Did Not Land', 'Landed']) 
    plt.show()

# Load the dataframes
data = pd.read_csv('dataset_part_2.csv')
print(data.head())
X = pd.read_csv('dataset_part3.csv')
print(X.head(100))

# Extract the 'Class' column and keep it as a Pandas series
y = data['Class']
print(y)

# Create an instance of StandardScaler
scaler = StandardScaler()

# Split the data into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Display the shapes of the resulting datasets
#print("Training data shape:", X_train.shape, y_train.shape)
#print("Test data shape:", X_test.shape, y_test.shape)

# Split the training data into training and validation sets
X_train_final, X_val, y_train_final, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)

# Standardize the features
X_train_final = scaler.fit_transform(X_train_final)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Create a logistic regression model
lr = LogisticRegression(max_iter=1000)

# Define the parameter grid
parameters = {
    'C': [0.01,0.1,1],  # Regularization strength,
    'penalty': ['l2'],  # Regularization type
    'solver': ['lbfgs'],  # Optimization algorithm
    'multi_class': ['multinomial']  # Multi-class option
}

# Create the GridSearchCV object with cv=10
logreg_cv = GridSearchCV(lr, parameters, cv=10, verbose=0)

# Fit the GridSearchCV object to the training data
logreg_cv.fit(X_train_final, y_train_final)

# Print the best parameters and accuracy
print("Logistic Regression - Tuned hyperparameters (best parameters): {}".format(logreg_cv.best_params_))
print("Logistic Regression - Best cross-validated accuracy: {:.2f}".format(logreg_cv.best_score_))

# Calculate accuracy on the test data using the score method
# Use the best estimator to calculate accuracy on the test data
best_model = logreg_cv.best_estimator_
accuracy = best_model.score(X_test, y_test)
print('Accuracy on test data: {:.2f}'.format(accuracy))

# Confusion matrix 
yhat=logreg_cv.predict(X_test)
plot_confusion_matrix(y_test,yhat, title='Logistic Regression Confusion Matrix')

# The performance of the classification model correctly predicted landed when it landed (True positives = 14)
# True negatives = 3
# 1 false positive (Type I error) and 0 false negative (Type II error)

# Create a Support Vector Machine model
svm = SVC()

# Define the parameter grid for SVM
parameters = {
    'kernel': ('linear', 'rbf', 'poly', 'sigmoid'),
    'C': np.logspace(-3, 3, 5),
    'gamma': np.logspace(-3, 3, 5)
}

# Create the GridSearchCV object with cv=10
svm_cv = GridSearchCV(svm, parameters, cv=10, verbose=0)

# Fit the GridSearchCV object to the training data
svm_cv.fit(X_train_final, y_train_final)

# Print the best parameters and accuracy
print("SVM - Tuned hyperparameters (best parameters): {}".format(svm_cv.best_params_))
print("SVM - Best cross-validated accuracy: {:.2f}".format(svm_cv.best_score_))

# Use the best estimator to calculate accuracy on the validation data
best_model_svm = svm_cv.best_estimator_
val_accuracy = best_model_svm.score(X_val, y_val)
print('SVM - Validation Accuracy: {:.2f}'.format(val_accuracy))

# Calculate accuracy on the test data
test_accuracy_svm = best_model_svm.score(X_test, y_test)
print('SVM - Test Accuracy: {:.2f}'.format(test_accuracy_svm))

# Plot the confusion matrix for the SVM model
yhat=svm_cv.predict(X_test)
plot_confusion_matrix(y_test,yhat, title='SVM Confusion Matrix')


# Create a Decision Tree Classifier object
tree = DecisionTreeClassifier()

# Define the parameter grid for Decision Tree
parameters = {
    'criterion': ['gini', 'entropy'],
    'splitter': ['best', 'random'],
    'max_depth': [2 * n for n in range(1, 10)],
    'max_features': ['auto', 'sqrt'],
    'min_samples_leaf': [1, 2, 4],
    'min_samples_split': [2, 5, 10]
}

# Create the GridSearchCV object with cv=10
tree_cv = GridSearchCV(tree, parameters, cv=10, verbose=0)

# Fit the GridSearchCV object to the training data
tree_cv.fit(X_train, y_train)

# Print the best parameters and accuracy using format()
print("Decision Tree - Tuned hyperparameters (best parameters): {}".format(tree_cv.best_params_))
print("Decision Tree - Best cross-validated accuracy: {:.2f}".format(tree_cv.best_score_))

# Use the best estimator to calculate accuracy on the test data
best_model_tree = tree_cv.best_estimator_
test_accuracy_tree = best_model_tree.score(X_test, y_test)
print('Decision Tree - Test Accuracy: {:.2f}'.format(test_accuracy_tree))

# Make predictions using the Decision Tree model
yhat_tree = best_model_tree.predict(X_test)

# Plot the confusion matrix for the Decision Tree model
def plot_confusion_matrix(y_true, y_pred, title='Confusion Matrix'):
    cm = confusion_matrix(y_true, y_pred)
    ax = plt.subplot()
    sns.heatmap(cm, annot=True, ax=ax, fmt='d', cmap='Blues');  # fmt='d' for integer annotations
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title(title)  
    ax.xaxis.set_ticklabels(['Did Not Land', 'Landed']); 
    ax.yaxis.set_ticklabels(['Did Not Land', 'Landed']) 
    plt.show()

# Plot the confusion matrix with a title
plot_confusion_matrix(y_test, yhat_tree, title='Decision Tree Confusion Matrix')


# Create a k nearest neighbors classifier object and perform hyperparameter tuning using GridSearchCV
KNN = KNeighborsClassifier()

# Define the parameter grid for KNN
parameters = {
    'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Number of neighbors
    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],  # Algorithm to compute the nearest neighbors
    'p': [1, 2]  # Power parameter for the Minkowski distance
}

# Create the GridSearchCV object with cv=10
knn_cv = GridSearchCV(KNN, parameters, cv=10, verbose=0)

# Fit the GridSearchCV object to the training data
knn_cv.fit(X_train, y_train)

# Print the best parameters and accuracy using format()
print("KNN - Tuned hyperparameters (best parameters): {}".format(knn_cv.best_params_))
print("KNN - Best cross-validated accuracy: {:.2f}".format(knn_cv.best_score_))

# Use the best estimator to calculate accuracy on the test data
best_model_knn = knn_cv.best_estimator_
test_accuracy_knn = best_model_knn.score(X_test, y_test)
print('KNN - Test Accuracy: {:.2f}'.format(test_accuracy_knn))

# Make predictions using the KNN model
yhat_knn = best_model_knn.predict(X_test)

# Plot the confusion matrix for the KNN model
def plot_confusion_matrix(y_true, y_pred, title='Confusion Matrix'):
    cm = confusion_matrix(y_true, y_pred)
    ax = plt.subplot()
    sns.heatmap(cm, annot=True, ax=ax, fmt='d', cmap='Blues');  # fmt='d' for integer annotations
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title(title)  # Set the title here
    ax.xaxis.set_ticklabels(['Did Not Land', 'Landed']); 
    ax.yaxis.set_ticklabels(['Did Not Land', 'Landed']) 
    plt.show()

# Plot the confusion matrix with a title
plot_confusion_matrix(y_test, yhat_knn, title='KNN Confusion Matrix')

