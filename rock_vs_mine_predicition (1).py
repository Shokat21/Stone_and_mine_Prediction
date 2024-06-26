# -*- coding: utf-8 -*-
"""Rock vs Mine Predicition

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UqoR4wO51wlYsj2L1Ifp4pxl71rXvcK5

Importing the dependicies

numpy is used for craeting numpy arrays
pandas are used for loadinf our  data from numbers into good table as data frames
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and Data processing"""

#loading the dataset to a pandas dataframe
sonar_data = pd.read_csv('/content/Copy of sonar data.csv',header=None)

"""Prints first five rows of data set from sonar_data"""

sonar_data.head()

# number of rows and columns(208rows , 61 cloumns)
sonar_data.shape

#statical measures of this Data
sonar_data.describe()

sonar_data[60].value_counts() #to see how many rocks and  mine examples are their!

"""M ---> mine
R---> rock
"""

sonar_data.groupby(60).mean()

"""Lets try to separte the data and the labels"""

#spearting data and label(rock and mine)
# we are storing each value in x expect the last column
X = sonar_data.drop(columns=60, axis = 1)
Y= sonar_data[60]#storing 60th cloumn in Y|

print(X)
print(Y)

"""Successfully Splitted the data and the labels form the sonar data

Training and test data
"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size =0.1, stratify = Y, random_state =1)
#using 10% of the data for the test (0.1) using stratify to split the data,random state to split the data ina particular order

print(X.shape, X_train.shape, X_test.shape)

"""in the original x = 208 ex , train data= 187 ins and in test = 21 ins"""

print(X_train)
print(Y_train)

"""Model Training---> logisctic regression model"""

model = LogisticRegression()

#training Logistic regression model with training data
model.fit(X_train,Y_train)

"""Model Evaluation

"""

#finding Accuracy on the trainig data(upto 70% is a good acc)
X_train_prediction = model.predict(X_train)
training_data_accuracy= accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data : ',training_data_accuracy)

#finding accuracy of test data
X_test_prediction = model.predict(X_test)
test_data_accuracy= accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data: ', test_data_accuracy)

"""making a predictive System"""

input_data= (0.0200,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032)

#changing the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are prediciting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction =model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]=='R'):
  print("Rock")
else:
    print("Mine")

