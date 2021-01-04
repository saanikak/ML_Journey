import pandas as pd 
import numpy as np 

# #===================================================================================================
# print("===========================================================================")
# print("Series and Dataframe")
# print('--------------------')

# #Series and Dataframe

# #creating a series using a list
# l = [4,1,3,5,6,4,6,7]
# s = pd.Series(l)
# print(s)

# #creating a series using a dictionary
# d = {"Saanika": 19, "Sharv":8, "Anjali": 43, "Swarraj": 49}
# s = pd.Series(d)
# print(s)

# #creating a DataFrame using a list
# l = [[22,"Saanika",45.66], [55,"Annika",56.34], [64,"Jessie",45.23]]
# df = pd.DataFrame(l)
# print(df)

# #creating a DataFrame using a numpy array
# nparray = np.array([[34,"Michelle",1965], [2334,"Barack",234], [64,"Sasha",3442]])
# df = pd.DataFrame(nparray, columns = ["Rand1", "Name", "Rand2"], index = [1,2,3])
# print(df)

# #creating a dataframe using a dictionary
# #key of dictionary is a column name, and the value of that key are the elements in that column
# d = {"Car Make": ['Toyota', 'Audi', 'Hyundai'], "Cost":[12322,23234,2343], "Color": ['red', 'blue', 'black'], "Year": [2001,1973,1982]}
# df = pd.DataFrame(d, index = [100,200,300])
# print(df)

# #===================================================================================================

# print("===========================================================================")
# print("Reading/Writing Files + Some Basic Methods/Attributes")
# print('--------------------')

# #Reading/Writing Files + Some Basic Methods/Attributes

# df = pd.read_csv("/Users/saanikak/Documents/Learning/MLBootcamp/NFWBS_PUF_2016_data.csv")
# print(df)

# #converting from datafram to csv

# d = {"Car Make": ['Toyota', 'Audi', 'Hyundai'], "Cost":[12322,23234,2343], "Color": ['red', 'blue', 'black'], "Year": [2001,1973,1982]}
# df = pd.DataFrame(d, index = [100,200,300])

# df = df.to_csv("dftocsv.csv", index= False)

# #Basic methods/attributes of dataframes

scores = pd.read_csv("exam_scores.csv")
# print(scores)
# print(scores.shape)
# print(scores.head()) #first 5 entries
# print(scores.tail()) #last 5 entries
# print(scores.dtypes)

# print(scores.info()) #summary of the dataframe

sma_data = pd.read_csv("sma_data.csv")

# print(sma_data.info())

# #===================================================================================================
# print("===========================================================================")
# print("Indexing, Selecting, and Assigning")
# print('--------------------')

# #Indexing, Selecting, and Assigning

# #INDEXING (selecting specific rows or columns)

# # iloc ---> index based selection
# print(scores.head())
# print(scores.iloc[0]) #first row
# print(scores.iloc[0:5, 4])
# print(scores.iloc[[0,1,2,3], [3,4,5,6]])

# # loc --> label based selection
# print(scores.loc[0:4, ['gender', 'math score', 'reading score', 'writing score']]) # first 4 entries in select categories

# #SELECTING

# print(scores['parental level of education'])
# print(scores[['math score', 'reading score', 'writing score']])

# print(scores['gender'] == 'male') 

# print(scores[scores['gender'] == 'male']) #conditional selection

# #ASSIGNING

# scores['parental level of education'] = 'MBA'
# print(scores['parental level of education'])
# print(scores)

# #HANDS-ON Exercise

# print(sma_data['physicians'])

# sample_data1 = sma_data.loc[[1,3,5,7,9,13], ['land_area', 'work_force', 'income', 'region', 'crime_rate']]
# print(sample_data1)

# sample_data2 = sma_data[sma_data['region'] == 2]
# print(sample_data2)
# print(sample_data2.shape)

# #===================================================================================================
# print("===========================================================================")
# print("Summary and Aggregation Functions")
# print('--------------------')

# #Summary and Aggregation Functions

# #SUMMARY

# #summary of numerical columns
# print(scores.describe())
# #summary of categorical columns 
# print(scores.describe(include = 'object'))

# #summary of numerical and categorical
# print(scores.describe(include = 'all'))

# print(scores['math score'].describe())

# #AGGREGATION
# print(scores.mean())
# print(scores.gender.unique())
# print(scores.gender.value_counts())

# #EXERCISE

# print(sma_data.mean())
# print(sma_data.region.unique())

# print(sma_data.describe(include = 'all'))

# sample_data1 = sma_data[sma_data['region'] == 3]
# print(sma_data.region.value_counts())

# #===================================================================================================
# print("===========================================================================")
# print("Sorting and Renaming")
# print('--------------------')

# #Sorting and Renaming

# print(scores.sort_values(by = 'math score', ascending = False).head())
# print()
# print(scores['reading score'].sort_values(ascending = True).head())

# scores.rename(columns = {
#     'race/ethnicity': 'race', 
#     'parental level of education': 'parent_education_level',
#     'test preparation course': 'test_prep_course', 
#     'math score': 'math_score',
#     'reading score': 'reading_score', 
#     'writing score': 'writing_score'

# }, inplace=True)

# print(scores)

# print(scores.columns)


# #EXERCISE

# print(sma_data.sort_values(by = 'crime_rate' , ascending = False))


# #===================================================================================================
print("===========================================================================")
print("Checking and Filling Missing Data")
print('--------------------')

#Checking and Filling Missing Data

print(sma_data.isnull())
print(sma_data.isna())
print(sma_data.isnull().sum())

#filling missing values

# df.Name.fillna('unknown', inplace = True) #just an example

# df['Marks%'].fillna(df['Marks%'].mean(), inplace = True)

print()
titanic = pd.read_csv('titanic.csv')
print(titanic.isnull().sum())
# print(titanic.isna().sum())

age_mean_before = titanic.Age.mean()
print(age_mean_before)
titanic.Age.fillna(age_mean_before, inplace = True)

age_mean_after = titanic.Age.mean()
print(age_mean_after)


print(titanic.Embarked.value_counts())
titanic.Embarked.fillna('S', inplace = True)
print(titanic.Embarked.value_counts())