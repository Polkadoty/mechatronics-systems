import numpy as np
import matplotlib.pyplot as plt
import math

def propagate_uncertainty(value, uncertainty, func):
    derivative = np.abs(func(value + uncertainty) - func(value - uncertainty)) / (2 * uncertainty)
    propagated_uncertainty = derivative * uncertainty
    return propagated_uncertainty

door_frame = [7.171, 7.154, 7.177] # mm
conversion2 = np.array(door_frame) / np.mean(door_frame)
conversion = 36 / np.array(door_frame) # in
in_to_ft = 1 / 12 # ft
foot_to_m = 0.3048  # ft/m

totalAreaCAD = 9431.731 # mm^2
cadUncertainty = 0.0005 # mm^2

totalArea_CAD2 = totalAreaCAD * conversion2**2


totalArea_in = totalAreaCAD * conversion**2

print("Total area of cross section CAD: " + str(totalArea_CAD2) + " CADmm^2")
print("Total area of cross section in: " + str(totalArea_in) + " in^2")
print("Total area of cross section ft: " + str(totalArea_in * in_to_ft**2) + " ft^2")
print("Total area of cross section m: " + str(totalArea_in * in_to_ft**2 * foot_to_m**2) + " m^2")

# Example usage of the propagate_uncertainty function
propagated_area_uncertainty = propagate_uncertainty(totalAreaCAD, cadUncertainty, lambda x: x * conversion**2)
print("Propagated uncertainty of total area: " + str(propagated_area_uncertainty) + " in^2")

# Take mean of areas in feet
mean_area_ft = np.mean(totalArea_in * in_to_ft**2)
print("Mean area in ft: " + str(mean_area_ft) + " ft^2")

# Take standard deviation of areas compared to mean
std_dev_area_ft = np.std(totalArea_in * in_to_ft**2)
print("Standard deviation of area in ft: " + str(std_dev_area_ft) + " ft^2")

# Take mean of areas in meters
mean_area_m = np.mean(totalArea_in * in_to_ft**2 * foot_to_m**2)
print("Mean area in m: " + str(mean_area_m) + " m^2")

# Take standard deviation of areas compared to mean
std_dev_area_m = np.std(totalArea_in * in_to_ft**2 * foot_to_m**2)
print("Standard deviation of area in m: " + str(std_dev_area_m) + " m^2")

# Calculate bias error
bias_error = cadUncertainty - std_dev_area_m
print("Bias error: " + str(bias_error) + " m^2")

# Calculate standard error
standard_error = propagated_area_uncertainty - std_dev_area_m
print("Standard error: " + str(standard_error) + " m^2")
