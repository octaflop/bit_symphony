from dagster import load_assets_from_modules
from . import (
    events,
)

artists_assets = load_assets_from_modules([events])
