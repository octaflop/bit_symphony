from dagster import Definitions, load_assets_from_modules, file_relative_path

from dagster_duckdb import DuckDBResource
from dagstermill import ConfigurableLocalOutputNotebookIOManager

from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={
        "motherduck": DuckDBResource(database="md:"),
        "nb_io_manager": ConfigurableLocalOutputNotebookIOManager(
            base_dir=file_relative_path(__file__, "notebooks/outputs")
        ),
    }
)
