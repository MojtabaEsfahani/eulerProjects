
/*

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

233168
*/
public class Main {

    public static void main(String[] args) {

        long result = 0L;
        int anzahl=0;

        for(int i = 1;i<1000;i++){
            if((i%3)==0||(i%5)==0){
                result+=i;
                anzahl++;
            }
        }

        System.out.println("\n######### The First Euler Project #########\n");
        System.out.println("The Result :"+result);
        System.out.println("The Number Of Numbers : " + anzahl);
    }
}
