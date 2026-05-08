import requests

 # Send GET request
response = requests.get(
    url, params=params, headers=headers, timeout=10
)

return response.json()
