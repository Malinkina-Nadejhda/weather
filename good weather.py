import requests


def weather():
    locations = {
        "london": "london?MnqT",
        "sheremetyevo": "svo?MnqT",
        "cherepovets": "череповец?MnqT&lang=ru"
    }

    for location in locations.values():
        url = f"http://wttr.in/{location}"
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)


def main():
    weather()


if __name__ == "__main__":
    main()

