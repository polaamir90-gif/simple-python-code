import numpy as np

grades = np.array([
    [80, 90, 70, 85],
    [95, 88, 92, 78],
    [60, 70, 65, 75]
])

weights = np.array([0.3, 0.25, 0.25, 0.2])
prediction = np.dot(grades, weights)
print(f"Final Scores: {prediction.round(3)}")

normalized = (prediction - prediction.min()) / (prediction.max() - prediction.min())
print(f"Norm: {normalized.round(2)}")


Transpose = grades.T
print(f"Shape before T: {grades.shape}")
print(f"Shape after T: {Transpose.shape}")
Maximum = np.max(prediction)
print(f"Top Student Score: {Maximum}")