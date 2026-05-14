COMMANDS TO RUN FOR ASSIGNMENTS


ASSIGNMENT 1 - RMI CALCULATOR
1)javac *.java in terminal 1
2)rmiregistry in terminal 1
3)java Server in terminal 2
4)java Client in terminal 3


ASSIGNMENT 2 - CORBA
1)idlj -fall calculator.idl in terminal 1
2)javac client\*.java server\*.java calculator_module\*.java in terminal 1
3)orbd -ORBInitialPort 1050 -ORBInitialHost localhost in terminal 2
4)java server.CalculatorServer -ORBInitialPort 1050 -ORBInitialHost localhost in terminal 3
5)java client.CalculatorClient -ORBInitialPort 1050 -ORBInitialHost localhost in terminal 4



ASSIGNMENT 3 - OPENMP
1)gcc main.c -fopenmp -o main in terminal 1
2)main in terminal 1


ASSIGNMENT 4 - BERKLEY ALGORITHM
1)python server.py in terminal 1
2)python client.py in terminal 2,3,4


ASSIGNMENT 5 - MUTUAL EXCLUSION
1)python server.py in terminal 1
2)python client.py in terminal 2,3,4


ASSIGNMENT 6 - BULLY AND RING



ASSIGNMENT 7 
1)python api.py in terminal 1
2)python app.py in terminal 2



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Search.java
**********
package remotes;

import java.rmi.*;

public interface Search extends Remote {

    String query(String user, String pass)
            throws RemoteException;

}
===============


SearchQuery.java
*********
package remotes;

import java.rmi.*;
import java.rmi.server.*;
import java.util.HashMap;

public class SearchQuery extends UnicastRemoteObject
implements Search {

    public SearchQuery() throws RemoteException {
        super();
    }

    public String query(String user, String pass)
    throws RemoteException {

        HashMap<String,String> users =
        new HashMap<>();

        users.put("admin","123");
        users.put("pari","pari123");

        // Check username exists or not
        if(!users.containsKey(user)) {
            return "Username not found";
        }

        // Username exists but password wrong
        if(!users.get(user).equals(pass)) {
            return "Incorrect password";
        }

        // Both correct
        return "Welcome " + user;
    }
}
=============

SERVER

SearchServer.java
**********

package server;

import java.rmi.*;
import java.rmi.registry.*;

import remotes.*;

public class SearchServer {

    public static void main(String[] args) {

        try {

            Search obj = new SearchQuery();

            LocateRegistry.createRegistry(1099);

            Naming.rebind(
                    "rmi://localhost:1099/LOGIN",
                    obj);

            System.out.println("Server Ready");

        }

        catch(Exception e) {

            System.out.println(e);

        }
    }
}

=========

ClientRequest.java
******
package client;

import java.rmi.*;
import java.util.Scanner;

import remotes.Search;

public class ClientRequest {

    public static void main(String[] args) {

        try {

            Scanner sc = new Scanner(System.in);

            System.out.print("Enter Username: ");
            String user = sc.nextLine();

            System.out.print("Enter Password: ");
            String pass = sc.nextLine();

            Search obj = (Search)
                    Naming.lookup(
                    "rmi://localhost:1099/LOGIN");

            String result = obj.query(user, pass);

            System.out.println(result);

            sc.close();

        }

        catch(Exception e) {

            System.out.println(e);

        }
    }
}

========

COMMAND:

javac remotes/*.java server/*.java client/*.java

java server.SearchServer

java client.ClientRequest


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Calculator.idl
***************
module calculator_module {
    interface Calculator {
        long add(in long a, in long b);
        long subtract(in long a, in long b);
        long multiply(in long a, in long b);
        long divide(in long a, in long b);
        void shutdown();
    };
};

COMMAND :  
idlj -fall Calculator.idl

========

SERVER FOLDER:

CalculatorImpl.java
****************

package server;

import org.omg.CORBA.ORB;
import calculator_module.CalculatorPOA;

public class CalculatorImpl extends CalculatorPOA {

    ORB orb;

    public void setORB(ORB o) {
        orb = o;
    }

    public int add(int a,int b) {
        return a+b;
    }

    public int subtract(int a,int b) {
        return a-b;
    }

    public int multiply(int a,int b) {
        return a*b;
    }

    public int divide(int a,int b) {
        if(b==0) {
            System.out.println("Divide by zero not possible");
            return 0;
        }
        return a/b;
    }

    public void shutdown() {
        orb.shutdown(false);
    }
}

===================

CalculatorServer.java
*****************
package server;

import org.omg.CORBA.*;
import org.omg.CosNaming.*;
import org.omg.PortableServer.*;

import calculator_module.*;

public class CalculatorServer {

    public static void main(String args[]) {

        try {
            ORB orb = ORB.init(args,null);

            POA rootpoa = (POA) orb.resolve_initial_references("RootPOA");
            rootpoa.the_POAManager().activate();

            CalculatorImpl obj = new CalculatorImpl();
            obj.setORB(orb);

            org.omg.CORBA.Object ref = rootpoa.servant_to_reference(obj);
            Calculator href = CalculatorHelper.narrow(ref);

            org.omg.CORBA.Object objRef = orb.resolve_initial_references("NameService");
            NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);

            ncRef.rebind(ncRef.to_name("Calculator"), href);

            System.out.println("Server Ready");
            orb.run();

        } catch(Exception e) {
            System.out.println(e);
        }
    }
}

=============
CLIENT FOLDER

CalculatorClient.java
***************

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

************

COMMANDS:

idlj -fall Calculator.idl

javac calculator_module\*.java server\*.java client\*.java

terminal 1:
orbd -ORBInitialPort 1050 -ORBInitialHost localhost

terminal 2:
java server.CalculatorServer -ORBInitialPort 1050 -ORBInitialHost localhost

terminal 3:
java client.CalculatorClient -ORBInitialPort 1050 -ORBInitialHost localhost
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
