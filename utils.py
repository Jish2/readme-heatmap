from datetime import datetime
from typing import List


def get_days_since_last_year(unix_timestamp) -> int:
    date = datetime.fromtimestamp(int(unix_timestamp))
    # day1 = datetime(date.year, 1, 1)
    date_1_year_ago = date.now().replace(year=date.year - 1)
    difference = date - date_1_year_ago
    return difference.days


def get_quartiles(timestamp_map: dict[str, int]):
    values = sorted(list(timestamp_map.values()))
    return [
        values[0],
        values[len(values) // 4],
        values[len(values) // 2],
        values[3 * len(values) // 4],
        values[-1],
    ]


def get_date_map_from_timestamp_map(timestamp_map: dict[str, int]) -> dict[int, int]:
    return {get_days_since_last_year(k): v for k, v in timestamp_map.items()}


def get_heat(heat: int, quartiles: List[int]):
    # eg [0, 5, 10, 15, 20]
    for i, quartile in enumerate(quartiles):
        if heat < quartile:
            return i
    return len(quartiles) - 1
