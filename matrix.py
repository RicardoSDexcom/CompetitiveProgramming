def sum_diagonals(matrix):
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        return 0
    
    # Get the dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Sum the main diagonal
    main_diagonal_sum = sum(matrix[i][i] for i in range(min(rows, cols)))

    # Sum the secondary diagonal
    secondary_diagonal_sum = sum(matrix[i][cols - 1 - i] for i in range(min(rows, cols)))

    # Return the sum of both diagonals
    return main_diagonal_sum + secondary_diagonal_sum

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = sum_diagonals(matrix)
print("Sum of diagonals:", result)
