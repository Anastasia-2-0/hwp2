# ; Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# ; Пример:

# ; - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('n = '))
my_list = []
for i in range(1, n+1):
    my_list.append([i, round(pow(1 + (1/i),i), 2)])
print(dict(my_list))

sum = 0
for i in range(1, n + 1):
    sum += (1 + 1 / i) ** i
print(f'Сумма последовательности равна {round(sum,2)}')