import requests

response = requests.get(
    "http://127.0.0.1:5000/analyze",
    params={"mu": 0.5, "sigma": 0.2, "X": 0.9}
)

print(response.json())