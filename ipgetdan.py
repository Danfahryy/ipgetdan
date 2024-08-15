import requests

def get_ip_from_email(email):
    # API Key untuk Email-to-IP service (sebagai contoh, kita akan menggunakan placeholder URL dan key)
    # Anda perlu mengganti URL dan key ini dengan layanan yang valid jika tersedia
    email_to_ip_api_url = "https://api.email-to-ip.com/v1/get-ip"
    params = {
        "email": email,
        "apikey": "77e3ce23547d427e9a9653bd4d35fcc9"  # Ganti dengan API Key yang valid
    }

    response = requests.get(email_to_ip_api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        ip_address = data.get('ip_address')
        return ip_address
    else:
        print("Error fetching IP from email")
        return None

def get_geolocation(ip_address):
    api_key = "77e3ce23547d427e9a9653bd4d35fcc9"  # Ganti dengan API Key yang valid dari ipgeolocation.io atau layanan serupa
    ip_geolocation_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}"

    response = requests.get(ip_geolocation_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching geolocation data")
        return None

def main():
    email = input("Enter the email address to lookup: ")
    ip_address = get_ip_from_email(email)

    if ip_address:
        print(f"IP Address: {ip_address}")
        geolocation_data = get_geolocation(ip_address)
        
        if geolocation_data:
            print("Geolocation Data:")
            print(f"Country: {geolocation_data.get('country_name')}")
            print(f"State: {geolocation_data.get('state_prov')}")
            print(f"City: {geolocation_data.get('city')}")
            print(f"Latitude: {geolocation_data.get('latitude')}")
            print(f"Longitude: {geolocation_data.get('longitude')}")
        else:
            print("Failed to retrieve geolocation data.")
    else:
        print("Failed to retrieve IP address.")

if __name__ == "__main__":
    main()
