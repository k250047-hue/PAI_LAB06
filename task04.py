import numpy as np

readings = np.array([
    [20, 25, 30, 35, 40],
    [30, 35, 40, 45, 50],
    [15, 20, 25, 30, 35],
    [40, 45, 50, 55, 60]
])

sensor_mean = np.mean(readings, axis=1)
sensor_min = np.min(readings, axis=1)
sensor_max = np.max(readings, axis=1)
sensor_std = np.std(readings, axis=1)

highest_sensor = np.argmax(sensor_mean) + 1

threshold = 40
above_threshold = readings > threshold

print("Sensor Readings:")
print(readings)

print("\nMean of Each Sensor:")
print(sensor_mean)

print("\nMinimum of Each Sensor:")
print(sensor_min)

print("\nMaximum of Each Sensor:")
print(sensor_max)

print("\nStandard Deviation of Each Sensor:")
print(sensor_std)

print("\nSensor with Highest Average:", highest_sensor)

print("\nReadings Above Threshold:")
print(above_threshold)

print("\nValues Above Threshold:")
print(readings[above_threshold])