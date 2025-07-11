package Lebensraum;

import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        int rs = 100;
        Markt markt = new Markt(rs);

        // Jobliste (variabel)
        HashMap<String, Integer> jobs = new HashMap<>();
        jobs.put("Arzt", 90000);
        jobs.put("Handwerker", 55000);
        jobs.put("Bauer", 50000);
        jobs.put("Lehrer", 60000);
        jobs.put("Informatiker", 120000);

        // Menschen (variabel)
        Mensch[] menschen = {
            new Mensch(29, "Arzt", "Joschua", 10000, jobs.get("Arzt"), 80000, 50000),
            new Mensch(44, "Handwerker", "Herbert", 80000, jobs.get("Handwerker"), 40000, 80000),
            new Mensch(12, "Bauer", "Jokabinus", 100, 200, 100, 100),
            new Mensch(65, "Lehrer", "Guthrudh", 150000, jobs.get("Lehrer"), 50000, 100000),
            new Mensch(26, "Informatiker", "Justus-Jonas", 50000, jobs.get("Informatiker"), 60000, 10000),
            new Mensch(51, "Lehrer", "Robert", 50000, jobs.get("Lehrer"), 50000, 20000)
        };

        int zyklus_laenge = 10; //HIER VERÄNDERN

        for (int jahr = 1; jahr <= zyklus_laenge; jahr++) {
            markt.setRohstoffe();
            float ressourcen = markt.getRohstoffe();

            System.out.println("=== Jahr: " + jahr + ", Rohstoffe: " + (int) ressourcen + ", Essenspreis: " + markt.getGueterPreise() + " ===\n");

            double totalKapital = 0; //zählen für durchschnitt
            int totalAlter = 0;

            for (Mensch mensch : menschen) {
                mensch.leben(ressourcen, markt); // Job ausüben & handeln
                System.out.printf("%s: Kapital EUR %d, Alter %d%n",
                        mensch.getName(), (int) mensch.getKapital(), mensch.getAlter());
                totalKapital += mensch.getKapital();
                totalAlter += mensch.getAlter();
            }
            System.out.println();
            System.out.printf("Durchschnittliches Kapital: EUR %.2f%n", totalKapital / menschen.length);
            System.out.printf("Durchschnittliches Alter: %.1f Jahre%n", (double) totalAlter / menschen.length);
            System.out.println();
        }
    }
}