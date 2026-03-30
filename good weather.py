import requests


def get_weather(location):
    url = f"http://wttr.in/{location}"
    params = {
        "M": "",
        "n": "",
        "q": "",
        "T": "",
        "lang": "ru"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def main():
    locations = ["london", "svo", "cherepovets"]
    for location in locations:
        print(get_weather(location))


if __name__ == "__main__":
    main()
