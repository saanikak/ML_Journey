import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pyplot

# Importing SimpleImputer from sklearn - this will be used to impute data in the cells with missing values
from sklearn.impute import SimpleImputer

#Data Preprocessing 

# importing training data
train = pd.read_csv('/Users/saanikak/Documents/Learning/MLBootcamp/Datasets/titanic_data.csv')
print(train.shape)

#importing test data; will have 1 less column than train bc it won't have the target variable
test = pd.read_csv('/Users/saanikak/Documents/Learning/MLBootcamp/Datasets/titanic_test.csv')
print(test.shape)

#returns datatypes of all variables
print(train.dtypes)

#returns first 5 rows in the dataset
print(train.head())

#returns first row
print(train.iloc[[0]])
print()

#returns 16th row
print(train.iloc[[15]])

#printing the count of missing values corresponding to the variable
train_count_of_missval_by_col = train.isnull().sum()
print(train_count_of_missval_by_col)
print()

#displays only the columns that have missing values
print(train_count_of_missval_by_col[train_count_of_missval_by_col > 0])

# below code will display only the columns with missing values (in percentage of missing values to the total rows)
print(train_count_of_missval_by_col[train_count_of_missval_by_col > 0]/train.shape[0] * 100)

print()

#displays the summary statistics (mean,count,median, std dev, etc.)
print(train.describe())

#displays the value counts of the categorical variables
print()
print(train['Sex'].value_counts())
print()
print(train['Embarked'].value_counts())

#displays the value counts of the people who survived and didn't survive. Also gives the percentage (using normalize)
print()
print(train['Survived'].value_counts())
print()
print(train['Survived'].value_counts(normalize = True))

#dropping/deleting irrelevant columns for our prediction
del train['Name']
del train['Ticket']
del train['PassengerId']

# transform the Survived and Pclass into categorical variable
train['Survived'] = train['Survived'].astype(str)
train['Pclass'] = train['Pclass'].astype(str)

print(train.shape)

# Missing value treatment
# missing values - too many missing values - dropping entire column
del train['Cabin']

# missing values in numeric column many not be NaN or blank. It could be zero as well
# for example, the Fare cannot be zero in our dataset. So the missing value in Fare columns are extracted by filtering for zero
# filter for Fare = 0 and display the shape of the dataframe - 15 rows
print(train[train['Fare'] == 0].shape)

# There are only few rows with missing values in Fare - Listwise or dropping entire rows
train = train[train['Fare'] != 0]
# shape of the training data after dropping rows with missing Fare
print(train.shape)

print(train.isnull().sum())

# missing values - numeric - impute with mean in column age
mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
mean_imputer = mean_imputer.fit(train[['Age']])
train['Age'] = mean_imputer.transform(train[['Age']]).ravel()

print(train.isnull().sum())

#missing values - categorical - impute with mode in the column Embarked
mode_imputer = SimpleImputer(missing_values=np.NaN, strategy='most_frequent')
mode_imputer = mode_imputer.fit(train[['Embarked']])
train['Embarked'] = mode_imputer.transform(train[['Embarked']]).ravel()

print(train.head(20))

#Outlier Methods

