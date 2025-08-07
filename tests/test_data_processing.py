import sys
from pathlib import Path

# Ensure the repository root is on the import path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from data_processing import load_sat_results, add_total_score


def test_load_sat_results():
    rows = load_sat_results('data/sat_results.csv')
    assert len(rows) > 0
    # First row should correspond to DBN 01M292
    assert rows[0]['DBN'] == '01M292'


def test_add_total_score():
    rows = load_sat_results('data/sat_results.csv')
    rows = add_total_score(rows)
    # Find the row for DBN 01M292 and ensure total score is correct
    row = next(r for r in rows if r['DBN'] == '01M292')
    assert row['sat_total'] == 355 + 404 + 363
