import requests
import time

API_KEY = "user123"

for i in range(200):
    r = requests.get('http://localhost:8080/resource', headers={'X-API-Key': API_KEY})
    print(f"{i+1}: {r.status_code} - {r.json()}")
    time.sleep(0.3)  # ~200 requests/min
