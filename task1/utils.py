from difflib import get_close_matches

def map_headers(csv_headers, target_fields):
    mapping = {}
    for header in csv_headers:
        match = get_close_matches(header.lower(), target_fields, n=1, cutoff=0.6)
        mapping[header] = match[0] if match else None
    return mapping
