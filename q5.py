import pandas as pd

df = pd.read_csv("./data/student_performance.csv")

#Print the first five rows
print("First 5 rows:")
print(df.head())

#Print the number of rows and columns
print("\nRows: ", df.shape[0])
print("Columns: ", df.shape[1])


#Display the column names
print("\nColumn names:", list(df.columns))

#Check whether the dataset contains missing values
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nAny missing values at all?", df.isnull().values.any())

#Calculate the average Final_Score
avg_final_score = df["Final_Score"].mean()
print("\nAverage Final_Score:", avg_final_score)

#Find the student with the highest Final_Score
top_student = df.loc[df["Final_Score"].idxmax()]
print("\nStudent with highest Final_Score:")
print(top_student)

#Create a new column: Improvement = Final_Score - Previous_Score
df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

#Display only students with attendance >= 80
high_attendance = df[df["Attendance"] >= 80]
print("\nStudents with Attendance >= 80:")
print(high_attendance)

#Sort the DataFrame by Final_Score in descending order
df_sorted = df.sort_values(by="Final_Score", ascending=False)
print("\nDataFrame sorted by Final_Score (descending):")
print(df_sorted)

#Save the processed DataFrame as processed_student_performance.csv
df_sorted.to_csv("./data/processed_student_performance.csv", index=False)
print("\nSaved as processed_student_performance.csv")