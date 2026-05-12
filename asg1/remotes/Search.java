package remotes;

import java.rmi.*;

public interface Search extends Remote {

    String query(String user, String pass)
            throws RemoteException;

}