# 4.7.2.1 PROYECTO: TIC-TAC-TOE
''' Nombre: Luis Alberto Romero Gómez
    Descripcion: Usar las propias funciones
    Fecha: 01 de octubre
'''
from random import randrange

def DisplayBoard(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def EnterMove(board):
    move = int(input("Ingresa tu movimiento: "))
    for i in range(3):
        for j in range(3):
            if board[i][j] == move:
                board[i][j] = 'O'
                return

def MakeListOfFreeFields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):
                free_fields.append((i, j))
    return free_fields

def VictoryFor(board, sign):
    for row in board:
        if row.count(sign) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def DrawMove(board):
    free_fields = MakeListOfFreeFields(board)
    move = randrange(len(free_fields))
    i, j = free_fields[move]
    board[i][j] = 'X'

# Inicializamos el tablero
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

# Ciclo del juego
while True:
    DisplayBoard(board)
    EnterMove(board)
    if VictoryFor(board, 'O'):
        DisplayBoard(board)
        print("¡Has Ganado!")
        break
    DrawMove(board)
    if VictoryFor(board, 'X'):
        DisplayBoard(board)
        print("La máquina ha ganado.")
        break
    if len(MakeListOfFreeFields(board)) == 0:
        DisplayBoard(board)
        print("Es un empate.")
        break