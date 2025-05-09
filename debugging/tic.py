#!/usr/bin/python3

def print_board(board):
    """
    Displays the Tic-Tac-Toe board with proper formatting.
    """
    for row in board:
        print(" | ".join(row))
    print("-" * 9)  # Corrected separator length

def check_winner(board):
    """
    Checks if any player has won the game.
    
    Returns:
    bool: True if there's a winner, False otherwise.
    """
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_valid_move(row, col, board):
    """
    Validates the move to ensure it's within bounds and the spot is available.
    
    Returns:
    bool: True if valid, False otherwise.
    """
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def tic_tac_toe():
    """
    Runs the Tic-Tac-Toe game loop with player input validation.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if not is_valid_move(row, col, board):
                print("Invalid move! Spot is taken or out of range. Try again.")
                continue

            board[row][col] = player

            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # Switch players correctly
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter numbers only.")

tic_tac_toe()
