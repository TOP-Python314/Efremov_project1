wins = [
    {0, 1, 2},
    {3, 4, 5},
    {6, 7, 8},
    {0, 3, 6},
    {1, 4, 7},
    {2, 5, 8},
    {0, 4, 8},
    {2, 4, 6}
]
""" Создает список выйгрышных комбинаций """
def wins(cells: int) -> list:
    wins = []
    for i in range(cells):
        wins.append({*range(i*cells, (i+1)*cells)})
        wins.append({*range(i, cells**2, cells)})
    wins.append({*range(0, cells**2, cells+1)})
    wins.append({*range(cells-1, cells**2-1, cells-1)})
    return wins

moves_made = []   
""" Проверяет наличие выйгрышной комбинации """
def win_test(turn: int, cells) -> str | list:
    moves1 = [moves_made[i] for i in range(0, len(moves_made), 2)] # ходы для крестика   
    moves2 = [moves_made[i] for i in range(1, len(moves_made), 2)] # ходы для нолика
    vars_moves1 = list(filter(lambda x: len(x & set(moves2)) == 0, wins(cells))) # список оставшихся возможных комбинаций для крестика
    vars_moves2 = list(filter(lambda x: len(x & set(moves1)) == 0, wins(cells))) # для нолика
    if len(vars_moves1) == 0 and len(vars_moves2) == 0:
        game_end = input(f' Возможные комбинации побед закончились. Партия будет закончена в ничью. Хотите продолжить игру? да/нет ')
        if game_end == 'да':
            return 'xo'
    elif any(set(moves1)>=win for win in vars_moves1):
        return 0
        # победа крестика
    elif any(set(moves2)>=win for win in vars_moves2):
        return 1
        # победа нолика

""" Проверяет занята ячейка или нет """
def step_test() -> int:
    step = int(input(' Введите номер клетки: '))
    while True:
        if step in moves_made:
            step = int(input(' Данная клетка уже занята\n'))
        else:
            return step
            

   
    