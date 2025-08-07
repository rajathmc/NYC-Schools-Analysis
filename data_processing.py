import csv
from typing import List, Dict, Optional

def load_sat_results(path: str) -> List[Dict[str, str]]:
    """Load SAT results data from a CSV file.

    Returns a list of rows where each row is a dict mapping column names to values."""
    # ``utf-8-sig`` handles files that start with a UTF-8 BOM, which some of the
    # project data files include.
    with open(path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)

def add_total_score(rows: List[Dict[str, str]]) -> List[Dict[str, Optional[int]]]:
    """Add a total SAT score to each row.

    The total is the sum of the reading, math, and writing scores. Non-numeric values
    result in a total of ``None``."""
    for row in rows:
        try:
            total = (
                int(row['SAT Critical Reading Avg. Score'])
                + int(row['SAT Math Avg. Score'])
                + int(row['SAT Writing Avg. Score'])
            )
        except (ValueError, KeyError):
            total = None
        row['sat_total'] = total
    return rows
