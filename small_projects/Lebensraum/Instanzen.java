package Lebensraum;

public class Instanzen {
    private String name;
    private double kapital;
    private int einkommen;
    private int ausgaben;
    private double liquidität;

    public Instanzen(String name, double kapital, int einkommen, int ausgaben, double liquidität) {
        this.name = name;
        this.kapital = kapital;
        this.einkommen = einkommen;
        this.ausgaben = ausgaben;
        this.liquidität = liquidität;
        profit();
        updateLiquidität();
    }

    public String getName() {return name;}
    public double getKapital() {return kapital;}
    public void setKapital(double kapital) {this.kapital = kapital;}
    public int getEinkommen() {return einkommen;}
    public void setEinkommen(int einkommen) {
        this.einkommen = einkommen;
        profit();}

    public int getAusgaben() {return ausgaben;}
    public void setAusgaben(int ausgaben) {
        this.ausgaben = ausgaben;
        profit();}
        
    public double getLiquidität() {return liquidität;}
    public void setLiquidität(double liquidität) {this.liquidität = liquidität;}

    private int profit() {
        int profit = einkommen - ausgaben;
        return profit;
    }
    //in das Kapital "einzahlen"
    public void updateLiquidität() {
        int p = profit();

        liquidität += p;
        if (liquidität < 0) {
            kapital += liquidität;
            liquidität = 0;
        }
        if (kapital < 0) {
            sterben();
        }
    }
    //sterben
    public void sterben() {
        setEinkommen(0);
        setAusgaben(0);;
        setKapital(0);
        System.out.println(name + " ist tod.");
    }
}