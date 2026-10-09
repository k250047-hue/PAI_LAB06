import numpy as np

image = np.array([
    [20, 50, 80, 100, 120],
    [30, 60, 90, 130, 150],
    [40, 70, 110, 160, 180],
    [50, 85, 140, 200, 220],
    [60, 100, 170, 230, 255]
])

minimum = np.min(image)
maximum = np.max(image)
mean = np.mean(image)

threshold = 120

mask = image > threshold

thresholded_image = np.where(image > threshold, 255, 0)

print("Original Image:")
print(image)

print("\nMinimum Intensity:", minimum)
print("Maximum Intensity:", maximum)
print("Mean Intensity:", mean)

print("\nBinary Mask:")
print(mask.astype(int))

print("\nThresholded Image:")
print(thresholded_image)