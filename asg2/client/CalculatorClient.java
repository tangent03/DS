package client;

import java.util.Scanner;
import org.omg.CORBA.*;
import org.omg.CosNaming.*;
import calculator_module.*;

public class CalculatorClient {

    public static void main(String args[]) {

        try {
            ORB orb = ORB.init(args,null);

            org.omg.CORBA.Object objRef = orb.resolve_initial_references("NameService");
            NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);

            Calculator obj = CalculatorHelper.narrow(ncRef.resolve_str("Calculator"));

            Scanner sc = new Scanner(System.in);

            while(true) {
                System.out.println("\n1.Add");
                System.out.println("2.Subtract");
                System.out.println("3.Multiply");
                System.out.println("4.Divide");
                System.out.println("5.Exit");

                System.out.print("Choice: ");
                int ch = sc.nextInt();

                if(ch==5)
                    break;

                System.out.print("Enter first number: ");
                int a = sc.nextInt();

                System.out.print("Enter second number: ");
                int b = sc.nextInt();

                switch(ch) {
                    case 1:
                        System.out.println("Result = "+obj.add(a,b));
                        break;
                    case 2:
                        System.out.println("Result = "+obj.subtract(a,b));
                        break;
                    case 3:
                        System.out.println("Result = "+obj.multiply(a,b));
                        break;
                    case 4:
                        // NEW FIX: Check for zero here on the client side
                        if (b == 0) {
                            System.out.println("Result = Infinity (Divide by zero not possible)");
                        } else {
                            System.out.println("Result = "+obj.divide(a,b));
                        }
                        break;
                    default:
                        System.out.println("Invalid Choice");
                }
            }
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}