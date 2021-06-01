import numpy as np
import matplotlib.pyplot as plt
#  ------------------------ CHALLENGE 1 ------------------------------------

arrNum = np.arange(start=1, stop=40, step=2)
#  Calculating mean, standard deviation and variance
my_mean = np.mean(arrNum)
my_stdn = round(np.std(arrNum), 2)
variance = np.var(arrNum)

#  adding values caltulated above on an array for y axis
values = [my_mean, my_stdn, variance]
# array of names for x axis
xtitle = ["Mean", "Standard Deviation ", "Variance"]

#  looping through the array of names
x_pos = [i for i, _ in enumerate(xtitle)]
plt.bar(x_pos, values, color='#7A5C61')
# labeling the axis of the bar graph
plt.xlabel("Type of Data")
plt.ylabel("Total")
plt.title("Numerical Data")
plt.xticks(x_pos, xtitle)
#  displaying the bar graph
plt.show()

#  ------------------------ CHALLENGE 2 ------------------------------------

nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
#  labeling axis of a histogram
plt.xlabel("Nums")
plt.ylabel("Bins")
plt.title("Histogram of nums against bins.")
#  printing the results
print("nums: ", nums)
print("bins: ", bins)
print("Result:", np.histogram(nums, bins))
plt.hist(nums, bins=bins, color="pink")
#  displaying the histogram
plt.show()
