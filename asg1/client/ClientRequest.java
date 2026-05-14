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


// javac remotes*.java server*.java client*.java

// java server.SearchServer

// java client.ClientRequest
