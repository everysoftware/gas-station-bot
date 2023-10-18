from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Ближайшая заправка ⛽', request_location=True)],

        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


def get_stations_kb(features: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i, feature in enumerate(features):
        name = feature['properties']['CompanyMetaData']['name']
        address = feature['properties']['CompanyMetaData']['address']

        builder.add(InlineKeyboardButton(
            text=f'📍 {name}, {address}',
            callback_data=f'show_{i}',
        ))
    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)
