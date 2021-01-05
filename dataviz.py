#Data Visualization and Diving into Matplotlib

import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import datasets

data = pd.read_csv('sma_data.csv')
# # print(data.head())

# plt.scatter(data.percent_senior, data.crime_rate) #plotting the scatterplot

# plt.title('Plot of Crime Rate vs. Percent Senior')
# plt.xlabel('Percent Senior')
# plt.ylabel('Crime Rate')

# plt.show() #showing the figure

#====================================================================================================

#LINE PLOT

# plt.figure(figsize=(12,5)) #12x5 plot 
# plt.plot(data.work_force, data.income, linestyle = '--', marker = 'o', color = 'r', label = 'labor')
# # plt.scatter(data.work_force, data.income, marker='x', color = 'r')
# # plt.xlabel('Work Force')
# # plt.ylabel('Income')
# # plt.show()

# plt.plot(data.physicians, data.income, label = 'graduates')
# plt.legend()
# plt.show()

#====================================================================================================
#SUBPLOTS

# plt.figure(figsize=(12,5))
# plt.subplot(1,2,1)
# plt.plot(data.work_force, data.income, linestyle = '--', marker = 'o', color = 'r', label = 'labor')
# plt.title('Income vs. Workforce')

# plt.subplot(1,2,2)
# plt.plot(data.physicians, data.income, label = 'graduates')
# plt.title('Physicians vs. Income')

# plt.suptitle("Subplots") #gives overall title to subplots
# plt.show()

#====================================================================================================

#HISTOGRAMS

# plt.title('Histogram')
# plt.xlabel('Percentage of Senior Citizens')
# plt.ylabel('Frequency')

# plt.hist(data.percent_senior)
# plt.show()

#====================================================================================================
#Working with Seaborn left at 37 minutes.. unable to load iris dataset

