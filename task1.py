# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kXGuLxa3M33AnJEwkN4ko1GNRwAPF4Up

# **Veda Jeevitha.R**

# Task-1

# Prediction using Supervised ML

importing the libaries
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
# %matplotlib inline

"""reading the data"""

data = pd.read_csv("http://bit.ly/w-data")
print("The given data")
data.head(5)

data.shape   #to get no of rows and columns

data.info()   #to get the type of data

"""plotting the distribution of scores

"""

data.plot(x="Hours",y="Scores",style="*")
plt.xlabel("Hours")
plt.ylabel("Percentage")
plt.show()

"""The plot shows the positive relation between the variables

**Preparing the data**

Divide the data into attributes and labels
"""

X = data.iloc[:, :-1].values  
y = data.iloc[:, 1].values

"""Splitting the data into training and test set"""

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                            test_size=0.2, random_state=0)

"""**Training the Algorithm**"""

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

# Plotting the regression line
line = regressor.coef_*X+regressor.intercept_   
plt.scatter(X, y)
plt.plot(X, line,color="red");
plt.show()

"""**Predictions**"""

print(X_test)
y_pred = regressor.predict(X_test)

"""**Comparing Actual vs Predicted**"""

d= pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
d

hours = [[9.25]]
own_pred = regressor.predict(hours)
print("If the student studies for 9.25 hour then the predicted score is {}".format(own_pred[0]))

"""**Evaluating the model**"""

from sklearn import metrics  
print('Mean Absolute Error:', 
      metrics.mean_absolute_error(y_test, y_pred))