
import matplotlib.pyplot as plt

print("введите название файла без расширения, который вы перенесли в эту папку")

fileName = input("ВИмя вашего файла: ")
fileName = fileName + ".txt"
f = open(fileName, "r");
file_content = f.read()
file_arr = file_content.split(',')

print(file_arr)
list_num = file_arr

# функция которая получает пишет значения в массив
for i in range(len(list_num)):
	list_num[i] = int(list_num[i])


N = len(list_num)

for i in range(N - 1):
	for j in range(N - i - 1):
		if list_num[j] > list_num[j + 1]:
			list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]
print(list_num)

def average(arr):
	sum = 0
	for i in range(len(list_num)):
		sum += arr[i]
	return sum/len(arr)
print(average(list_num))
print("и его медиана совсем несложная")
print(list_num[int(len(list_num)/2)])



plt.plot(list_num)
plt.ylabel('наш числовой ряд')
plt.show()
# https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

# и можно написать вывод моды
# и сделать запись в файле




