package Lebensraum;

public class Mensch extends Instanzen {
    private int alter;
    private String job;

    public Mensch(int alter, String job, String name, double kapital, int einkommen, int ausgaben, double liquidität) {
        super(name, kapital, einkommen, ausgaben, liquidität);
        this.alter = alter;
        this.job = job;
    }

    public int getAlter() { return alter; }
    public void setAlter(int alter) { this.alter = alter; }
    public String getJob() { return job; }
    public void setJob(String job) { this.job = job; }

    public void findeJob() {
        setJob("Bauer"); //random job auch moeglich; hier noch nicht implementiert, da nur eine Person mit Alter <18
        setEinkommen(50000);
        setAusgaben((int) (getEinkommen() * 0.9));
    }

    public void leben(float ressourcen, Markt markt) {
        double kapitalzinsen = 1.02; // Zinsen
        double gehaltserhoehung = 1.04; // Einkommenssteigerung
    
        // Inflation
        float inflation = Math.max(1.0f, 1 + (ressourcen - 100) / 500.0f);
        setAusgaben((int) (getAusgaben() * inflation));
    
        // Kapitalmanagement
        if (alter > 80) {
            setKapital(getKapital() / (10 - ressourcen / 10.0) * 0.8); //Vererbung / Brute Force, um Geld zu verlieren
        } else {
            if (getKapital() > 1000000 && getKapital() < 5000000) { //Vermoegenssteuer / Kapitalertragssteuer
                setKapital(getKapital() * (1 + (kapitalzinsen - 1) * 0.6));
            } else if (getKapital() > 5000000) {
                setKapital(getKapital() * (1 + (kapitalzinsen - 1) * 0.4));
            } else { //normaler Fall
                setKapital(getKapital() * kapitalzinsen);
            }
        }
    
        updateLiquidität();
    
        // Wirtschaftliche Notlage 1% Wahrscheinlichkeit, um Variabilität zu produzieren
        if (Math.random() < 0.01) {
            setKapital(getKapital() - 10000);
            System.out.println("Wirtschaftliche Notlage für " + getName());
        }
    
        // Einkommen
        alter++;
        if (alter == 18) {
            findeJob();
        } else if (alter > 18 && alter < 67) {
            setEinkommen((int) (getEinkommen() * gehaltserhoehung));
        } else if (alter >= 67) { // Rente
            setEinkommen(0);
        }
    
        // Wirtschaftlicher "Tod" oder Verhungern, je nach Interpretation
        if (getKapital() <= 0) {sterben();}
    
        // Handel
        if (Math.random() < 0.4) { // 40% Wahrscheinlichkeit für Handel
            String gut = "Essen";
            int menge = 10; // Beispiel-Menge
    
            if (Math.random() < 0.3) { // 30% Wahrscheinlichkeit für Kauf/Verkauf
                markt.handleTrade(this, gut, menge, true); // Kauf
            } else {
                markt.handleTrade(this, gut, menge, false); // Verkauf
            }
        }
    }
}