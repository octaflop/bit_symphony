from dagster import load_assets_from_modules
from . import (
    artists,
)

artists_assets = load_assets_from_modules([artists])
