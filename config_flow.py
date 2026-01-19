import voluptuous as vol
from homeassistant import config_entries

DOMAIN = "min_madplan"
# Indtast din faste URL her
CONF_API_URL = "https://yqwrvwjapllfqefejyhr.supabase.co/functions/v1/meal-api/schedule"

class MinMadplanConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Konfigurationsflow for Min Madplan."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # Her injicerer vi den hardcodede URL ind i konfigurationen,
            # så den bliver gemt sammen med API-nøglen.
            user_input["api_url"] = CONF_API_URL

            return self.async_create_entry(
                title="Madplan API", 
                data=user_input
            )

        # Schema viser nu kun api_key feltet
        schema = vol.Schema({
            vol.Required("api_key"): str,
        })

        return self.async_show_form(
            step_id="user", 
            data_schema=schema, 
            errors=errors
        )