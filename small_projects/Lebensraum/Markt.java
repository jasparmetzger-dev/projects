package Lebensraum;

import java.util.HashMap;
import java.util.Random;

class Markt {
    private int rohstoffe;
    private HashMap<String, Integer> gueterPreise; // Handelbare Güter mit Preisen

    public Markt(int rohstoffe) {
        this.rohstoffe = rohstoffe;
        this.gueterPreise = new HashMap<>(); //mehr güter leicht addierbar
        gueterPreise.put("Essen", 50);
    }

    public int getRohstoffe() {return rohstoffe;}
    public void setRohstoffe() {
        Random random = new Random();
        this.rohstoffe = random.nextInt(20) + 80; // 80-100 Ressourcen
        updatePreise(); // Preise anpassen
    }

    public int getGueterPreise() {return gueterPreise.get("Essen");}

    public void updatePreise() {
        Random random = new Random();
        for (String gut : gueterPreise.keySet()) {
            int preis = gueterPreise.get(gut);
            gueterPreise.put(gut, Math.max(10, preis + random.nextInt(20) - 10)); // Schwankungen ±10 im Preis
        }
    }

    public void handleTrade(Mensch mensch, String gut, int menge, boolean kaufen) {
        if (!gueterPreise.containsKey(gut)) return; //edge case, da es ohne zT einen Error gab 

        int preis = gueterPreise.get(gut) * menge;
        if (kaufen) { //Kauf
            if (mensch.getKapital() >= preis) {
                mensch.setKapital(mensch.getKapital() - preis);
                System.out.println(mensch.getName() + " hat " + menge + " " + gut + " für EUR " + preis + " gekauft.");
            }
            else {
                System.out.println(mensch.getName() + " hat nicht genug Kapital, um " + gut + " zu kaufen.");
            }
        } else { // Verkauf
            mensch.setKapital(mensch.getKapital() + preis);
            System.out.println(mensch.getName() + " hat " + menge + " " + gut + " für EUR " + preis + " verkauft.");
        }
    }
}