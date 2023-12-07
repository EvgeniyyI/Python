import numpy as np
import matplotlib.pyplot as plt

x = 12.1
a = np.arange(-5, 12, 0.5)
args = []
func_values = []

for i in a:
    value = np.exp(i * x) - 3.45 * i
    args.append(x)
    func_values.append(value)

args = np.array(args)
func_values = np.array(func_values)
print("Значения аргумента:\n", args)
print("Значения функции:\n", func_values)

max_value = func_values.max()
min_value = func_values.min()
average = func_values.mean()
size = func_values.size

print("Наибольший элемент:", max_value)
print("Наименьший элемент:", min_value)
print("Среднее занчение:", average)
print("Количество элементов:", size)

print(np.sort(func_values))

plt.plot(a,func_values,'o-', label = 'f(x)')
plt.axhline(average,color='r', linestyle = '--', label='mean')

plt.xlabel('a')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.title('change f(x)')
plt.show()