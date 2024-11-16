import requests

PROXY = "http://127.0.0.1:8081"  # Burp Suite's proxy address
proxies = {
    "http": PROXY,
    "https": PROXY,  # Optional if HTTPS traffic is used
}

response = requests.post(
    "http://127.0.0.1:5000/play", 
    json={"username": "henry", "bet": 50, "w": [1, 1, 100]},
    proxies=proxies  # Route traffic through Burp Suite
)
print(response.json())
