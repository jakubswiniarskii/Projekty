import requests

API_URL_CURRENT = "https://api.openweathermap.org/data/2.5/weather"
API_URL_FORECAST = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "e25bbb5ddf52584b453bb6a6c3fbc6c1"


def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
    }

    try:
        # Pogoda na teraz
        response = requests.get(API_URL_CURRENT, params=params)
        response.raise_for_status()
        data = response.json()

        print("\nAktualna pogoda:")
        print("=" * 30)
        print(f"Miasto: {data['name']}")
        print(f"Temperatura: {data['main']['temp']}°C")
        print(f"Opis: {data['weather'][0]['description'].capitalize()}")
        print("=" * 30)

        # Prognoza co 3 godziny na następne 5 dni
        response_forecast = requests.get(API_URL_FORECAST, params=params)
        response_forecast.raise_for_status()
        data_forecast = response_forecast.json()

        print("\nPrognoza co 3 godziny na następne 5 dni:")
        print("=" * 50)
        for entry in data_forecast["list"][:40]:  # 40 prognoz = 5 dni co 3 godziny
            date_time = entry["dt_txt"]
            temp = entry["main"]["temp"]
            description = entry["weather"][0]["description"].capitalize()
            print(f"{date_time}: {temp}°C, {description}")
        print("=" * 50)

    except requests.exceptions.RequestException as e:
        print(f"\nWystąpił błąd podczas komunikacji z API: {e}")
    except KeyError:
        print("\nNiepoprawna odpowiedź od serwera. Sprawdź poprawność nazwy miasta lub klucza API.")

while True:
    if __name__ == "__main__":
        city = input("Podaj nazwę miasta: ")
        get_weather(city)