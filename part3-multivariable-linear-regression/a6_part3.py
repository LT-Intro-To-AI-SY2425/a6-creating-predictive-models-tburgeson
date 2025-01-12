import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values

#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.15)

#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)

#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 
coef = model.coef_
print("Coefficients:")
print("Miles:", round(coef[0], 2))
print("Age:", round(coef[1], 2))
print("")
print("Intercept: ", round(model.intercept_, 2))
print("Score: ", round(model.score(xtrain, ytrain), 2))

#Loop through the data and print out the predicted prices and the 
#actual prices
print("***************")
print("Testing Results")
for i in range(len(xtest)):
    print("Predicted Price: ", round(model.predict([xtest[i]])[0], 2))
    print("Actual Price: ", ytest[i])
    print

#Predicts the price of a 10 year old car with 89,000 miles and 20 years old with 150,000 miles
print("***************")
print("Predicted Price of a 10 year old car with 89,000 miles: ", round(model.predict([[89000, 10]])[0], 2))
print("Predicted Price of a 20 year old car with 150,000 miles: ", round(model.predict([[150000, 20]])[0], 2))