from datetime import datetime

import pandas as pd
from dagster import (
    MetadataValue,
    asset,
    AssetExecutionContext, file_relative_path, AssetIn,
)
from dagstermill import define_dagstermill_asset


@asset(
    group_name="seer_sync_space_insights",
    description="Cleanup old, deleted spaces as partitions",
    compute_kind="pandas"
)
def clean_inactive_space_partitions(context: AssetExecutionContext):
    context.log.info("Fetching concerts for today")
    df = pd.DataFrame()
    return df


# # Uncomment to debug, note this will slow down downstream jobs when enabled
space_insights_playground = define_dagstermill_asset(
    name="space_insights_playground",
    notebook_path=file_relative_path(
        __file__,
        "../notebooks/inputs/music_events.ipynb"
    ),
    group_name="seer_sync_space_insights",
    description="An enriched, space-by-space exploration of documents in a space.",
    ins={
        "space_df": AssetIn("space_df"),

    },
    io_manager_key="nb_io_manager"
)
