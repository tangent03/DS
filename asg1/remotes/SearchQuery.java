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