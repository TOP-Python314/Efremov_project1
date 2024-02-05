import random as r, test
""" Запускает легкого бота """
def easy_bot() -> int:
    return r.choice(list(set(range(9)) - set(test.moves_made)))

""" Запускает нормального бота """
def normal_bot():
    pass
    
""" Запускает сложного бота """
def hard_bot():
    pass

def func():
    pass