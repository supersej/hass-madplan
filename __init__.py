from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

# Her definerer vi domænet ét sted
DOMAIN = "madplan"
PLATFORMS = ["sensor"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Starter integrationen."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Stopper integrationen."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)