import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'JavaScript']
values = [40, 25, 20, 15]

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Programming Language Usage")
plt.show()