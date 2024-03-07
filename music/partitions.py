from dagster import DailyPartitionsDefinition


daily_events = DailyPartitionsDefinition(start_date='2024-03-01')