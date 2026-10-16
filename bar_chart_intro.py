import matplotlib.pyplot as plt

students = ["Arun", "Nila","Kavin"]
marks = [85, 72, 91]

plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()