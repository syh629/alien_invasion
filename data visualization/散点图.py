import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [i**2 for i in x_values]


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)   #颜色映射

#设置图表标题并给坐标轴加上标签
ax.set_title('squares', fontsize = 24)
ax.set_xlabel('value', fontsize = 14)
ax.set_ylabel('square of value', fontsize = 14)

#设置刻度标记的大小
ax.tick_params(axis='both', which='both', labelsize = 14)

#设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight')  保存