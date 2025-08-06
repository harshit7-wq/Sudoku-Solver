def print_board(board):
    for i in range(9):
        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += " | "
            row += str(board[i][j]) if board[i][j] != 0 else "."
            row += " "
        print(row)
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j  # row, col
    return None

def is_valid(board, num, pos):
    row, col = pos
    # Check row
    for j in range(9):
        if board[row][j] == num and j != col:
            return False
    # Check column
    for i in range(9):
        if board[i][col] == num and i != row:
            return False
    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # Solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # backtrack
    return False

if __name__ == "__main__":
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku board before solving:\n")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSudoku board after solving:\n")
        print_board(sudoku_board)
    else:
        print("No solution exists for the given Sudoku puzzle.")
