import requests

def DadJokes():
    url = "https://icanhazdadjoke.com/"

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        JokeData = response.json()
        print(JokeData['joke'])
    else:
        print(f"Failed to load joke, error code is {response.status_code}")

print(DadJokes())