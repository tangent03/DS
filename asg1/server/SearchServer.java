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