import requests
import sys
def enrich_ip(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "ip": ip_address,
            "city": data.get("city", "N/A"),
            "region": data.get("region", "N/A"),
            "country": data.get("country", "N/A"),
            "org": data.get("org", "N/A"),
            "hostname": data.get("hostname", "N/A")
        }
    except requests.RequestException as e:
        print(f"Error fetching data for IP {ip_address}: {e}")
        return {
            "ip": ip_address,
            "city": "N/A",
            "region": "N/A",
            "country": "N/A",
            "org": "N/A",
            "hostname": "N/A"
        }
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python ip_enrichment.py <ip_address>")
        sys.exit(1)

    ip_address = sys.argv[1]
    enriched_data = enrich_ip(ip_address)

    print("Enriched IP Information:")
    print(f"{enriched_data}")

if __name__ == "__main__":
    main()