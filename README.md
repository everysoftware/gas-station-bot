# Заправки

## Краткое описание
Быстрый поиск ближайшей заправочной станции ⛽️


<img src="https://github.com/everysoftware/gas-station-bot/assets/22497421/831a42e8-e34d-4cb5-9f52-7f978b4f4e2a" width="300" />  
<img src="https://github.com/everysoftware/gas-station-bot/assets/22497421/5b4a9e59-bd43-418c-a60d-c2c8aafd0db6" width="300" />  


## Начало работы

1. Запустите бота, поделитесь местоположением. Бот найдет ближайшие к вам заправки.   
2. Выберите интересующую вам заправку и получите информацию о том, как до неё добраться.  
3. Готово!

## Стек технологий

Python3, Aiogram3, SQLAlchemy2, Alembic, Yandex Maps API  

## Сборка

1. Установите зависимости ```pip install -r requirements.txt```
2. Задайте переменные окружения с помощью файла ```.env```
```
DEBUG=0
LOGGING_LEVEL="INFO"
TG_TOKEN=
POSTGRES_DATABASE=
POSTGRES_HOST=
POSTGRES_PASSWORD=
POSTGRES_PORT="5432"
POSTGRES_USERNAME=
YANDEX_API_KEY=
```
3. Примените миграции: ```alembic upgrade head``` или ```make migrate```
4. Запустите бота: ```python -m src```
