""" Первый проект """

import func, draw

print('Приветствую тебя в игре "Крестики и Нолики"')
name = input('Введите свое имя: ')
print(f'{name}, желаете начать игру?')

s = input('y/n -> ')
if s == 'y':    
    func.start_play(name)
else:
    print(f'До скорой встречи, {name}!')
    
        
        
