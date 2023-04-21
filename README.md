# TicTacToe-AI

In this project, I have created an AI that is capable of playing the game of Tic Tac Toe. I have used the Minimax algorithm with Alpha-Beta pruning to do so. 

First, I created a class that represents our Tic Tac Toe board. This class has few methods that will be used to check the game state, make moves, check for legal moves, allow the user to play with AI. 

Furthermore, the game state can be one of three things: 'X', 'O', or 'tie'. 

If 'X' is displayed, that means that player 'X' has won the game.

If 'O' is displayed, that means that player 'O' has won the game. 

If ‘tie’ is displayed, that means that the game has ended in a draw

Comparison Table

| Algorithm         | Minimum time | Maximum time |
| ----------------- | ------------ | ------------ |
| Minimax           | 3.14s        | 3.68s        |
| Alpha-beta pruning| 0.12s        | 0.13s        |
