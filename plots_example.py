import matplotlib.pyplot as plt

x = [x for x in range(100)]
y = [x for x in range(100)]
y_2 = [x * x for x in range(100)]
plt.plot(x, y, x, y_2)
plt.title("My plot")

plt.show()