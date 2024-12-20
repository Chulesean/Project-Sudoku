# 1st-individual-project
The idea I want to create is the game Sudoku
- Description: The game is created by 9x9 big square, each is created by 3x3 small square.
               The purpose is to fill all the small square by numbers from 0 to 9, which isn't repeated in a big square, in a column or in a row.
- Functionality: This program can fill some constant random numbers which follow the rules.
                 When all numbers are filled, if the numbers are repeated, the small squares containt them will flash.
                 If there's no number is repeated, appear "Congratulation!"
- Architecture: Using class SudokuBoard
                Attributes:
                    grid: A 9x9 list of lists to represent the Sudoku grid.
                    fixed_positions: A set of tuples indicating the positions of pre-filled numbers.
                Methods:
                    init(): Initializes the grid and sets up any initial pre-filled numbers.
                    generate_board(): Fills the board with an initial valid set of numbers, ensuring some cells are left empty for the player to fill.
                    is_valid_move(row, col, num): Checks if placing num in the specified row and column is valid according to Sudoku rules.
                    fill_cell(row, col, num): Fills a cell with the given number if the move is valid.
                    is_complete(): Checks if the board is completely and correctly filled.
                Class SudokuGame
                    board: An instance of SudokuBoard
                    play(): Starts the game loop, allowing the player to input numbers and update the board.
                    check_for_completion(): Checks if the game is completed correctly.
                    highlight_conflicts(): Identifies and highlights cells with conflicting numbers.
                Functions:
                    enerate_random_numbers(board): Fills the board with a random set of initial numbers, ensuring they follow Sudoku rules.
                    flash_cells(cells): Visually highlights the cells containing conflicts 