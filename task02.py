import numpy as np

features = np.array([
    [10, 20, 30, 40],
    [12, 25, 35, 45],
    [14, 30, 40, 50],
    [16, 35, 45, 55],
    [18, 40, 50, 60],
    [20, 45, 55, 65],
    [22, 50, 60, 70],
    [24, 55, 65, 75],
    [26, 60, 70, 80],
    [28, 65, 75, 85]
])

mean = np.mean(features, axis=0)
std = np.std(features, axis=0)

standardized = (features - mean) / std

print("Feature Means:")
print(mean)

print("\nFeature Standard Deviations:")
print(std)

print("\nStandardized Features:")
print(standardized)

print("\nMeans After Standardization:")
print(np.mean(standardized, axis=0))

print("\nStandard Deviations After Standardization:")
print(np.std(standardized, axis=0))