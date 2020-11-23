# рисую поле
s00 = "     0    1    2\n"
s0 = "0    -    -    -\n"
s1 = "1    -    -    -\n"
s2 = "2    -    -    -\n"
field = [s00, s0, s1, s2]


def print_field():
    print(field[0])
    print(field[1])
    print(field[2])
    print(field[3])


# пересчет введенных координат
def ent():
    hod = input("введите номер строки и номер столбца без пробела: ")
    if ((int(hod[0]) < 0) or (int(hod[0]) > 2)) or ((int(hod[1]) < 0) or (int(hod[1]) > 2)):
        print("введены некорректные координаты")
        ent()
    else:
        y = int(hod[0]) + 1
    if int(hod[1]) == 0:
        x = 6
    elif int(hod[1]) == 1:
        x = 11
    else:
        x = 16
    if field[y][x-1:x] == "x" or field[y][x-1:x] == "o":
        print("данная позиция занята")
        hod = input("введите номер строки и номер столбца без пробела: ")
        if ((int(hod[0]) < 0) or (int(hod[0]) > 2)) or ((int(hod[1]) < 0) or (int(hod[1]) > 2)):
            print("введены некорректные координаты")
            ent()
        else:
            y = int(hod[0]) + 1
            x = 0
        if int(hod[1]) == 0:
            x = 6
        elif int(hod[1]) == 1:
            x = 11
        else:
            x = 16

    return [y, x]


# реализация хода первого игрока
def hod_1():
    print("ход первого игрока")
    y, x = ent()
    field[y] = field[y][:x - 1] + 'x' + field[y][x:]
    print_field()


# реализация хода второго игрока
def hod_2():
    print("ход второго игрока")
    y, x = ent()
    field[y] = field[y][:x - 1] + 'o' + field[y][x:]
    print_field()


# детектор победы\проигрыша
def detekt_win():
    if all([field[1][5:6] == "x",
            field[1][10:11] == "x",
            field[1][15:16] == "x"]):
        return 1
    if all([field[2][5:6] == "x",
            field[2][10:11] == "x",
            field[2][15:16] == "x"]):
        return 1
    if all([field[3][5:6] == "x",
            field[3][10:11] == "x",
            field[3][15:16] == "x"]):
        return 1
    if all([field[1][5:6] == "x",
            field[2][5:6] == "x",
            field[3][5:6] == "x"]):
        return 1
    if all([field[1][10:11] == "x",
            field[2][10:11] == "x",
            field[3][10:11] == "x"]):
        return 1
    if all([field[1][15:16] == "x",
            field[2][15:16] == "x",
            field[3][15:16] == "x"]):
        return 1
    if all([field[1][15:16] == "x",
            field[2][10:11] == "x",
            field[3][5:6] == "x"]):
        return 1
    if all([field[1][5:6] == "x",
            field[2][10:11] == "x",
            field[3][15:16] == "x"]):
        return 1

    if all([field[1][5:6] == "o",
            field[1][10:11] == "o",
            field[1][15:16] == "o"]):
        return 1
    if all([field[2][5:6] == "o",
            field[2][10:11] == "o",
            field[2][15:16] == "o"]):
        return 1
    if all([field[3][5:6] == "o",
            field[3][10:11] == "o",
            field[3][15:16] == "o"]):
        return 1
    if all([field[1][5:6] == "o",
            field[2][5:6] == "o",
            field[3][5:6] == "o"]):
        return 1
    if all([field[1][10:11] == "o",
            field[2][10:11] == "o",
            field[3][10:11] == "o"]):
        return 1
    if all([field[1][15:16] == "o",
            field[2][15:16] == "o",
            field[3][15:16] == "o"]):
        return 1
    if all([field[1][15:16] == "o",
            field[2][10:11] == "o",
            field[3][5:6] == "o"]):
        return 1
    if all([field[1][5:6] == "o",
            field[2][10:11] == "o",
            field[3][15:16] == "o"]):
        return 1


# реализация игры
def play():
    count_draw = 0
    while True:
        hod_1()
        if detekt_win() == 1:
            print("первый игрок победил")
            break
        if count_draw == 4:
            print("ничья")
            break
        hod_2()
        if detekt_win() == 1:
            print('второй игрок победил')
            break
        count_draw += 1


print_field()
play()
