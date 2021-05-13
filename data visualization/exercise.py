'''15-1'''
import matplotlib.pyplot as plt

x_values = [i for i in range(1,6)]
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, s=100)
ax.set_title('cube', fontsize=24)
ax.set_xlabel('value', fontsize=14)
ax.set_ylabel('the cube of value', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

'''15-2'''
import matplotlib.pyplot as plt

x_values = [i for i in range(1,50001)]
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
ax.set_title('cube', fontsize=24)
ax.set_xlabel('value', fontsize=14)
ax.set_ylabel('the cube of value', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()