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
if mode == 'm' :
        true = False
        true2 = False
        played = 0
        while True :
                if played == 0 :
                        print(welcome)
                        s = input('>>')
                        if s != '-s' :
                                continue
                l = [1,2,3,4,5,6,7,8,9]
                e1,e2,e3,e4,e5,e6,e7,e8,e9 = [em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em],[em,em,em,em]
                print('which symbol do you want ? ')
                grid()
                turn = 1
                player1 = input('X or O : ')
                if player1 == 'x':
                        player1 = x
                        player2 = o
                elif player1 == 'o':
                        player1 = o
                        player2 = x
                elif player1 == '-q' :
                        break
                else :
                        continue
                while True :
                        if turn == 1 :
                                print('Available moves :')
                                print(l)
                                p1 = input('Player 1 :')
                                if p1 == '1' :
                                        e1 = player1
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                        l.remove(int(p1))
                                elif p1 == '2' :
                                        e2 = player1
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                        l.remove(int(p1))
                                elif p1 == '3' :
                                        e3 = player1
                                        l.remove(int(p1))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p1 == '4' :
                                        e4 = player1
                                        l.remove(int(p1))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p1 == '5' :
                                        e5 = player1
                                        l.remove(int(p1))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p1 == '6' :
                                        e6 = player1
                                        l.remove(int(p1))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p1 == '7' :
                                        e7 = player1
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                        l.remove(int(p1))
                                elif p1 == '8' :
                                        e8 = player1
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                        l.remove(int(p1))
                                elif p1 == '9' :
                                        e9 = player1
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                        l.remove(int(p1))
                                elif p1 == '-q' :
                                        true2 = True
                                        break
                                else :
                                        print('Enter something valid')
                                        continue
                                print()
                                grid()
                                if true is True :
                                        print('Player 1 WINS !!!')
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
                                                elif y_n == '-q' :
                                                        true2 = True
                                                        true3 = True
                                        else :
                                                break
                        if turn == 2 :
                                print('Available moves :')
                                print(l)
                                p2 = input('Player 2 :')
                                if p2 == '1' :
                                        e1 = player2
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == '2':
                                        e2 = player2
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == '3' :
                                        e3 = player2
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == '4':
                                        e4 = player2
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == '5' :
                                        e5 = player2
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == '6' :
                                        e6 = player2
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == '7' :
                                        e7 = player2
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == '8' :
                                        e8 = player2
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == '9' :
                                        e9 = player2
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == '-q' :
                                        true2 = true
                                else :
                                        print('Enter something valid')
                                        continue
                                print()
                                grid()
                                if true is True :
                                        print('Player 2 WINS !!!')
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
                                                elif y_n == '-q' :
                                                        true2 = True
                                                        true3 = True
                                        else :
                                                break
                if true2 == True :
                        break

if mode == 's' :
        true = False
        true2 = False
        played = 0
        while True :
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
                player1 = input('X or O : ')
                if player1 == 'x':
                        player1 = x
                        ai = o
                elif player1 == 'o':
                        player1 = o
                        ai = x
                elif player1 == 'q' :
                        break
                else :
                        continue
                while True :
                        if turn == 1 :
                                print('Available moves :')
                                print(l)
                                p1 = input('Player 1 :')
                                if p1 == '1' :
                                        e1 = player1
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                        l.remove(int(p1))
                                elif p1 == '2' :
                                        e2 = player1
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                        l.remove(int(p1))
                                elif p1 == '3' :
                                        e3 = player1
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                        l.remove(int(p1))
                                elif p1 == '4' :
                                        e4 = player1
                                        l.remove(int(p1))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p1 == '5' :
                                        e5 = player1
                                        l.remove(int(p1))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p1 == '6' :
                                        e6 = player1
                                        l.remove(int(p1))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p1 == '7' :
                                        e7 = player1
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                        l.remove(int(p1))
                                elif p1 == '8' :
                                        e8 = player1
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                        l.remove(int(p1))
                                elif p1 == '9' :
                                        e9 = player1
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                        l.remove(int(p1))
                                elif p1 == 'q' :
                                        true2 = True
                                        break
                                else :
                                        print('Enter something valid')
                                        continue
                                grid()
                                if true is True :
                                        print('Player 1 WINS !!!')
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
                                                elif y_n == '-q' :
                                                        true2 = True
                                                        true3 = True
                                        else :
                                                break
                                turn += 1
                        elif turn == 2 :
                                time.sleep(0.5)
                                p2 = random.choice(l)
                                if p2 == 1 :
                                        e1 = ai
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == 2:
                                        e2 = ai
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == 3 :
                                        e3 = ai
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == 4:
                                        e4 = ai
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == 5 :
                                        e5 = ai
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == 6 :
                                        e6 = ai
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == 7 :
                                        e7 = ai
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == 8 :
                                        e8 = ai
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                elif p2 == 9 :
                                        e9 = ai
                                        l.remove(int(p2))
                                        true = win(x, o, e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                grid()
                                if true is True :
                                        print('ai WINS !!!')
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
                                                elif y_n == 'q' :
                                                        true2 = True
                                                        true3 = True
                                        else :
                                                break
                                turn = turn - 1

                if true2 == True :
                        break
