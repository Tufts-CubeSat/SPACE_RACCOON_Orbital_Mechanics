import math

FIELD_OF_VIEW = 92.5 # in degrees, radian(FIELD_OF_VIEW) gives radians
RESOLUTION = 6000
DIAGONAL_FOV = 104
CUBESAT_VELOCITY = 6700 # km/second
SPACE_DEBRIS_DENSITY = 1e-5 # average density of debris at orbit of 550km

def probability_debris_period(debris_size, duration):
	return (1-(math.e**(-1 * SPACE_DEBRIS_DENSITY*scan_volume(debris_size)*duration))) * 100

def scan_volume(debris_size): # meters
	scan_volume_meters_cubed_per_sec =math.pi * (max_viewing_distance(debris_size) * math.tan(math.radians(FIELD_OF_VIEW /2)))**2 * CUBESAT_VELOCITY
	return scan_volume_meters_cubed_per_sec/(1000**3)  # return unit: kilometers cubed per second
def max_viewing_distance(debris_size):
	return debris_size / angular_resolution()

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