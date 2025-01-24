public class Main {
    public static void main(String[] args) {
            String[] input =  {    "______",
                                ",-' ;  ! `-.",
                                "/ :  !  :  . \\",
                                "|_ ;   __:  ;  |",
                                ")| .  :)(.  !  |",
                                "|\"    (##)  _  |",
                               "|  :  ;`'  (_) (",
                "|  :  :  .     |",
 ")_ !  ,  ;  ;  |",
 "|| .  .  :  :  |",
 "|\" .  |  :  .  |",
                "|mt-2_;----.___|",};


            for(String s : input){
                System.out.println(reverseAndReplace(s));
            }}

    public static String reverseAndReplace(String input) {
        StringBuilder reversed = new StringBuilder();

        for (int i = input.length() - 1; i >= 0; i--) {
            char c = input.charAt(i);
            switch (c) {
                case '/':
                    reversed.append('\\');
                    break;
                case '\\':
                    reversed.append('/');
                    break;
                case '(':
                    reversed.append(')');
                    break;
                case ')':
                    reversed.append('(');
                    break;
                default:
                    reversed.append(c);
                    break;
            }
        }
        return reversed.toString();
}}