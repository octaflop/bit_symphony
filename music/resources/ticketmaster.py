
from dagster import ConfigurableResource



class TicketMasterResource(ConfigurableResource):  # type: ignore[misc]
    """A resource that connects to a PlanetScale database."""

    host: str
    user: str
    password: str
    db: str
    port: int

    def get_url(self) -> str:
        return get_sql_alchemy_url(
            self.user, self.password, self.host, self.db, self.port
        )