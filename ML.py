
    # Objective: Create a ML pipeline to predict first stage landing.
    
    # Author: CFB
    # Date: 2025-01-30
    # Perform EDA and determine training labels
    # Create a column for the class, standardize the data, split into training/test data 
    # & find best hyperparameter for SVM, Classification Trees and Logistic Regression
    
    
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier 
    




# Load the dataframe
data = pd.read_csv('dataset_part_2.csv')
print(data.head())
