# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
It tends to vary between .65 and .85, so not super accurate. I think this is because the data is on different scales without using StandardScaler, so numbers like salaries and ages are different magnitues and will cause inconsistent results.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
With StandardScaler, the r^2 factor is much more consistent, staying around .84. It's accurate enough for predicting buyer's habits.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model did pretty good. The model might miss inputs where it doesn't have a lot of acccurate training data to draw conclusions from.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
No, she would not.