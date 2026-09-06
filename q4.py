import numpy as np

hours_studied = np.array([5, 8, 2, 7, 6])
attendance = np.array([90, 95, 60, 85, 78])
previous_scores = np.array([65, 89, 55, 80, 70])
final_scores = np.array([70, 91, 58, 87, 76])


print("Hours Studied -> shape:", hours_studied.shape, ", dtype:", hours_studied.dtype)
print("Attendance    -> shape:", attendance.shape, ", dtype:", attendance.dtype)
print("Previous Scores -> shape:", previous_scores.shape, ", dtype:", previous_scores.dtype)
print("Final Scores  -> shape:", final_scores.shape, ", dtype:", final_scores.dtype)

mean_score = np.mean(final_scores)
print("\nMean Final Score:", mean_score)

max_score = np.max(final_scores)
min_score = np.min(final_scores)
print("Max Final Score:", max_score)
print("Min Final Score:", min_score)

std_score = np.std(final_scores)
print("Standard Deviation of Final Scores:", std_score)

final_scores_bonus = final_scores + 5
print("Final Scores with Bonus:", final_scores_bonus)

passed_75 = final_scores_bonus >= 75
print("Scored at least 75 (Boolean):", passed_75)

scores_75_and_above = final_scores_bonus[passed_75]
print("Scores grater than or equal to 75:", scores_75_and_above)