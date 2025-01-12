# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
My r^2 value is .85, which means the model is pretty accurate.

2. Is your model accurate? Why or why not?

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
10 year old car: $9112.53
20 year old car: $1840.76

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

Because it is a linear model, the line may cross into the negatives and return negative values. Because the cars are so old and well-used, the car isn't worth money anymore.