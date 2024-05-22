import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
//        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[26];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = -1;  // 배열에 -1 다 넣어놓기
        }

        String S = sc.nextLine();
        for (int i = 0; i < S.length(); i++) {
            char ch = S.charAt(i);  // 문자열 추출 후 ch에 저장 

            if(arr[ch -'a'] == -1){  // -1인 경우에만
                arr[ch - 'a'] = i;
            }
        }

        for(int val : arr){
            System.out.print(val + " ");
        }
        sc.close();



    }
}