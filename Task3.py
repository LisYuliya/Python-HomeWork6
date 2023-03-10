# 2. Старший и младший
# Пользователь вводит число N.
# Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.

# # Ввод:
# >> 3 # Количество друзей
# >> Иван
# >> 11
# >> Саша
# >> 12
# >> Леша
# >> 10
# # Вывод:
# >> Леша

some_dict = {}
N = int(input('Введите количество друзей: '))
friends = []

while N > 0:
    name = input(f'Введите имя друга: ')
    age = int(input('Введите возраст друга: '))
    some_dict[name] = age
    N -= 1
    friends.append({'name': name, 'age': age})


print(f'Ваши друзья и их возраст: {friends}')

print(f'Имя младшего друга: {min(some_dict, key=some_dict.get)}')
