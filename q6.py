import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/processed_student_performance.csv")

#Bar chart: Student names vs final scores
plt.figure(figsize=(20, 6))
bars = plt.bar(df["Student"], df["Final_Score"], color="blue")
plt.title("Final Scores by Student", fontsize=14, fontweight="bold")
plt.xlabel("Student Name")
plt.ylabel("Final Score")
plt.xticks(rotation=45, ha="right")
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,   # x: center of the bar
        height - 5,                          # y: slightly below the top (inside the bar)
        f"{height:.0f}",                     # label text
        ha="center", va="top",
        color="white", fontsize=9
    )
plt.tight_layout()
plt.savefig("./plots/final_scores.png", dpi=150)
plt.close()

#Scatter plot: Hours studied vs final score
plt.figure(figsize=(8, 6))
plt.scatter(df["Hours_Studied"], df["Final_Score"], color="orange", edgecolor="black")
plt.title("Hours Studied vs Final Score", fontsize=14, fontweight="bold")
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("./plots/study_vs_score.png", dpi=150)
plt.close()

#Histogram: Distribution of final scores
plt.figure(figsize=(8, 6))
plt.hist(df["Final_Score"], bins=10, color="green", edgecolor="black")
plt.title("Distribution of Final Scores", fontsize=14, fontweight="bold")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("./plots/score_distribution.png", dpi=150)
plt.close()


print("All four plots saved successfully.")