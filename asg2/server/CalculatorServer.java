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