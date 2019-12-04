print("Введите количество элементов")

iter = int(input())

list_num = []

# функция которая получает пишет значения в массив
def get_data(count):
	for i in range(count):
		x = int(input())
		list_num.append(x)
get_data(iter)

def average(arr):
	sum = 0
	for i in range arr:
		sum += arr[i]
	return sum/len(arr)
print(average(list_num))





