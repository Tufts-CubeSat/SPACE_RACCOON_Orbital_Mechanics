import math

# constants
FIELD_OF_VIEW = 92.5 # in degrees, radian(FIELD_OF_VIEW) gives radians
RESOLUTION = 6000
DIAGONAL_FOV = 104
CUBESAT_VELOCITY = 6700 # km/second
SPACE_DEBRIS_DENSITY = 1e-5 # average density of debris at orbit of 550km

# Function: probability_debris_period
# Inputs:
#	debris_size: the size in meters of the piece of debris of interest
#	duration: the length of time in seconds over which the probability of detection is being measured
# Returns:
# float: Probability of detecting debris of the specified size during the given duration, as a percentage (0-100).

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
	return math.radians(DIAGONAL_FOV) / RESOLUTION

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