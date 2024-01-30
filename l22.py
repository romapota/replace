import itertools as it
import time
n: int;
l: int;
k: int;
count: int;
summ: int
dangers_places: list;
places: list;
new_file: list;
dangers_places_double: list;
places_double: list;
free_place: list;
save_in_file: list
def check_in(first, second):
    for s in first:
        if list(s) in second:
            return False
            break
        else:
            return True
def dangers_places_def(n:int, placess:list, c:int)-> list:  # поиск опасных "координат", переменная отвечает за добавление найденных опасных ходов в общий список. Если с = 1, то будут добавлены, если с = 0 - нет
    # везде есть проверка на то, чтобы значения были в пределах доски
    danger = []
    if c == 1:
        for i in placess:
            # опасные места по горизонтальной линии
            for x in range(0, n + 1):
                danger.append([x, i[1]])
            # опасные места по вертикали
            for y in range(0, n + 1):
                danger.append([i[0], y])
            # опасные места по главной диагонали
            for j in range(1, n + 1):
                danger.append([i[0] + j, i[1] + j])
            if i[0] != 0 and i[1] != 0:
                if i[0] < i[1]:
                    minn = i[0]
                else:
                    minn = i[1]
                for j in range(minn, 0, -1):
                    danger.append([i[0] - j, i[1] - j])
            # опасные места по побочной диагонали
            if i[1] != 0:
                if i[0] < i[1]:
                    minn = i[0]
                else:
                    minn = i[1]
                for j in range(1, minn + 1):
                    if i[1] - j >= 0:
                        danger.append([i[0] + j, i[1] - j])
            if i[0] != 0:
                if i[0] > i[1]:
                    minn = i[0]
                else:
                    minn = i[1]
                for j in range(0, minn + 1):
                    if i[0] - j >= 0:
                        danger.append([i[0] - j, i[1] + j])
            # опасные места, конь
            if i[0] + 2 <= n and i[1] + 1 <= n:
                danger.append([i[0] + 2, i[1] + 1])
            if i[0] + 1 <= n and i[1] + 2 <= n:
                danger.append([i[0] + 1, i[1] + 2])
            if i[0] - 2 >= 0 and i[1] - 1 >= 0:
                danger.append([i[0] - 2, i[1] - 1])
            if i[0] - 1 >= 0 and i[1] - 2 >= 0:
                danger.append([i[0] - 1, i[1] - 2])
            if i[0] + 1 >= 0 and i[1] - 2 >= 0:
                danger.append([i[0] + 1, i[1] - 2])
            if i[0] + 2 >= 0 and i[1] - 1 >= 0:
                danger.append([i[0] + 2, i[1] - 1])
            if i[0] - 1 >= 0 and i[1] + 2 >= 0:
                danger.append([i[0] - 1, i[1] + 2])
            if i[0] - 2 >= 0 and i[1] + 1 >= 0:
                danger.append([i[0] - 2, i[1] + 1])
    else:
        i = placess
        list(i)
        danger = []
        # опасные места по горизонтальной линии
        for x in range(0, n + 1):
            danger.append([x, i[1]])
        # опасные места по вертикали
        for y in range(0, n + 1):
            danger.append([i[0], y])
        # опасные места по главной диагонали
        for j in range(1, n + 1):
            danger.append([i[0] + j, i[1] + j])
        if i[0] != 0 and i[1] != 0:
            if i[0] < i[1]:
                    minn = i[0]
            else:
                minn = i[1]
            for j in range(minn, 0, -1):
                danger.append([i[0] - j, i[1] - j])
        # опасные места по побочной диагонали
        if i[1] != 0:
            if i[0] < i[1]:
                minn = i[0]
            else:
                minn = i[1]
            for j in range(1, minn + 1):
                if i[1] - j >= 0:
                    danger.append([i[0] + j, i[1] - j])
        if i[0] != 0:
            if i[0] > i[1]:
                minn = i[0]
            else:
                minn = i[1]
            for j in range(0, minn + 1):
                if i[0] - j >= 0:
                    danger.append([i[0] - j, i[1] + j])
        # опасные места, конь
        if i[0] + 2 <= n and i[1] + 1 <= n:
            danger.append([i[0] + 2, i[1] + 1])
        if i[0] + 1 <= n and i[1] + 2 <= n:
                danger.append([i[0] + 1, i[1] + 2])
        if i[0] - 2 >= 0 and i[1] - 1 >= 0:
                danger.append([i[0] - 2, i[1] - 1])
        if i[0] - 1 >= 0 and i[1] - 2 >= 0:
                danger.append([i[0] - 1, i[1] - 2])
        if i[0] + 1 >= 0 and i[1] - 2 >= 0:
                danger.append([i[0] + 1, i[1] - 2])
        if i[0] + 2 >= 0 and i[1] - 1 >= 0:
                danger.append([i[0] + 2, i[1] - 1])
        if i[0] - 1 >= 0 and i[1] + 2 >= 0:
                danger.append([i[0] - 1, i[1] + 2])
        if i[0] - 2 >= 0 and i[1] + 1 >= 0:
                danger.append([i[0] - 2, i[1] + 1])
    for x in places:
        danger.append(x)
    return danger
def free_place():
    global n, dangers_places
    free = []
    for x in range(n):
        for y in range(n):
            if [x, y] not in dangers_places:
                free.append([x, y])
    for x in places:
        free.append(x)
    return free

def search(combin):
    global places, new_file
    check = True
    place = [i for i in places]
    for option in combin:
        check = True
        for option_one in option:
            if option_one not in dangers_places_def(n, place, 1) and check_in(place, dangers_places_def(n, option_one, 0)):
                place.append(tuple(option_one))
            else:
                place = [i for i in places]
                check = False
                break
        if check:
            new_file.writelines(f'{m} ' for m in place)
            new_file.writelines('\n')
        place = [i for i in places]
def get_data() -> int:
    with open(f'input.txt', 'r', encoding='utf-8') as file:
        n, l, k = map(int, file.readline().split())
        places = []
        for _ in range(k):
            a = tuple(map(int, file.readline().split()))
            places.append(a)
        return n, l, k, places
def main():
    start_time = time.time()
    global dangers_places, places, n, k, new_file, dangers_places_double, places_double, l, free_place, save_in_file, first, places_for_print
    n, l, k, places = get_data()
    summ = 0
    first = False
    save_in_file = []
    dangers_places = dangers_places_def(n, places, 1)
    free_place = free_place()
    combinations = list(it.combinations(free_place, l))
    print(combinations)
    new_file = open('output.txt', 'w+')
    search(combinations)
    new_file.close()
    end_time = time.time()
    print('Time: ', end_time - start_time)

if __name__ == '__main__':
    main()

