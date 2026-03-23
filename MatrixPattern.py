import urllib.parse


def matrix_to_wolfram(matrix):
    """Convert Python matrix to Wolfram format"""
    wolfram_str = "{"
    for i, row in enumerate(matrix):
        wolfram_str += "{"
        wolfram_str += ",".join(map(str, row))
        wolfram_str += "}"
        if i < len(matrix) - 1:
            wolfram_str += ","
    wolfram_str += "}"
    return wolfram_str


def generate_wolfram_link(matrix, operation):
    """Generate Wolfram Alpha link for a given operation"""
    wolfram_matrix = matrix_to_wolfram(matrix)
    query = f"{operation} {wolfram_matrix}"
    return "https://www.wolframalpha.com/input?i=" + urllib.parse.quote(query)


def main():
    n = int(input("Enter the size of the matrix (n): "))
    matrix_type = input(
        "Is the matrix linear or cyclical? (Enter 'linear' or 'cyclical'): "
    ).lower()

    # Initialize matrix
    matrix = [[0] * n for _ in range(n)]

    # Fill matrix
    for i in range(n):
        for j in range(n):
            if abs(i - j) == 1:
                matrix[i][j] = 1
            elif matrix_type == "cyclical" and (
                (i == 0 and j == n - 1) or (i == n - 1 and j == 0)
            ):
                matrix[i][j] = 1

    # Print matrix
    print("\nGenerated Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

    # Wolfram format
    wolfram_matrix = matrix_to_wolfram(matrix)

    print("\nWolfram Matrix Format:")
    print(wolfram_matrix)

    # Generate links
    eigen_link = generate_wolfram_link(matrix, "eigenvalues")
    diag_link = generate_wolfram_link(matrix, "diagonalize")
    ortho_link = generate_wolfram_link(matrix, "Orthogonal diagonalization:")

    # Output links
    print("\nWolfram Alpha Links:")
    print("Eigenvalues:")
    print(eigen_link)

    print("\nDiagonalization:")
    print(diag_link)

    print("\nOrthogonal Eigenvectors:")
    print(ortho_link)


if __name__ == "__main__":
    main()
