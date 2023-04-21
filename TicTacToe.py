# Hansi Seitaj
# CMPSC 442
# Project 1
# Tic Tac Toe using Minimax Algorithm & Alpha Beta Pruning Algorithm

# The time module to measure the time of evaluating the game tree in every move
import time

# Implementation of a Tic Tac Toe game
class Game:
    def __init__(self):
        self.build_game()

    def build_game(self, board=None):
        self.current_state = board if board else [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # Player X always plays first
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print(" {} ".format(self.current_state[i][j]), end=" ")
            print()
        print()

    # Determines if the made move is a legal move
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    # Checks if the game has ended and returns the winner in each case
    def is_end(self):
        # Vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                    self.current_state[0][i] == self.current_state[1][i] and
                    self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (self.current_state[0][0] != '.' and
                self.current_state[0][0] == self.current_state[1][1] and
                self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # Second diagonal win
        if (self.current_state[0][2] != '.' and
                self.current_state[0][2] == self.current_state[1][1] and
                self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # Loop to check if the board is full
        for i in range(0, 3):
            for j in range(0, 3):
                # Otherwise there is an empty field so we continue the game
                if (self.current_state[i][j] == '.'):
                    return None

        # It's a tie!
        return '.'

    # Player 'O' is max, in this case AI
    def Max(self):

        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # Initially setting it to -2 as worse than the worst case:
        maxValue = -2

        px = None
        py = None

        result = self.is_end()

        # If the game came to an end, the function needs to return
        # the evaluation function of the end.
        # That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    # On the empty field player 'O' makes a move and calls Min
                    # That's one branch of the game tree.
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.Min()
                    # Fixing the maxv value if needed
                    if m > maxValue:
                        maxValue = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '.'

        return (maxValue, px, py)

    # Player 'X' is min, in this case human/user
    def Min(self):

        # Possible values for minv are:
        # -1 - win
        # 0  - a tie
        # 1  - loss

        # Initially setting it to 2 as worse than the worst case:
        minValue = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.Max()
                    if m < minValue:
                        minValue = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'

        return (minValue, qx, qy)

    def MaxAlphaBeta(self, alpha, beta):

        maxValue = -2
        px = None
        py = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    (m, min_i, in_j) = self.MinAlphaBeta(alpha, beta)
                    if m > maxValue:
                        maxValue = m
                        px = i
                        py = j
                    self.current_state[i][j] = '.'

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if maxValue >= beta:
                        return (maxValue, px, py)

                    if maxValue > alpha:
                        alpha = maxValue

        return (maxValue, px, py)

    def MinAlphaBeta(self, alpha, beta):

        minValue = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.MaxAlphaBeta(alpha, beta)
                    if m < minValue:
                        minValue = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'

                    if minValue <= alpha:
                        return (minValue, qx, qy)

                    if minValue < beta:
                        beta = minValue
        return (minValue, qx, qy)

    def PlayAlphaBeta(self):

        while True:
            self.draw_board()
            self.result = self.is_end()

            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '.':
                    print("It's a tie!")

                self.build_game()
                return

            if self.player_turn == 'X':
                while True:
                    start = time.time()
                    (m, qx, qy) = self.MinAlphaBeta(-2, 2)
                    end = time.time()
                    print("Evaluation time: {}s".format(round(end - start, 7)))
                    print("Recommended move: Row = {}, Column = {}".format(qx, qy))

                    px = int(input("Row: "))
                    py = int(input("Column: "))

                    qx = px
                    qy = py

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')

            else:
                (m, px, py) = self.MaxAlphaBeta(-2, 2)
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'

    def Play(self):

        while True:
            self.draw_board()
            self.result = self.is_end()

            # Printing the appropriate message if the game has ended
            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '.':
                    print("It is a tie!")

                self.build_game()
                return

            # If it's player's turn
            if self.player_turn == 'X':

                while True:
                    start = time.time()
                    (m, qx, qy) = self.Min()
                    end = time.time()
                    print("Evaluation time: {}s".format(round(end - start, 7)))
                    print("Recommended move: Row = {}, Column = {}".format(qx, qy))

                    px = int(input("Row: "))
                    py = int(input("Column: "))

                    (qx, qy) = (px, py)

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Please try again.')

            # If it is AI's turn
            else:
                (m, px, py) = self.Max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'


#Note: Uncomment the section to play accordingly.

# Pae 1
# Without a given board

print("Tic Tac Toe!\n")
#TicTacToe = Game()
#TicTacToe.PlayAlphaBeta()
#TicTacToe.Play()


# Part 2
# With a given board

myBoard = [['.','.','O'], ['X','O','O'], ['.','.','X']]
TicTacToe = Game()
TicTacToe.build_game(myBoard)
TicTacToe.PlayAlphaBeta()
#TicTacToe.Play()