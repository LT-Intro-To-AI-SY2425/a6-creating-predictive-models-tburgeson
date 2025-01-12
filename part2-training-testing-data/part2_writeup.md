# Part 2 - Training and Testing Data Writeup

After completing `a6_part2.py` answer the following questions

## Questions to answer

1. What makes this model more effective than the model you created in the previous lesson?
Varying subsets of the datset are used to test against other random datapoints, so the accuracy of the dataset to repredict its own data can be verified. This is better than the first dataset because we can verify that the model can predict known datapoints.

2. What does the R squared coefficient tell you about the model?
The r^2 value is .65, which means the model is able to predict data about 65 percent correctly.

3. Would you say that your model is accurate? What evidence supports your conclusion? Consider the meaning of the predicted and actual values in the context of the chart below from the American Heart Association’s website on understanding blood pressure.

I would say my model is accurate because age does have a correlation with blood pressure and my model has been able to predict pressure related to the age of people in this dataset. 