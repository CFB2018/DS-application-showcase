
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
def plot_confusion_matrix(y,y_predict):
    cm = confusion_matrix(y, y_predict)
    ax= plt.subplot()
    sns.heatmap(cm, annot=True, ax = ax); #annot=True to annotate cells
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title('Confusion Matrix'); 
    ax.xaxis.set_ticklabels(['did not land', 'land']); ax.yaxis.set_ticklabels(['did not land', 'landed']) 
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


# Check the data types of the columns in X_train_final
#print(X_train_final.dtypes)

# Standardize the features
X_train_final = scaler.fit_transform(X_train_final)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Define the parameter grid
parameters = {
    'C': np.logspace(-2, 0, 20),  # Regularization strength,
    'penalty': ['none', 'l2'],  # Regularization type
    'solver': ['newton-cg', 'lbfgs'],  # Optimization algorithm
    'multi_class': ['multinomial']  # Multi-class option
}

# Create a logistic regression model
lr = LogisticRegression(max_iter=1000)

# Create the GridSearchCV object with cv=10
logreg_cv = GridSearchCV(lr, parameters, cv=10, verbose=0)

# Fit the GridSearchCV object to the training data
logreg_cv.fit(X_train, y_train)

# Print the best parameters and accuracy
print("Tuned hyperparameters (best parameters):", logreg_cv.best_params_)
print("Accuracy:", logreg_cv.best_score_)

# Calculate accuracy on the test data using the score method
# Use the best estimator to calculate accuracy on the test data
best_model = logreg_cv.best_estimator_
accuracy = best_model.score(X_test, y_test)
print('Accuracy on test data: {:.2f}'.format(accuracy))