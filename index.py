import requests
import csv
import time
import json

def get_google_position(keyword, domain, api_key):
    params = {
        "engine": "google",
        "q": keyword,
        "api_key": api_key,
        "num": 100,
        "hl": "fr",
        "gl": "fr",
        "google_domain": "google.fr"
    }
    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()

    for i, result in enumerate(results.get("organic_results", []), 1):
        if domain in result.get("link", ""):
            return i, result.get("link")
    return None, None

# Configuration (voir readme.md)
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

keywords = config["keywords"]
domain = config["domain"]
csv_filename = config["csv_filename"]
api_key = config["api_key"]

# Ecriture des résultats dans un fichier CSV
with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Mot-clé", "Position", "URL"])

    for keyword in keywords:
        print(f"Recherche : {keyword}")
        position, url = get_google_position(keyword, domain, api_key)
        writer.writerow([keyword, position or "Non trouvé", url or "—"])
        time.sleep(2)

print(f"Les résultats sont enregistrés dans le fichier {csv_filename}")