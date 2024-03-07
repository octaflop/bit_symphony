import os
from datetime import datetime

import httpx
import pandas as pd
from dagster import (
    MetadataValue,
    asset,
    AssetExecutionContext, file_relative_path, AssetIn,
)
from dagstermill import define_dagstermill_asset

from music.partitions import daily_events


@asset(
    group_name="artists",
    description="Artists asset",
    compute_kind="pandas",
    partitions_def=daily_events
)
def fetch_daily_concerts(context: AssetExecutionContext) -> pd.DataFrame:
    start_dt = context.partition_key
    context.log.info(f"Fetching concerts for today {start_dt}")
    TM_API_KEY = os.environ['TM_API_KEY']
    latlong = '40.7659051,-111.8487420'  # SLCPython UoU
    radius = 60
    unit = 'miles'
    page = 1
    locale = "*"
    url = f"https://app.ticketmaster.com/discovery/v2/events?apikey={TM_API_KEY}&latlong={latlong}&radius={radius}&unit={unit}&locale={locale}&startDateTime={start_dt}"
    resp = httpx.get(url)
    df = pd.DataFrame.from_records(resp.json()['_embedded']['events'])
    context.add_output_metadata(metadata={
        "num_events": MetadataValue.int(len(df))
    })
    return df


@asset(
    group_name="artists",
    description="Artists asset",
    compute_kind="pandas",
    partitions_def=daily_events
)
def transform_daily_concerts(context: AssetExecutionContext, fetch_concerts: pd.DataFrame) -> pd.DataFrame:
    return fetch_concerts

# # Uncomment to debug, note this will slow down downstream jobs when enabled
artists_playground = define_dagstermill_asset(
    name="artists_playground",
    notebook_path=file_relative_path(
        __file__,
        "../notebooks/inputs/music_events.ipynb"
    ),
    group_name="artists",
    description="An enriched, artist playground.",
    ins={
        "fetch_concerts": AssetIn("fetch_concerts"),

    },
    io_manager_key="nb_io_manager",
    partitions_def=daily_events
)

#%%
