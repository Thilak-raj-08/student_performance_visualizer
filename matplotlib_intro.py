import matplotlib.pyplot as plt

days = [1,2,3,4,5]
marks = [50,60,55,75,85]

plt.figure(figsize=(8, 5))
plt.plot(days, marks, label="Test Marks")
plt.title("Student Progress")
plt.xlabel("Days")
plt.ylabel("Marks")
plt.legend()
plt.show()