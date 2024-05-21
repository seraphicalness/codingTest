import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
//        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        Scanner sc = new Scanner(System.in);

        String n = sc.nextLine();  // 입력받음
        sc.close();

        System.out.println(n.length());
    }
}