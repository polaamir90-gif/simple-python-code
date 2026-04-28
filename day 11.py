import numpy as np
"""
scores = np.array([85, 92, 45, 78, 60, 55, 88, 73, 91, 40])
avg = np.mean(scores)
maxscore=np.max(scores)
minscore=np.min(scores)
print(f"Average: {avg}")
print(f"Max: {maxscore} | Min: {minscore}")
above_average=scores[scores>avg]
print(f"Above Average: {above_average}")
passed=np.sum([scores>=60])
print(f"Passed: {passed}")
"""
grades = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [60, 55, 70],
    [45, 50, 40]
])
avg_score=np.mean(grades,axis=1)
avg_subject=np.mean(grades,axis=0)
top_student =np.max(avg_score)
print(f"Student Averages: {avg_score.round(1)}")
print(f"Subject  Averages: {avg_subject.round(1)}")
print(f"Top Student: {top_student.round(1)}")
list_student1=avg_score[avg_score>60]
list_subject1=np.sum([avg_subject>70])
print(f"Students with an average above 60: {list_student1.round(1)}")
print(f"Number of subjects with an average above: {list_subject1}")