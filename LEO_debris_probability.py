import math

# constants
FIELD_OF_VIEW = 92.5 # in degrees, radian(FIELD_OF_VIEW) gives radians
MEGAPIXEL_RESOLUTION = 24 # in megapixels
DIAGONAL_FOV = 104
CUBESAT_VELOCITY = 6700 # km/second
SPACE_DEBRIS_DENSITY = 2.67e-5 # average density of debris at orbit of 550km

# Function: probability_in_size_range
# Inputs:
#   debris_size_min (float): Minimum size of debris in meters
#   debris_size_max (float): Maximum size of debris in meters
#   duration (float): Duration over which the probability is calculated in seconds
# Returns:
#   float: Probability of detecting any debris within the specified size range during the given duration
def probability_in_size_range(debris_size_min, debris_size_max, duration):
    # Number of intervals for averaging probability across the range
    num_intervals = 10
    size_step = (debris_size_max - debris_size_min) / num_intervals
    
    # Sum probabilities for each step in the range and calculate the average
    probability_sum = 0
    for i in range(num_intervals + 1):
        size = debris_size_min + i * size_step
        probability_sum += probability_debris_period(size, duration)
    
    # Average probability across all size steps
    average_probability = probability_sum / (num_intervals + 1)
    return average_probability


# Function: probability_debris_period
# Inputs:
#	debris_size: the size in meters of the piece of debris of interest
#	duration: the length of time in seconds over which the probability of detection is being measured
# Returns:
# 	float: Probability of detecting debris of the specified size during the given duration, as a percentage (0-100).

def probability_debris_period(debris_size, duration):
	return (1-(math.e**(-1 * SPACE_DEBRIS_DENSITY*scan_volume(debris_size)*duration))) * 100

# Function: scan_volume
# Input: debris_size: the size in meters of the piece of debris of interest
# Returns:
# 	float: Volume of space scanned per second in cubic kilometers, considering the debris size.
def scan_volume(debris_size): # meters
	scan_volume_meters_cubed_per_sec =math.pi * (max_viewing_distance(debris_size) * math.tan(math.radians(FIELD_OF_VIEW /2)))**2 * CUBESAT_VELOCITY
	return scan_volume_meters_cubed_per_sec/(1000**3)  # return unit: kilometers cubed per second

# Function: max_viewing_distance
# Input:
#   debris_size (float): Size of the debris in meters.
# Returns:
#   float: Maximum viewing distance for debris of the specified size in meters.
def max_viewing_distance(debris_size):
	return debris_size / angular_resolution()

# Function: angular_resolution
# Input: None N/A
# Returns:
# 	float: Angular resolution of the cubesat's sensor in radians.
def angular_resolution():
	return math.radians(DIAGONAL_FOV) / int(math.sqrt(MEGAPIXEL_RESOLUTION * 1e6))

if __name__ == "__main__":
	print("Probability of finding 1mm debris within one orbit",probability_debris_period(0.001,5700))
	print("Probability of finding 1cm debris within one orbit",probability_debris_period(0.01,5700))
	print("Probability of finding 5cm debris within one orbit",probability_debris_period(0.05,5700))
	print("Probability of finding 10cm debris within one orbit",probability_debris_period(0.1,5700))
	print("Probability of finding 1mm debris within one day",probability_debris_period(0.001,86400))
	print("Probability of finding 1cm debris within one day",probability_debris_period(0.01,86400))
	print("Probability of finding 5cm debris within one day",probability_debris_period(0.05,86400))
	print("Probability of finding 10cm debris within one day",probability_debris_period(0.1,86400))
	print("Probability of finding 1mm debris within one year",probability_debris_period(0.001,31536000))
	print("Probability of finding debris between 1mm and 1cm within one day:", probability_in_size_range(0.001, 0.01, 86400))
	print("Probability of finding debris between 1cm and 10cm within one day:", probability_in_size_range(0.01, 0.1, 86400))
	print("Probability of finding debris between 5cm and 10cm within one day:", probability_in_size_range(0.05, 0.1, 86400))
	print("Probability of finding debris between 5cm and 10cm within one orbit:", probability_in_size_range(0.05, 0.1, 5700))