import numpy as np
from scipy import stats

scores = np.array([85, 92, 45, 78, 60, 55, 88, 73, 91, 40, 95, 30, 110, 5, 150])

Mean   = np.mean(scores)
Median = np.median(scores)
Std    = np.std(scores)
scores = np.array([85, 92, 45, 78, 60, 55, 88, 73, 91, 40, 95, 30, 110, 5, 150])

z_scores = np.abs(stats.zscore(scores))
outliers = scores[z_scores > 2]
clean    = scores[z_scores <= 2]

ranks      = stats.rankdata(scores)
corr, _    = stats.spearmanr(scores, ranks)

print("=== Before Cleaning ===")
print(f"Mean: {Mean:.1f} | Median: {Median:.1f}")
print(f"Std: {Std:.1f}")
print(f"Outliers: {outliers}")
print(f"Correlation: {corr:.2f}")


print("\n=== After Cleaning ===")
print(f"Mean: {np.mean(clean):.1f} | Median: {np.median(clean):.1f}")
print(f"Std: {np.std(clean):.1f}")