import logging
import aiohttp
from datetime import date, timedelta
from homeassistant.util import Throttle
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

# Opdateres hver time
TIME_BETWEEN_UPDATES = timedelta(minutes=60)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Opsætter sensoren."""
    api_key = entry.data["api_key"]
    api_url = entry.data.get("api_url")
    
    # Vi bruger update_before_add=True så den henter data med det samme ved start
    async_add_entities([MinMadplanSensor(api_key, api_url)], update_before_add=True)

class MinMadplanSensor(SensorEntity):
    def __init__(self, api_key, api_url):
        self._api_key = api_key
        self._api_url = api_url
        self._state = None
        # Navnet på selve entiteten i HA
        self._attr_name = "Madplan"
        # Unikt ID baseret på det nye domæne
        self._attr_unique_id = f"min_madplan_{api_key}"
        self._attr_icon = "mdi:food-fork-drink"

    @property
    def state(self):
        return self._state

    @Throttle(TIME_BETWEEN_UPDATES)
    async def async_update(self):
        """Henter data."""
        if not self._api_url:
            return

        # --- NY LOGIK START ---
        # 1. Vi fjerner slash til sidst (hvis den findes) for at undgå dobbelt-slash
        clean_url = self._api_url.rstrip("/")

        # 2. Vi tjekker om '/schedule' mangler, og tilføjer det hvis nødvendigt
        if not clean_url.endswith("schedule"):
            final_url = f"{clean_url}/schedule"
        else:
            final_url = clean_url
        # --- NY LOGIK SLUT ---

        headers = {
            "X-Api-Key": self._api_key,
            "Accept": "application/json"
        }

        try:
            async with aiohttp.ClientSession() as session:
                # VIGTIGT: Brug 'final_url' her i stedet for self._api_url
                async with session.get(final_url, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        schedule_list = data.get("schedule", [])
                        
                        parsed_schedule = []
                        today_meal = "Ingen madplan i dag"
                        today_str = str(date.today())

                        for item in schedule_list:
                            scheduled_date = item.get("scheduled_date")
                            meals_data = item.get("meals") or {}
                            meal_name = meals_data.get("name", "Ukendt ret")

                            parsed_schedule.append({
                                "dato": scheduled_date,
                                "ret": meal_name
                            })

                            if scheduled_date == today_str:
                                today_meal = meal_name

                        self._state = today_meal
                        self._attr_extra_state_attributes = {
                            "helo_schedule": parsed_schedule,
                            "last_update": str(date.today()),
                            "api_endpoint_used": final_url # God til debugging
                        }
                    else:
                        _LOGGER.error("Fejl %s ved kald til %s", response.status, final_url)

        except Exception as e:
            _LOGGER.error("Kunne ikke forbinde: %s", e)