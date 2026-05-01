import numpy as np

scores = np.random.normal(loc=75, scale=12, size=500)

Mean   = np.mean(scores)
Median = np.median(scores)
Std    = np.std(scores)

print(f"Mean: {Mean:.1f} | Std: {Std:.1f} | Median: {Median:.1f}")

excellent = np.sum(scores > 90)
good      = np.sum((scores >= 75) & (scores <= 90))
needs     = np.sum(scores < 75)
total     = len(scores)

print(f"\nExcellent (>90):  {excellent/total*100:.1f}%")
print(f"Good (75-90):     {good/total*100:.1f}%")
print(f"Needs Work (<75): {needs/total*100:.1f}%")

z = (95 - Mean) / Std
print(f"\nZ-Score for 95: {z:.2f}")