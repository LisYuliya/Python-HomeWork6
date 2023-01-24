# 3. Еще немного о друзьях
# Пользователь вводит число N.
# Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя.

# # Ввод:
# >> 3 # Количество друзей
# >> Иван
# >> 12
# >> Иннокентий
# >> 20
# >> Леша
# >> 10
# # Вывод:
# >> 14
# >> Иннокентий

some_dict = {}
N = int(input('Введите количество друзей: '))
friends = []

while N > 0:
    name = input(f'Введите имя друга: ')
    age = int(input('Введите возраст друга: '))
    some_dict[name] = age
    N -= 1
    friends.append({'name': name, 'age': age})


def average(some_dict):
    summ = 0
    count = 0
    for value in some_dict.values():
        summ += value
        count += 1
    return summ/count


keys = list(some_dict.keys())

print(f'Самое длинное имя: {max(keys, key=len)}')
print(f'Средний возраст ваших друзей: {average(some_dict)}')


