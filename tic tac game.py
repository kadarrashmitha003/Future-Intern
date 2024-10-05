def print_board(board):
    """Prints the Tic Tac Toe board."""
    print("\n".join([" | ".join(row) for row in board]))
    print("\n")

def check_winner(board, player):
    """Checks if the current player has won."""
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    """Checks if the board is full and it's a draw."""
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'
        
        while True:
            print_board(board)
            print(f"Player {current_player}'s turn.")

            # Get move
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Invalid input. Please enter row and column as 0, 1, or 2.")
                    continue
                
                if board[row][col] != ' ':
                    print("Cell already taken. Choose another cell.")
                    continue
                
                board[row][col] = current_player
                
            except ValueError:
                print("Invalid input. Please enter numeric values for row and column.")
                continue
            
            # Check for a win
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins! 🎉")
                break

            # Check for a draw
            if check_draw(board):
                print_board(board)
                print("It's a draw! 🤝")
                break
            
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
        
        # Ask to restart or exit
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! 👋")
            break

# Start the game
tic_tac_toe()
