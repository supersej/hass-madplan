# Privatlivspolitik for Min Madplan

**Sidst opdateret:** 17. januar 2026

Denne privatlivspolitik beskriver, hvordan applikationen "Min Madplan" ("Applikationen") indsamler, bruger og beskytter dine data. Applikationen er udviklet som en open-source integration til Home Assistant.

## 1. Indsamling af data
Applikationen indsamler udelukkende de data, der er strengt nødvendige for dens funktion:
* **API-kommunikation:** Applikationen kommunikerer med den konfigurerede API-URL for at hente madplansdata (f.eks. retter, datoer og ID'er).
* **Google Brugerdata:** Hvis Applikationen konfigureres med Google OAuth, bruges adgangstoken udelukkende til at autentificere og læse data fra de tjenester, du har godkendt (f.eks. Google Calendar eller Google Sheets).

## 2. Brug af data
Data hentet via Applikationen bruges udelukkende til:
* At vise din madplan i Home Assistant.
* At gemme data lokalt på din egen Home Assistant-instans (state og attributter).

**Vi deler ikke dine data.** Applikationen sender ingen data til tredjepart, trackere eller annonce-netværk. Al behandling sker lokalt på din egen server.

## 3. Google API Services User Data Policy
Applikationens brug og overførsel af information modtaget fra Google API'er til enhver anden app vil overholde [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), herunder kravene om begrænset brug (Limited Use).

## 4. Dataopbevaring
Dine data opbevares lokalt på din Home Assistant-enhed. Hvis du afinstallerer integrationen, slettes konfigurationen fra Home Assistant.

## 5. Kontakt
Hvis du har spørgsmål til denne privatlivspolitik, kan du oprette et "Issue" på Applikationens GitHub-repository.