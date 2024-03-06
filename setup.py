from setuptools import find_packages, setup

setup(
    name="music",
    packages=find_packages(exclude=["music_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagstermill",
        "httpx",
        "dagster-duckdb",
        "duckdb-engine==0.9.2",  # pinned for motherduck
        "dagster-postgres",
        "beautifulsoup4",
        "geopandas",
        "seaborn"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
