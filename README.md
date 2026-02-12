## Home Assistant Custom Component: 🍴 Madplan (Meal Plan)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![version](https://img.shields.io/badge/version-1.0.5-blue.svg)](https://github.com/supersej/hass-madplan/releases)
[![maintainer](https://img.shields.io/badge/maintainer-Supersej-blue.svg)](https://github.com/supersej)
[![buy_me_a_coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/darkdk)

**Madplan** is a custom integration for Home Assistant that retrieves your meal plan from [letmadplan.dk](https://letmadplan.dk) via its API and displays it elegantly on your dashboard.

The integration automatically handles login via an API key and formats the data for easy use in Lovelace dashboards.

## ✨ Features

* 🚀 **Easy Setup:** Configured directly through the Home Assistant User Interface (UI).
* 🔐 **Security:** Supports API Key authentication (`X-Api-Key`).
* 🧠 **Intelligent Sensor:** Displays today's meal as the state and stores the entire weekly plan as attributes.
* 📉 **Efficient:** Updates once per hour to conserve resources.
* 🖼️ **Image support:** If an image is added to the meal, this integration can show it on the dashboard.



---

## 📥 Installation

### Option 1: HACS (Recommended)

1.  Open **HACS** in Home Assistant.
2.  Go to **Integrations** > **3 dots (top right)** > **Custom repositories**.
3.  Paste the URL of this GitHub repository: [https://github.com/supersej/hass-madplan](https://github.com/supersej/hass-madplan) and select **Integration** as the category.
4.  Click **Add** and then **Download**.
5.  Restart Home Assistant.

### Option 2: Manual Installation

1.  Download this repository.
2.  Copy the `custom_components/madplan` folder into your Home Assistant `config/custom_components/` directory.
3.  Restart Home Assistant.

---

## 🔑 Create an API Key on letmadplan.dk

1. Log in to [letmadplan.dk](https://letmadplan.dk) and click the **gear icon** at the top.
2. Click the **"Konto" (Account)** tab.
3. Click **"Avancerede indstillinger" (Advanced settings)**.
4. **Optional:** Choose whether the API should have write access.
    * There is currently no built-in functionality to send data back to the site.
    * **"Skrivebeskyttet" (Read-only)** is recommended for now.
5. Click **"Generer ny nøgle" (Generate new key)**.
6. **IMPORTANT:** Save this key in a secure location, as it will not be shown again.

## ⚙️ Configuration

Once the integration is installed and Home Assistant has been restarted:

1.  Go to **Settings** > **Devices & Services**.
2.  Click **+ Add Integration** in the bottom right corner.
3.  Search for **Madplan**.
4.  Enter your **API Key**.

---

## 📱 Dashboard Cards (Lovelace)

### Today's Meal
Displays the meal for the current date, including an image if available.

```yaml
type: markdown
content: >
  {% set state = states('sensor.madplan') %} {% set img =
  state_attr('sensor.madplan', 'image_url') %}

  {% set days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
  'Sunday'] %} {% set months = ['January', 'February', 'March', 'April', 'May',
  'June', 'July', 'August', 'September', 'October', 'November', 'December'] %}
  {% set day_name = days[now().weekday()] %} {% set month_name =
  months[now().month - 1] %} {% set date_str = day_name ~ ", " ~ now().day ~ " "
  ~ month_name ~ " " ~ now().year %}

  <div style="text-align: center;"> <span style="color:
  var(--secondary-text-color); font-size: 0.9em;">{{ date_str }}</span> <h1
  style="margin: 10px 0 20px 0; font-size: 2em; font-weight: bold;">{{ state
  }}</h1> {% if img %} <img src="{{ img }}" style="width: 100%; border-radius:
  16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"> {% else %} <div style="padding:
  20px; background: rgba(255,255,255,0.1); border-radius: 16px;">🍽️ No image available</div> {% endif %} </div>
```

## 📋 Table View via Markdown Card
This code creates a clean table of the upcoming days, including meal images where available.

```yaml
type: markdown
content: >
  ## 🍴 Meal Plan

  {% set plan = state_attr('sensor.madplan', 'helo_schedule') %}

  {% if plan %}

  | Date | Meal |
  | :--- | :--- |
  {% for item in plan -%}
  | {{ item.dato }} | {% if item.image_url %}<img src="{{ item.image_url }}" width="30" style="vertical-align:middle;border-radius:50%"> {% endif %}{{ item.ret }} |
  {% endfor %}

  {% else %}

  *No meal plan found...*

  {% endif %}
```