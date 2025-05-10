import json, time
from plugin_loader import load_parsers
from ledger_schema import EXPECTED_FIELDS
from utils import map_headers

def reconcile(file_path):
    start = time.time()
    
    parsers = load_parsers()
    parser = parsers['comma' if ',' in open(file_path).readline() else 'semicolon']
    records = parser.parse(file_path)
    
    header_map = map_headers(records[0].keys(), EXPECTED_FIELDS)

    matched, mismatched, missing = [], [], []
    
    for row in records:
        mapped = {target: row[src] for src, target in header_map.items() if target}
        try:
            amount = float(mapped.get('amount', 0))
            if abs(amount) <= 0.01:
                matched.append(mapped)
            else:
                mismatched.append(mapped)
        except:
            missing.append(row)

    with open('report.json', 'w') as f:
        json.dump({
            "matched": matched[:5],
            "mismatched": mismatched[:5],
            "missing": missing[:5]
        }, f, indent=2)

    with open('perf.log', 'w') as f:
        f.write(f"Processed {len(records)} records in {time.time() - start:.2f}s\n")
