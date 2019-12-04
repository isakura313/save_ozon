print("введите название файла без расширения, который вы перенесли в эту папку")

fileName = input("Ваше число: ")
fileName = fileName + ".txt"
f = open(fileName, "r");
file_content = f.read()
file_arr = file_content.split(',')

print(file_arr)
list_num = file_arr

# функция которая получает пишет значения в массив
for i in range(len(list_num)):
	list_num[i] = int(list_num[i])


def average(arr):
	sum = 0
	for i in range(len(list_num)):
		sum += arr[i]
	return sum/len(arr)
print(average(list_num))





