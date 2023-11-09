import requests

from src.config import cfg


def get_nearest_gas_station(latitude: float, longitude: float) -> list | None:
    url = f'https://search-maps.yandex.ru/v1/?apikey={cfg.bot.yandex_api_key}&' \
          f'text=заправка&ll={longitude},{latitude}&type=biz&lang=ru_RU'
    response = requests.get(url)
    data = response.json()

    if 'features' in data and data['features']:
        return data['features']
    else:
        return None
