def main():
    n = int(input("Enter the size of the matrix (n): "))
    matrix_type = input("Is the matrix linear or cyclical? (Enter 'linear' or 'cyclical'): ").lower()

    matrix = [[0] * n for _ in range(n)]

    # Filling the matrix based on conditions
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0
            elif abs(i - j) == 1:
                matrix[i][j] = 1
            elif matrix_type == "cyclical" and ((i == 0 and j == n - 1) or (i == n - 1 and j == 0)):
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

    # Printing the matrix
    print("\nGenerated Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

    print("\nWolfram Code:")
    print("{", end=" ")
    for i in range(n):
        print("{", end=" ")
        for j in range(n):
            print(matrix[i][j], end="")
            if j < n - 1:
                print(", ", end="")
        print("}", end="")
        if i < n - 1:
            print(", ", end="")
    print(" }")

if __name__ == "__main__":
    main()
