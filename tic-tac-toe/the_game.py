from ending import win
import random,time

x1 = '\  / '
x2 = ' \/  '
x3 = ' /\  '
x4 = '/  \ '

h = '  | '

o1 = ' ___ '
o2 = '|   |'
o3 = '|   |'
o4 = '|___|'

v1 = '________|'
v2 = '__________|'
v3 = '________'

em = '     '

x = [x1,x2,x3,x4]
o = [o1,o2,o3,o4]
e1,e2,e3,e4,e5,e6,e7,e8,e9 = [em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em]

def grid() :
        print()
        print(e1[0], end=' '), print(h, end=' '), print(e2[0], end=' '), print(h, end=' '), print(e3[0])
        print(e1[1], end=' '), print(h, end=' '), print(e2[1], end=' '), print(h, end=' '), print(e3[1])
        print(e1[2], end=' '), print(h, end=' '), print(e2[2], end=' '), print(h, end=' '), print(e3[2])
        print(e1[3], end=' '), print(h, end=' '), print(e2[3], end=' '), print(h, end=' '), print(e3[3])

        print(v1, end=''), print(v2, end=''), print(v3)

        print(e4[0], end=' '), print(h, end=' '), print(e5[0], end=' '), print(h, end=' '), print(e6[0])
        print(e4[1], end=' '), print(h, end=' '), print(e5[1], end=' '), print(h, end=' '), print(e6[1])
        print(e4[2], end=' '), print(h, end=' '), print(e5[2], end=' '), print(h, end=' '), print(e6[2])
        print(e4[3], end=' '), print(h, end=' '), print(e5[3], end=' '), print(h, end=' '), print(e6[3])

        print(v1, end=''), print(v2, end=''), print(v3)

        print(e7[0], end=' '), print(h, end=' '), print(e8[0], end=' '), print(h, end=' '), print(e9[0])
        print(e7[1], end=' '), print(h, end=' '), print(e8[1], end=' '), print(h, end=' '), print(e9[1])
        print(e7[2], end=' '), print(h, end=' '), print(e8[2], end=' '), print(h, end=' '), print(e9[2])
        print(e7[3], end=' '), print(h, end=' '), print(e8[3], end=' '), print(h, end=' '), print(e9[3])
        print()

welcome = ''' 
    --------------------------------------
        type s to start the game
        type q to quit at any time
    --------------------------------------

    '''
welcome2 = '''
    --------------------------------------
      Welcome to tic-tac-toe in python !
     which gamemode do you want to play ?
         input s for single player
         input m for multiplayer
                  Enjoy
    --------------------------------------
'''
print(welcome2)
mode = input('>>')
true = False
true2 = False
true4 = True
played = 0
while true4 == True :
        if played == 0 :
                print(welcome)
                s = input('>>')
                if s != 's' :
                        continue
        l = [1,2,3,4,5,6,7,8,9]
        e1,e2,e3,e4,e5,e6,e7,e8,e9 = [em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em]
        print('which symbol do you want ? ')
        grid()
        turn = 1
        moves = 0
        player1 = input('X or O : ')
        if player1 == 'x':
                player1 = x
                player2 = o
        elif player1 == 'o':
                player1 = o
                player2 = x
        elif player1 == 'q' :
                break
        else :
                continue
        player = 1
        for i in range(9) :
                print('Available moves :')
                print(l)
                if player == 1 :
                        p = input('Player 1 : ')
                        player_ = player1
                elif player == 2 :
                        if mode == 's' :
                                p = str(random.choice(l))
                        elif mode == 'm' :
                                p = input('Player 2 : ')
                        player_ = player2
                moves += 1
                if p == '1' :
                        e1 = player_
                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                        l.remove(int(p))
                elif p == '2' :
                        e2 = player_
                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                        l.remove(int(p))
                elif p == '3' :
                        e3 = player_
                        l.remove(int(p))
                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                elif p == '4' :
                        e4 = player_
                        l.remove(int(p))
                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                elif p == '5' :
                        e5 = player_
                        l.remove(int(p))
                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                elif p == '6' :
                        e6 = player_
                        l.remove(int(p))
                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                elif p == '7' :
                        e7 = player_
                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                        l.remove(int(p))
                elif p == '8' :
                        e8 = player_
                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                        l.remove(int(p))
                elif p == '9' :
                        e9 = player_
                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                        l.remove(int(p))
                elif p == 'q' :
                        true2 = True
                        break
                else :
                        print('Enter something valid')
                        continue
                print()
                grid()
                turn += 1
                if true is True :
                        print('Player ',player,' WINS !!!')
                        played += 1
                        print()
                        print()
                        print()
                        true3 = False
                        while true3 == False :
                                print('Play Again ? [y or n]')
                                y_n = input('>>')
                                if y_n == 'y' :
                                        true3 = True
                                elif y_n == 'n' :
                                        true2 = True
                                        true3 = True
                                        true4 = False
                                elif y_n == 'q' :
                                        true2 = True
                                        true3 = True
                                        true4 = False

                        else :
                                break
                elif moves == 9 :
                        print('Its a tie')
                        played += 1 
                        print()
                        print()
                        print()
                        true3 = False
                        while true3 == False :
                                print('Play Again ? [y or n]')
                                y_n = input('>>')
                                if y_n == 'y' :
                                        true3 = True
                                elif y_n == 'n' :
                                        true2 = True
                                        true3 = True
                                        true4 = False

                                elif y_n == '-q' :
                                        true2 = True
                                        true3 = True
                                        true4 = False
                        else :
                                break
                if player == 1 :
                        player = 2
                elif player == 2 :
                        player = 1

