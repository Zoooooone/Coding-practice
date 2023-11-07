import java.util.Arrays;

public class multi_mention {
    public static void main(String[] args){
        int[][] m1 = {{1, 2, 3}, {4, 5, 6}}, m2 = {{2, 3}, {1, -1}, {5, -3}};
        int [][] res = multi_mention.matrix_dot(m1, m2);
        System.out.print("m1 = " + Arrays.deepToString(m1) + "\t\tm2 = " + Arrays.deepToString(m2));
        System.out.println("\nm1 * m2 = " + Arrays.deepToString(res));
    }

    private static int[][] matrix_dot(int[][] A, int[][] B){
        // A = m * n, B = n * l
        int m = A.length, n = A[0].length, l = B[0].length;        
        int[][] ans = new int[m][l];

        for (int i = 0; i < m; i++){
            for (int j = 0; j < l; j++){
                for (int k = 0; k < n; k++){
                    ans[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        return ans;
    }
}
