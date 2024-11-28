import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> arr = new ArrayList<>();
        int T = sc.nextInt();
        if(T<1){
            return;
        }

        for (int i = 0; i<T;i++){
            String vps = sc.next();
            if (vps.length()<2 || vps.length()>50){
                return;
            }else {
                Stack<Character> stack = new Stack<>();
                for(int j =0;j<vps.length();j++){
                    if(vps.charAt(j)=='(') {
                        stack.push(vps.charAt(j));
                    }else {
                        if(stack.empty()){
                            stack.push(vps.charAt(j));
                            break;
                        }else{
                            stack.pop();
                        }
                    }
                }
                if(stack.empty()){
                    arr.add("YES");
                }else{
                    arr.add("NO");
                }
            }
        }
       for(String r :arr){
           System.out.println(r);
       }
        sc.close();

    }
}
