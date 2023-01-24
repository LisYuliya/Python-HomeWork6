# Создайте список из случайных чисел. Найдите количество различных элементов в нем.
import random


some_list = [random.randint(0, 10) for _ in range(10)]
new_list = []
count = 0
print(f'Список: {some_list}')
for i in some_list:
    if not i in new_list:
        new_list.append(i)
        i += 1
        count += 1

print(f'Количество различных элементов в списке: {count}')
