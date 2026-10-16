import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Student_Name" : ["Ram","Kumar","Rahul","Ajay","Vijay","Rajini","Kamal","Surya","Vishal","Ajith",
                      "Jason","Mukesh","Shathika","Abi","Kokul","Ramya","Vasan","Ansar","Thamarai","Vinoth"],
    "Math" : [45,34,56,76,76,45,78,67,56,98,34,67,86,43,87,98,75,84,39,84],
    "Science" : [76,45,67,87,78,73,56,78,98,45,90,87,56,75,45,92,94,63,71,65],
    "Python" : [78,67,56,98,34,67,86,43,87,98,75,84,39,84,34,56,76,76,45,78],
    "AI" : [90,87,56,75,45,92,94,63,71,65,76,45,67,87,78,73,56,78,98,45]
}

df = pd.DataFrame(data)
print(df.shape)
print(df.head(5))

subjects = ["Math", "Science", "Python", "AI"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)
print(df[["Student_Name", "Total", "Average"]].head(5))


plt.figure(figsize=(12, 6))
plt.plot(df["Student_Name"], df["Total"], label = "Total Marks")
plt.title("Student Total Marks")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.legend()
plt.tight_layout()
plt.show()


plt.figure(figsize= (12,6))
plt.bar(df["Student_Name"], df["Average"], label="Average Marks")
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.legend()
plt.tight_layout()
plt.show()

def get_grade(average):
    if average >= 75:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(get_grade)
print(df[["Student_Name", "Average", "Grade"]].head(5))

grade_counts = df["Grade"].value_counts()
print(grade_counts)


plt.figure(figsize=(7, 7))
plt.pie(
    grade_counts.values,
    labels=grade_counts.index,
    autopct="%1.1f%%"
)
plt.title("Student Grade Distribution")
plt.legend(title="Grades")
plt.tight_layout()
plt.show()

top_5_students = df.sort_values(by="Total", ascending=False).head(5)
print(top_5_students[["Student_Name", "Total", "Average"]])

plt.figure(figsize=(8, 5))
plt.bar(
    top_5_students["Student_Name"],
    top_5_students["Total"],
    label="Total Marks"
)
plt.title("Top 5 Students by Total Marks")
plt.xlabel("Students")
plt.ylabel("Total Marks (out of 400)")
plt.legend()
plt.tight_layout()
plt.show()