import copy


PLAYER_X = "X"
PLAYER_O = "O"


def is_free_to_mark(board, movement):
    columna,fila = movement
    if(board[fila][columna] is None):
        return True
    return False


def players(board):
    contador = 0
    for fila in board:
        for columna in fila:
            if columna is not None:
                contador += 1
    return PLAYER_O if contador % 2 == 1 else PLAYER_X




def actions(board):
    resultado = []
    filas = len(board)
    columnas = len(board[0])
    for i in range(filas):
        for j in range(columnas):
            if board[i][j] is None:
                tupla = (i, j)
                resultado += [tupla]
    return resultado


def result(board, action):
    jugador = players(board)
    x, y = action
    newBoard = copy.deepcopy(board)
    newBoard[y][x] = jugador
    return newBoard
    


def terminal(board):
    resultado = False
    filas = len(board)
    columnas = len(board[0])
    for i in range(filas):
        for j in range(columnas):
            if len(set(board[i])) <= 1:
                return  True
    conjunto = []
    isEqual = False
    for i in range(columnas):
        for j in range(filas):
            conjunto += [board[j][i]]
        if len(set(conjunto)) <= 1:
            return True
    

    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]

    if len(set(diagonal1)) <= 1:
        return True
    if len(set(diagonal2)) <= 1:
        return True
    
    return True if actions(board) == [] else False
        
     
    
def utility(board):
    resultado = False
    filas = len(board)
    columnas = len(board[0])
    for i in range(filas):
        for j in range(columnas):
            if len(set(board[i])) <= 1:
                return 1 if board[i][j] == PLAYER_X else -1
    conjunto = []
    isEqual = False
    for i in range(columnas):
        for j in range(filas):
            conjunto += [board[j][i]]
        if len(set(conjunto)) <= 1:
            return 1 if conjunto [0][0] == PLAYER_X else -1
    

    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]

    if len(set(diagonal1)) <= 1:
        return 1 if diagonal1[0] == PLAYER_X else -1
    if len(set(diagonal2)) <= 1:
        return 1 if diagonal2[0] == PLAYER_X else -1
    return 0
        
    """
    Final numeric value for terminal state s
    """
