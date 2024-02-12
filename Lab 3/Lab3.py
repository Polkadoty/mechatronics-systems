import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Sample data
data = [
    [10, 0.5706, 0.0007],
    [20.09, 1.013, 0.00071],
    [29.99, 1.82, 0.00088],
    [40.04, 2.485, 0.0009],
    [50.01, 3.023, 0.0008],
    [60.09, 3.699, 0.00078],
    [80.06, 4.996, 0.0004]
]



# Extracting x, y, and std from the data
x = [row[0] for row in data]
y = [row[1] for row in data]
std = [row[2] for row in data]

slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Print the R-squared value
print("R-squared:", r_value**2)

# Creating the plot
plt.errorbar(x, y, yerr=std, fmt='o', capsize=4)

# Adding labels and title
plt.xlabel('Distance')
plt.ylabel('Voltage')
plt.title('Voltage vs Distance')

# Plot the linear regression line
plt.plot(x, [slope*i + intercept for i in x])

# Displaying the plot
plt.show()# Perform linear regression



# Print what range the R-squared value is in
if r_value**2 > 0.8:
    print("The R-squared value is in the range of 0.8-1, which means the linear regression is a good fit.")
else:
    print("The R-squared value is not in the range of 0.8-1, which means the linear regression is not a good fit.")


# New dataset
new_data = [
    [10, 1.674, 0.0009],
    [20, 1.692, 0.0009],
    [30, 1.713, 0.0009],
    [40, 1.705, 0.0009],
    [50, 1.718, 0.00095],
    [60, 1.731, 0.00091],
    [70, 1.751, 0.00093],
    [80, 1.757, 0.00099],
    [90, 1.763, 0.0010],
    [100, 1.781, 0.00097]
]

# Extracting x, y, and std from the new data
new_x = [row[0] for row in new_data]
new_y = [row[1] for row in new_data]
new_std = [row[2] for row in new_data]

# Plotting the new data
plt.errorbar(new_x, new_y, yerr=new_std, fmt='o', capsize=4)


# Fit a function to the data
coefficients2 = np.polyfit(new_x, new_y, 2)
fit_function2 = np.poly1d(coefficients2)

# Perform linear regression
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(new_x, new_y)

# Plot the linear regression line
plt.plot(new_x, [slope2*i + intercept2 for i in new_x], label='Linear Regression')

# # Plotting the fitted function
# plt.plot(x, fit_function2(x), label='Fitted Function')

# Displaying the legend
plt.legend()

# Displaying the plot
plt.show()

# Print the R-squared value
print("R-squared:", r_value2**2)

# Print what range the R-squared value is in
if r_value2**2 > 0.8:
    print("The R-squared value is in the range of 0.8-1, which means the linear regression is a good fit.")
else:
    print("The R-squared value is not in the range of 0.8-1, which means the linear regression is not a good fit.")
