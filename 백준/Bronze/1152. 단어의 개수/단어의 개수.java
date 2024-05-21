import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
//        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        Scanner sc = new Scanner(System.in);

        String n = sc.nextLine();  // 입력받음
        sc.close();

        // StringTokenizer:
        // 공백을 기준으로 나뉘어 토큰에 저장하기 때문에 입력한 문자열의
        // 처음이나 마지막에 공백이 있어도 동일한 결과를 출력
        StringTokenizer st = new StringTokenizer(n," ");
        System.out.println(st.countTokens());



    }
}