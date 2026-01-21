# 🍴 Madplan

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![version](https://img.shields.io/badge/version-1.0.3-blue.svg)](https://github.com/dit-brugernavn/dit-repo)
[![maintainer](https://img.shields.io/badge/maintainer-Supersej-green.svg)](https://github.com/supersej)

**Madplan** er en custom integration til Home Assistant, der henter din madplan fra [madplan.drk.one](https://madplan.drk.one) via dennes API og viser den pænt på dit dashboard.

Integrationen håndterer automatisk login via API-nøgle og formaterer dataen, så den er let at bruge i Lovelace (dashboards).

## ✨ Funktioner

* 🚀 **Nem opsætning:** Konfigureres direkte via Home Assistants brugerflade (UI).
* 🔐 **Sikkerhed:** Understøtter API Key authentication (`X-Api-Key`).
* 🧠 **Intelligent Sensor:** Viser dagens ret som status og gemmer hele ugeplanen som attributter.
* 📉 **Effektiv:** Opdaterer kun én gang i timen for at spare ressourcer.

---

## 📥 Installation

### Mulighed 1: HACS (Anbefales)

1.  Åbn HACS i Home Assistant.
2.  Gå til **Integrationer** > **3 prikker (øverst)** > **Brugerdefinerede lagre**.
3.  Indsæt URL'en til dette GitHub repository: [https://github.com/supersej/hass-madplan](https://github.com/supersej/hass-madplan) og vælg **Integration**.
4.  Klik **Tilføj** og derefter **Download**.
5.  Genstart Home Assistant.

### Mulighed 2: Manuel Installation

1.  Download dette repository.
2.  Kopier mappen `custom_components/min_madplan` over i din Home Assistant `config/custom_components/` mappe.
3.  Genstart Home Assistant.

---

## 🔑 Opret API nøgle på madplan.drk.one

1. Når du er logget ind på [madplan.drk.one](https://madplan.drk.one) skal du trykke på tandhjulet i toppen
2. Klikke på fanen "konto"
3. Klikke på "advanceret indstillinger"
4. **Valgfrit:** Vælg om api skal have skriveadgang eller ej.
   * Der er endnu ikke indbygget funktionalitet til at sende data tilbage til madplan.drk.one
   * **Skrivebeskyttet** er derfor anbefalet
5. Tryk "Generer ny nøgle"
6. **VIGTIGT** gem denne nøgle et sikkert sted da den ikke vil blive vist igen.

## ⚙️ Opsætning

Når integrationen er installeret og Home Assistant er genstartet:

1.  Gå til **Indstillinger** > **Enheder og tjenester**.
2.  Klik på **+ Tilføj Integration** nederst til højre.
3.  Søg efter **Madplan**.
4.  Indtast din **API Nøgle**.


---

## 📱 Dashboard Kort (Lovelace)

Her er et eksempel på at vise madplanen.

### 📋 Tabel-visning via Markdown kort

Denne kode laver en pæn tabel over de kommende dage.

```yaml
type: markdown
content: |
  ## 🍴 Madplan
  {% set plan = state_attr('sensor.madplan', 'helo_schedule') %}

  {% if plan %}
  | Dato | Dagens Ret |
  | :--- | :--- |
  {% for item in plan -%}
  | {{ item.dato }} | {{ item.ret }} |
  {% endfor %}
  {% else %}
  *Ingen madplan data fundet...*
  {% endif %}