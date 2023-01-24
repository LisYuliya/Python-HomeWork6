# Задачи для самостоятельного решения
# 1. Фрукты
# Пользователь вводит число K - количество фруктов.
# Затем он вводит K фруктов в формате: название фрукта и его количество.
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.
# Например:

# # Ввод:
# >> 3 # Количество фруктов
# >> Яблоко
# >> 3
# >> Апельсин
# >> 3
# >> Мандарин
# >> 10
# # Вывод:
# >> {'Яблоко': 3, 'Апельсин': 3, 'Мандарин': 10}


some_dict = {}
K = int(input('Введите количество фруктов: '))
count = 1

while K > 0:
    fruit = input(f'Введите название фрукта номер {count}: ')
    count_fruit = int(input('Введите количество фруктов: '))
    some_dict[fruit] = count_fruit
    K -= 1
    count += 1

print(f'Ваш список: {some_dict}')
