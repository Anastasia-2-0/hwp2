# ; Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# ; Найдите произведение элементов на указанных позициях. Позиции хранятся в файле 
# ; file.txt в одной строке одно число.
import random
n = int(input("Введите число:"))
my_list = []

for i in range(n):
    my_list.append(random.randint(-n, n))
print(my_list)

poz1 = random.randint(0,n)
poz2 = random.randint(0,n)
print(f'позиция 1 равна {poz1}')
print(f'позиция 2 равна {poz2}')

if poz1 == poz2: 
    # проверяю,чтобы позиции не были равны
    print(f'произведения чисел не может быть, потому что позиции равны')
else:
    proizvesenie = my_list[poz1] * my_list[poz2]
    print(f'произведение чисел на указанных позициях {proizvesenie}')
