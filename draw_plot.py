import matplotlib.pyplot as plt

acc = [95.80 , 99.62]
labels = ['before resize' , 'after resize']

plt.ylim(90,100)
plt.bar(labels , acc , 0.5 , align = 'center' , zorder = 20)
plt.grid(axis = 'y' , zorder = 10)
plt.title('Resize Augmentation Comparison')
plt.show()