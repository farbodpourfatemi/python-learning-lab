"""Read current weather using an OpenWeather API key from the environment."""
import os
import requests


def get_temperature(city: str, api_key: str) -> tuple[float, str]:
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": api_key, "units": "metric"},
        timeout=15,
    )
    response.raise_for_status()
    data = response.json()
    return float(data["main"]["temp"]), data.get("name", city)


def main() -> None:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Set OPENWEATHER_API_KEY in your environment before running this script.")
        return
    city = input("City: ").strip()
    if not city:
        print("City must not be empty.")
        return
    try:
        temperature, name = get_temperature(city, api_key)
        print(f"{name}: {temperature:.1f}°C")
    except (requests.RequestException, KeyError, ValueError) as exc:
        print(f"Weather lookup failed: {type(exc).__name__}")


if __name__ == "__main__":
    main()
