
class Pattern {
    public static void main(String[] args) {

        for (int i = 4; i >= 1; i--) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
                /*
                 * if (i == 1 || j == 1 || i == 4 || j == 5) {
                 * System.out.print("*");
                 * } else {
                 * System.out.print(" ");
                 * }
                 */
            }
            System.out.println();

        }
    }
}