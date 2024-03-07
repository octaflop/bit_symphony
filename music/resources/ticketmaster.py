from dagster import ConfigurableResource


class TicketMasterResource(ConfigurableResource):  # type: ignore[misc]
    """A resource that connects to the ticketmaster API."""
    TM_API_KEY: str

    def get_local_events(self,
                         latlong: str = '40.7659051,-111.8487420',
                         radius: str = 60,
                         unit: str = 'miles',
                         locale: str = '*',
                         start_dt: str = '2025-03-06T15:04:00Z',
                         page: int = 1) -> str:
        """
        Get local events based on the given parameters.

        :param latlong: The latitude and longitude of the location in the format 'latitude,longitude'. Defaults to '40.7659051,-111.8487420'.
        :param radius: The search radius for finding events. Defaults to 60.
        :param unit: The unit of distance for the search radius. Defaults to 'miles'.
        :param locale: The desired locale for event information. Defaults to '*'.
        :param start_dt: The start date and time for filtering events. Defaults to '2025-03-06T15:04:00Z'.
        :param page: The page number for paginated results. Defaults to 1.
        :return: The URL for getting local events based on the parameters.
        """
        url = f"https://app.ticketmaster.com/discovery/v2/events?apikey={self.TM_API_KEY}&latlong={latlong}&radius={radius}&unit={unit}&locale={locale}&startDateTime={start_dt}"
        return url
