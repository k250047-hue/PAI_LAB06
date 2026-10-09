import numpy as np

data = np.array([10, 20, np.nan, 30, 40, np.nan, 50, 60])

print("Original Array:")
print(data)

missing_values = np.isnan(data)
print("\nNaN Detection:")
print(missing_values)

print("\nNumber of NaN Values:", np.sum(missing_values))

print("\nMean:", np.nanmean(data))
print("Median:", np.nanmedian(data))
print("Minimum:", np.nanmin(data))
print("Maximum:", np.nanmax(data))

mean_value = np.nanmean(data)

data[np.isnan(data)] = mean_value

print("\nArray After Replacing NaNs:")
print(data)

print("\nAre Any NaNs Remaining?", np.isnan(data).any())