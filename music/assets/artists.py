from datetime import datetime

import pandas as pd
from dagster import (
    MetadataValue,
    asset,
    AssetExecutionContext, file_relative_path, AssetIn,
)
from dagstermill import define_dagstermill_asset


@asset(
    group_name="artists",
    description="Artists asset",
    compute_kind="pandas"
)
def fetch_concerts(context: AssetExecutionContext):
    context.log.info("Fetching concerts for today")
    df = pd.DataFrame()
    return df


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
    io_manager_key="nb_io_manager"
)
