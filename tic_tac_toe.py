import random

# Function to print the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Check if the player has won
def check_win(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

# Check if the board is full (no moves left)
def is_full(board):
    return ' ' not in board

# AI function that makes a move
def ai_move(board):
    # Try to win or block the player
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'  # AI is 'O'
            if check_win(board, 'O'):
                return i
            board[i] = ' '  # Undo move

    # Block player from winning
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'  # Player is 'X'
            if check_win(board, 'X'):
                board[i] = 'O'
                return i
            board[i] = ' '  # Undo move

    # Otherwise, choose a random empty spot
    return random.choice([i for i in range(9) if board[i] == ' '])

# Main game loop
def main():
    board = [' '] * 9
    print("Tic-Tac-Toe: You are 'X' and the AI is 'O'")
    print_board(board)

    while True:
        # Player's move
        try:
            player_move = int(input("Enter your move (1-9): ")) - 1
            if board[player_move] != ' ':
                print("Invalid move, try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")
            continue

        board[player_move] = 'X'
        print_board(board)

        if check_win(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI's move
        print("AI's move:")
        ai_position = ai_move(board)
        board[ai_position] = 'O'
        print_board(board)

        if check_win(board, 'O'):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
