import requests
from  django.core.cache import cache

def get_currencies():
    cached = cache.get("currencies")
    if  cached:
        return cached
    response = requests.get("https://forecast.ge/api/v1/get-currencies")
    data = response.json()
    cache.set("currencies", data, timeout=60*15)
    return data
