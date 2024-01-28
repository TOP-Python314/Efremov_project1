def func():
    pass

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
moves_made = []

def win_test(name):
    return any(set(name)>=win for win in wins)
    
""" Проверяет занята ячейка или нет """
def step_test():
    step = int(input())
    while True:
        if step in moves_made:
            step = int(input('Данная клетка уже занята\n'))
        else:
            return step
    
    
    