import draw, test

""" Запускает игровой процес """
def Game():
    all_cells = 9
    board = [' ']*all_cells
    
    turn = 0
    name1 = []
    name2 = []
      
    flag = False
    while flag == False:
        print(draw.field_template.format(*board))
        if turn == 0:
            step = test.step_test()
            test.moves_made.append(step)
            name1.append(step)
            board[step] = 'X'
            turn = 1
            flag = test.win_test(name1)
        else:
            step = test.step_test()
            test.moves_made.append(step)
            name2.append(step)
            board[step] = 'O'
            turn = 0
            flag = test.win_test(name2)
    print(draw.field_template.format(*board))

""" Запускает легкого бота """
info = f'Чтобы поставить токен в нужную ячейку, введите номер клетки. Нумерация клеток от 1 до 9\n\n{draw.field_template}\n'

def easy_bot():
    print('Легкий бот запущен\n')
    print(info)
    
""" Запускает нормального бота """
def normal_bot():
    print('Нормальный бот запущен\n')
    print(info)
    
""" Запускает сложного бота """
def hard_bot():
    print('Сложный бот запущен\n')
    print(info)
    
""" Запуск режима одиночной игры """
def solo_play(name):
    lvl_bot = input('Выберите уровень сложности -> easy/normal/hard: ')
    if lvl_bot == 'easy':
        easy_bot()
    elif lvl_bot == 'normal':
        normal_bot()
    else:
        hard_bot()
    print('solo игра начата\n')

""" Запуск режима кооперативной игры """    
def coop_play(name1):
    print('coop игра начата\n')
    name2 = ('Введите имя второго игрока: ')

""" Запускает игру """    
def start_play(name):
    print(f'Погнали, {name}!\n')
    players_select = input('Хотите играть один или с другом? solo/coop: ')
    if players_select == 'solo':
        solo_play(name)
    else:
        coop_play(name)