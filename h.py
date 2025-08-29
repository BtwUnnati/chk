import requests

BHARATPE_MERCHANT_ID = "56433931"
BHARATPE_API_KEY = "bcc467040e43979777b03881bf2916"

url = f"https://api.bharatpe.in/merchant/{BHARATPE_MERCHANT_ID}/profile"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {BHARATPE_API_KEY}"
}

resp = requests.get(url, headers=headers)

print(resp.status_code)
print(resp.text)
