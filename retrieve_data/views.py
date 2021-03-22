import json
import numpy as np
import pandas as pd


def parse_events(data):
    events = json.loads(data)
    df = create_event_count(events)
    df = multiply_by_constant(df, 0.1)
    return df


def create_event_count(events):
    df = pd.DataFrame(events)
    timestamps = [event['timestamp'] for event in events]
    distribution = np.arange(min(timestamps)-1, max(timestamps) + 3600, 3600)
    df_grouped = df.groupby([pd.cut(df["timestamp"], distribution), "event"]).size()
    df_grouped = df_grouped.unstack()
    return df_grouped


def multiply_by_constant(df, column,c):
    df[column+"_c"] = c * df[column]
    return df
