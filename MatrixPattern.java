import java.util.Scanner;

public class MatrixPattern {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the matrix (n): ");
        int n = scanner.nextInt();
        System.out.print("Is the matrix linear or cyclical? (Enter 'linear' or 'cyclical'): ");
        String type = scanner.next().toLowerCase();


        int[][] matrix = new int[n][n];

        // Filling the matrix based on conditions
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    matrix[i][j] = 0;
                } else if (Math.abs(i - j) == 1) {
                    matrix[i][j] = 1;
                } else if (type.equals("cyclical") && (i == 0 && j == n - 1 || i == n - 1 && j == 0)) {
                    matrix[i][j] = 1;
                } else {
                    matrix[i][j] = 0;
                }
            }
        }

        // Printing the matrix
        System.out.println();
        System.out.println("Generated Matrix:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }

                    System.out.println();


        // Printing matrix for Wolfram
         System.out.println("Wolfram Code:");
        System.out.print("{ ");
        for (int i = 0; i < n; i++) {
            System.out.print("{ ");
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j]);
                if (j < n - 1) System.out.print(", ");
            }
            System.out.print(" }");
            if (i < n - 1) System.out.print(", ");
        }
        System.out.println(" }");

       

    
        }
        
    }

