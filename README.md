# 🍴 Madplan

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![version](https://img.shields.io/badge/version-1.0.4-blue.svg)](https://github.com/dit-brugernavn/dit-repo)
[![maintainer](https://img.shields.io/badge/maintainer-Supersej-blue.svg)](https://github.com/supersej)
[![buy_me_a_coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/darkdk)

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

Vis madplan for dags dato,
inklusiv billede af menuen såfremt dette er tilgængeligt.

```yaml
type: markdown
content: >
  {% set state = states('sensor.madplan_2') %} {% set img =
  state_attr('sensor.madplan_2', 'image_url') %}

  {% set days = ['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag',
  'søndag'] %} {% set months = ['januar', 'februar', 'marts', 'april', 'maj',
  'juni', 'juli', 'august', 'september', 'oktober', 'november', 'december'] %}
  {% set day_name = days[now().weekday()] %} {% set month_name =
  months[now().month - 1] %} {% set date_str = day_name ~ ", " ~ now().day ~ " "
  ~ month_name ~ " " ~ now().year %}

  <div style="text-align: center;"> <span style="color:
  var(--secondary-text-color); font-size: 0.9em;">{{ date_str }}</span> <h1
  style="margin: 10px 0 20px 0; font-size: 2em; font-weight: bold;">{{ state
  }}</h1> {% if img %} <img src="{{ img }}" style="width: 100%; border-radius:
  16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"> {% else %} <div style="padding:
  20px; background: rgba(255,255,255,0.1); border-radius: 16px;">🍽️ Intet
  billede</div> {% endif %} </div>
```

### 📋 Tabel-visning via Markdown kort

Denne kode laver en pæn tabel over de kommende dage,
inklusiv billede af menuen såfremt dette er tilgængeligt.


```yaml
type: markdown
content: >
  ## 🍴 Madplan

  {% set plan = state_attr('sensor.madplan_2', 'helo_schedule') %}


  {% if plan %}

  | Dato | Ret |

  | :--- | :--- |

  {% for item in plan -%}

  | {{ item.dato }} | {% if item.image_url %}<img src="{{ item.image_url }}"
  width="30" style="vertical-align:middle;border-radius:50%"> {% endif %}{{
  item.ret }} |

  {% endfor %}

  {% else %}

  *Ingen madplan fundet...*

  {% endif %}
```
