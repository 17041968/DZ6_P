#Дано натуральное число N. Найдите значение выражения:N + NN + NNN
#N может быть любой длины.
N = input('Введите число ')
print(N)
print(N*2)
print(N*3)
print(int(N) + int(N*2) + int(N*3))