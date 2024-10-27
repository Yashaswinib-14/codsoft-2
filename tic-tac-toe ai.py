import math

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if the game is won
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

# Function to check if the board is full
def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    if winner == 'O':
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    
    return best_move

# Main function to play against the AI
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    while True:
        print_board(board)
        if check_winner(board) or is_full(board):
            break

        # Human move
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move! Try again.")
            continue

        if check_winner(board) or is_full(board):
            break

        # AI move
        ai_move = find_best_move(board)
        if ai_move != (-1, -1):
            board[ai_move[0]][ai_move[1]] = 'X'

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie!")

# Run the game
play_game()