import matplotlib.pyplot as plt




#итого, как у нас строится процесс вычислений?
# у нас есть формула, которая занимается подбором оптимального значения
# y = Ax + b
# b мы пока оставим, потому что пройдем через начало координат
#первым мы выбираем A = 0.25
#первая наша формула - ошибка = желаемое значение - фактический результат
# треугольник A - небольшое изменение, или learning scale
# t = (A + треугольник A) * X
# E = t - y
# t - y = (A + треугольникA)x - Ax
# E = небольшое значение  * x
# треугольник A = E/x
# треугольникA = L(E/x)
# итоговое значение  A = 1,4


A = 1.4
x_values = list(range(0, 10))
y_values = [x * A for x in x_values]


beatles = [3, 1]
gusen = [1, 3]
plt.style.use('seaborn-whitegrid')
plt.plot(beatles,  gusen, 'ro')
plt.axis([0, 5, 0, 5])
plt.xlabel('ширина')
plt.ylabel('высота')
plt.scatter(x_values, y_values, linewidth = 5)
plt.show()