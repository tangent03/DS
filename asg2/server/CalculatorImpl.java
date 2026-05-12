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