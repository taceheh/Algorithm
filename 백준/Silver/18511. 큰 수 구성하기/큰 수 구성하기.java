

import java.util.Scanner;

public class Main {
    static int n;
    static int k;
    static String[] arr;
    static int result=0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();

       arr = new String[k];
        for(int i =0;i<k;i++){
            String element = sc.next();
            arr[i]=element;
        }

        recursive(0);
        System.out.println(result);
    }

    private static void recursive(int num) {

        if(num>n){
            return;
        }
        if (num>result){
            result=num;
        }

        for(int i =0;i<k;i++){
            recursive(num*10+Integer.parseInt(arr[i]));
        }


    }
}
