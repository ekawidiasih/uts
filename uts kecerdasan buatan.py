# Import library
import math

# Fungsi untuk menentukan pemenang
def evaluate(board):
    for row in board:
        if all([cell == 'X' for cell in row]):
            return 1
        elif all([cell == 'O' for cell in row]):
            return -1
    for col in range(3):
        if all([board[row][col] == 'X' for row in range(3)]):
            return 1
        elif all([board[row][col] == 'O' for row in range(3)]):
            return -1
    if all([board[i][i] == 'X' for i in range(3)]) or all([board[i][2 - i] == 'X' for i in range(3)]):
        return 1
    elif all([board[i][i] == 'O' for i in range(3)]) or all([board[i][2 - i] == 'O' for i in range(3)]):
        return -1
    return 0

# Fungsi minimax dengan alpha-beta pruning
def minimax(board, depth, is_maximizing_player, alpha, beta):
    score = evaluate(board)
    if score != 0:
        return score
    if depth == 0:
        return 0
    if is_maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    eval = minimax(board, depth - 1, False, alpha, beta)
                    board[i][j] = '-'
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    eval = minimax(board, depth - 1, True, alpha, beta)
                    board[i][j] = '-'
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Fungsi untuk membuat langkah terbaik
def best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                eval = minimax(board, 5, False, -math.inf, math.inf)
                board[i][j] = '-'
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Fungsi untuk menampilkan papan
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

# Inisialisasi papan
board = [['-' for _ in range(3)] for _ in range(3)]

# Main game loop
play_again = True
while play_again:
    board = [['-' for _ in range(3)] for _ in range(3)];
    
    while True:
   
        print_board(board)
        row, col = map(int, input("Masukkan baris dan kolom (0-2) pisahkan dengan spasi: ").split())
        if board[row][col] != '-':
            print("Sudah diisi. Pilih yang lain.")
            continue
        board[row][col] = 'O'
        if evaluate(board) == -1:
            print_board(board)
            print("Anda Menang!")
            break
        elif all([cell != '-' for row in board for cell in row]):
            print_board(board)
            print("Permainan Seri!")
            break
        print("Giliran komputer...")
        best_row, best_col = best_move(board)
        board[best_row][best_col] = 'X'
        if evaluate(board) == 1:
            print_board(board)
            print("Komputer Menang!")
            break
            
    play_again_input = input("Ingin bermain lagi? (ya/tidak): ")
    if play_again_input.lower() != 'ya':
        play_again = False
        break