import voluptuous as vol
from homeassistant import config_entries

# Skal matche mappenavnet præcist
DOMAIN = "min_madplan"

class MinMadplanConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Konfigurationsflow for Min Madplan."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            if not user_input["api_url"].startswith("http"):
                errors["base"] = "invalid_url"
            else:
                return self.async_create_entry(
                    title="Madplan API", 
                    data=user_input
                )

        schema = vol.Schema({
            vol.Required("api_key"): str,
            vol.Required("api_url", default="https://din-api-url.dk"): str,
        })

        return self.async_show_form(
            step_id="user", 
            data_schema=schema, 
            errors=errors
        )