
def show_field(f):
    num = '  0 1 2'
    print('\033[32m' + num + '\033[0m')
    for i in range(len(f)):
        print('\033[32m' + str(i) + '\033[0m' + ' ' + ' '.join(f[i]))


def users_input(f, user):
    while True:
        place = input(f"Ходит игрок {user} . Введите свои координаты: ").split()
        if len(place) != 2:
            print('Введите, пожалуйста две координаты: ')
            continue

        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числовые значения координат: ')
            continue

        x, y = map(int, place)
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Вы вышли за диапазон игрового поля')
            continue

        if f[x][y] != '_':
            if user is f[x][y]:
                print('Клетка уже занята Вами')
            else:
                print('Клетка уже занята другим игроком')
            show_field(field)
            continue

        break
    return x, y


def win_position(f, user):
    win_cord = (((0, 0), (0, 1), (0, 2)),   # 3 строки
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),   # 3 столбца
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)),
                ((0, 2), (1, 1), (2, 0)),  # диагональ /
                ((0, 0), (1, 1), (2, 2)))  # диагональ \

    for cord in win_cord:
        symbols = []
        for r in cord:
            symbols.append(f[r[0]][r[1]])
        if symbols == [user, user, user]:   # если символ одного игрока
            return True

    return False


def start(field):
    count = 0                   # счетчик ходов
    while True:
        show_field(field)
        if count % 2 == 0:      # смена игроков
            user = 'X'
        else:
            user = 'O'

        if count < 9:
            x, y = users_input(field, user)
            field[x][y] = user

        if count == 9:
            print('Победила ДРУЖБА, то есть ничья!')
            break

        if win_position(field, user):
            print(f"\033[1;31mПоздравляем, Вы выиграли {user} , вот Ваш результат!\033[0m")
            show_field(field)
            break

        count += 1

field = [['_'] * 3 for _ in range(3)]


start(field)