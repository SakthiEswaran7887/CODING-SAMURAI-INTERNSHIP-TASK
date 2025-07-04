import math

# Initialize board
board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('-'*5)

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)

def is_full():
    return all(cell != ' ' for cell in board)

def minimax(depth, is_maximizing):
    if check_winner('O'): return 1
    if check_winner('X'): return -1
    if is_full(): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

def play_game():
    print("You are X. AI is O.")
    print_board()

    while True:
        # Player Move
        try:
            move = int(input("Choose your move (1-9): ")) - 1
            if board[move] != ' ':
                print("Invalid move, try again.")
                continue
        except:
            print("Enter a valid number.")
            continue

        board[move] = 'X'
        print_board()
        if check_winner('X'):
            print("You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        # AI Move
        ai_move()
        print("\nAI played:")
        print_board()
        if check_winner('O'):
            print("AI wins!")
            break
        if is_full():
            print("It's a draw!")
            break

play_game()
 