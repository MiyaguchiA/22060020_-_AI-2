import requests

def get_all_breeds():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    if response.status_code == 200:
        return list(response.json()["message"].keys())
    return []
 
def get_random_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["message"]
    return None

def get_image_by_breed(breed):
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["message"]
    return None
