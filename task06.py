import numpy as np

rng1 = np.random.default_rng(42)
data1 = rng1.normal(loc=50, scale=10, size=1000)

rng2 = np.random.default_rng(100)
data2 = rng2.normal(loc=50, scale=10, size=1000)


mean1 = np.mean(data1)
median1 = np.median(data1)
std1 = np.std(data1)
minimum1 = np.min(data1)
maximum1 = np.max(data1)

inside1 = np.sum((data1 >= mean1 - std1) &
                 (data1 <= mean1 + std1))
percentage1 = (inside1 / len(data1)) * 100


mean2 = np.mean(data2)
median2 = np.median(data2)
std2 = np.std(data2)
minimum2 = np.min(data2)
maximum2 = np.max(data2)

inside2 = np.sum((data2 >= mean2 - std2) &
                 (data2 <= mean2 + std2))
percentage2 = (inside2 / len(data2)) * 100


print("Results for Seed 42")
print("Mean:", mean1)
print("Median:", median1)
print("Standard Deviation:", std1)
print("Minimum:", minimum1)
print("Maximum:", maximum1)
print("Percentage inside one standard deviation:", percentage1, "%")

print("\nResults for Seed 100")
print("Mean:", mean2)
print("Median:", median2)
print("Standard Deviation:", std2)
print("Minimum:", minimum2)
print("Maximum:", maximum2)
print("Percentage inside one standard deviation:", percentage2, "%")