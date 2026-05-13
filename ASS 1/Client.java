import java.rmi.*;
import java.util.Scanner;

public class Client{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        try{
            String serverUrl = "rmi://localhost/Server";
            ServerIntf serverIntf = (ServerIntf) Naming.lookup(serverUrl);
            
            System.out.print("Enter First Number ");
            double num1 = sc.nextDouble();

            System.out.print("Enter Second Number ");
            double num2 = sc.nextDouble();

            System.out.println("First Number is " + num1);
            System.out.println("Second Number is " + num2);


            System.out.println("--------------------RESULTS--------------------");
            System.out.println("ADDITION IS : " + serverIntf.Addition(num1,num2));
            System.out.println("SUBTRACTION IS : " + serverIntf.Subtraction(num1,num2));
            System.out.println("MULTIPLICATION IS : " + serverIntf.Multiplication(num1,num2));
            System.out.println("DIVISION IS : " + serverIntf.Division(num1,num2));
        }
        catch(Exception e){
            System.out.println("Exception Occurred at Server!" + e.getMessage());
        }
    }
}