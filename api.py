import requests

def get_coffee():
    response=requests.get("https://coffee.alexflipnote.dev/random.json")
    info=response.json()
    return info['file']

