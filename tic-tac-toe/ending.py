def game():
    return print('Still in development \n Coming soon!!!')


'''
print('which symbol do you want ? ')
player1 = input('X or O : ')
if player1 == 'x':
    player1 = x
    player2 = o
elif player1 == 'o':
    player1 = o
    player2 = x

while True:
    p1 = input('Player 1 :')
    if p1 == 1:
        e1 = player1
    if p1 == 2:
        e2 = player1
    if p1 == 3:
        e3 = player1
    if p1 == 4:
        e4 = player1
    if p1 == 5:
        e5 = player1
    if p1 == 6:
        e6 = player1
    if p1 == 7:
        e7 = player1
    if p1 == 8:
        e8 = player1
    if p1 == 9:
        e9 = player1
    win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
'''


def win1(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9):
    if e1 == e5:
        if e1 == e9:
            if e1 == x:
                print('player 1 wins')
                return True
            elif e1 == o:
                print('player 2 wins')
                return True
    elif e1 == e4:
        if e1 == e7:
            if e1 == x:
                print('player 1 wins')
                return True
            elif e1 == o:
                print('player 2 wins')
                return True
    elif e1 == e2:
        if e1 == e3:
            if e1 == x:
                print('player 1 wins')
                return True
            elif e1 == o:
                print('player 2 wins')
                return True
    elif e2 == e5:
        if e2 == e8:
            if e2 == x:
                print('player 1 wins')
                return True
            elif e2 == o:
                print('player 2 wins')
                return True
    elif e3 == e6:
        if e3 == e9:
            if e3 == x:
                print('player 1 wins')
                return True
            elif e3 == o:
                print('player 2 wins')
                return True
    elif e3 == e5:
        if e3 == e7:
            if e3 == x:
                print('player 1 wins')
                return True
            elif e3 == o:
                print('player 2 wins')
                return True
    elif e4 == e5:
        if e4 == e6:
            if e4 == x:
                print('player 1 wins')
                return True
            elif e4 == o:
                print('player 2 wins')
                return True
    elif e7 == e8:
        if e7 == e9:
            if e7 == x:
                print('player 1 wins')
                return True
            elif e7 == o:
                print('player 2 wins')
                return True


def win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9):
    if e1 == e2 == e3:  # 1
        if e1 == x:
            return True
        elif e1 == o:
            return True
    if e4 == e5 == e6:  # 2
        if e4 == x:
            return True
        elif e4 == o:
            return True
    if e7 == e8 == e9:  # 3
        if e7 == x:
            return True
        elif e7 == o:
            return True
    if e1 == e4 == e7:  # 4
        if e1 == x:
            return True
        elif e1 == o:
            return True
    if e2 == e5 == e8:  # 5
        if e2 == x:
            return True
        elif e2 == o:
            return True
    if e3 == e6 == e9:  # 6
        if e3 == x:
            return True
        elif e3 == o:
            return True
    if e1 == e5 == e9:  # 7
        if e1 == x:
            return True
        elif e1 == o:
            return True
    if e3 == e5 == e7:  # 8
        if e3 == x:
            return True
        elif e3 == o:
            return True


'''
e1 = x
e2 = o
e3 = o
e4 = x
e5 = x
e6 = o
e7 = x
e8 = x
e9 = o
'''
