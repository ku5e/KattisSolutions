import java.util.*;

/*
* Programmer: Mario Martinez
* date: 04/01/2022  
* Purpose: FinalExam2
*/

class Untitled {
    public static void main(String[] args) {
        int score = 0;
        Scanner stdIn = new Scanner(System.in);
        int count = stdIn.nextInt();
        stdIn.nextLine();
        
        String[] arr = new String[count];
        for (int i = 0; i < count; i++) {
            arr[i] = stdIn.nextLine();
            if(i > 0 && arr[i].equals(arr[i - 1])){
                score++;
            }
        }
        System.out.println(score);
        
    }
}