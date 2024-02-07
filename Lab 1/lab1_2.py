import math
import numpy as np

# Define the given dimensions in millimeters as dictionaries
measurement1 = {
    'trapezoid1': {'b_short': 19.03, 'b_long': 38.03, 'height': 8.66},
    'trapezoid2': {'b_short': 19.27, 'b_long': 38.03, 'height': 8.33},
    'rectangle': {'base': 38.03, 'height': 23.60},
    'circle': {'diameter': 15.89},
    'height': {'height': 41.03},
    'mass': {'mass': 134.45}

}

measurement2 = {
    'trapezoid1': {'b_short': 19.11, 'b_long': 38.04, 'height': 8.74},
    'trapezoid2': {'b_short': 19.31, 'b_long': 38.04, 'height': 8.47},
    'rectangle': {'base': 38.04, 'height': 23.60},
    'circle': {'diameter': 15.77},
    'height': {'height': 41.06},
    'mass': {'mass': 134.43}
}

# Combine the measurements into one dictionary called dimensions
dimensions = {**measurement1, **measurement2}

# Define uncertainty
uncertainty = .005  # mm

# Function to calculate the area of a trapezoid
def area_trapezoid(b_short, b_long, height):
    return 0.5 * (b_short + b_long) * height

# Function to calculate the area of a rectangle
def area_rectangle(base, height):
    return base * height

# Function to calculate the area of a circle
def area_circle(diameter):
    radius = diameter / 2
    return math.pi * (radius**2)

# Calculate areas of the shapes
A_trapezoid1 = area_trapezoid(**dimensions['trapezoid1'])
A_trapezoid2 = area_trapezoid(**dimensions['trapezoid2'])
A_rectangle = area_rectangle(**dimensions['rectangle'])
A_circle = area_circle(**dimensions['circle'])

# Calculate the total area of the cross-section
total_area_cross_section = A_trapezoid1 + A_trapezoid2 + A_rectangle - A_circle

# Function to calculate volume
def calculate_volume(area, height):
    return area * height

# Function to calculate density
def calculate_density(mass, volume):
    volume_cm3 = volume / 1000  # Convert mm^3 to cm^3 for density calculation
    return mass / volume_cm3

# Calculate volume and density
volume_mm3 = calculate_volume(total_area_cross_section, dimensions['height']['height'])
density_g_cm3 = calculate_density(dimensions['mass']['mass'], volume_mm3)

print(A_trapezoid1, A_trapezoid2, A_rectangle, A_circle, total_area_cross_section, volume_mm3, density_g_cm3)

# Calculate uncertainty in areas
def calculate_uncertainty_area_trapezoid(b_short, b_long, height):
    return 0.5 * (b_short + b_long) * height * uncertainty

def calculate_uncertainty_area_rectangle(base, height):
    return base * height * uncertainty

def calculate_uncertainty_area_circle(diameter):
    radius = diameter / 2
    return math.pi * (radius**2) * uncertainty

# Calculate uncertainty in volume
def calculate_uncertainty_volume(area, height):
    return area * height * uncertainty

uncertainty_volume_mm3 = calculate_uncertainty_volume(total_area_cross_section, dimensions['height']['height'])

# Calculate uncertainty in density
def calculate_uncertainty_density(mass, volume):
    return calculate_density(mass, volume) * math.sqrt((uncertainty_volume_mm3 / volume_mm3)**2)

uncertainty_density_g_cm3 = calculate_uncertainty_density(dimensions['mass']['mass'], volume_mm3)

print(uncertainty_volume_mm3, uncertainty_density_g_cm3)

# Print results
print('The volume of the object is', volume_mm3, 'mm^3')
print('The density of the object is', density_g_cm3, 'g/cm^3')
print('The uncertainty in the volume is', uncertainty_volume_mm3, 'mm^3')
print('The uncertainty in the density is', uncertainty_density_g_cm3, 'g/cm^3')

# Function to propagate uncertainty through the entire process
def propagate_uncertainty():
    # Calculate uncertainty in areas
    uncertainty_A_trapezoid1 = calculate_uncertainty_area_trapezoid(**dimensions['trapezoid1'])
    uncertainty_A_trapezoid2 = calculate_uncertainty_area_trapezoid(**dimensions['trapezoid2'])
    uncertainty_A_rectangle = calculate_uncertainty_area_rectangle(**dimensions['rectangle'])
    uncertainty_A_circle = calculate_uncertainty_area_circle(**dimensions['circle'])

    # Calculate uncertainty in total area
    uncertainty_total_area_cross_section = math.sqrt(uncertainty_A_trapezoid1**2 + uncertainty_A_trapezoid2**2 + uncertainty_A_rectangle**2 + uncertainty_A_circle**2)

    # Calculate uncertainty in volume
    uncertainty_volume_mm3 = calculate_uncertainty_volume(total_area_cross_section, dimensions['height']['height'])

    # Calculate uncertainty in density
    uncertainty_density_g_cm3 = calculate_uncertainty_density(dimensions['mass']['mass'], volume_mm3)

    print('Uncertainty in A_trapezoid1:', uncertainty_A_trapezoid1)
    print('Uncertainty in A_trapezoid2:', uncertainty_A_trapezoid2)
    print('Uncertainty in A_rectangle:', uncertainty_A_rectangle)
    print('Uncertainty in A_circle:', uncertainty_A_circle)
    print('Uncertainty in total_area_cross_section:', uncertainty_total_area_cross_section)
    print('Uncertainty in volume:', uncertainty_volume_mm3)
    print('Uncertainty in density:', uncertainty_density_g_cm3)

propagate_uncertainty()

# Calculate the sample mean for each density value:
density_values = [2.7396, 2.7541]
mean_density = np.mean(density_values)
print('Sample Mean: ', mean_density)

# Calculate the standard deviation of the density values
std_dev_density = np.std(density_values)
print('Standard Deviation: ', std_dev_density)

# Calculate the measurement with confidence interval
confidence_interval = 1.96 * (std_dev_density / math.sqrt(len(density_values)))
print('Confidence Interval: ', confidence_interval)