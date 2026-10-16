import matplotlib.pyplot as plt

grades = ["A", "B", "C"]
counts = [10, 6, 4]

plt.pie(counts, labels=grades, autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.show()