from aiogram import filters, Router, types, F
from aiogram.fsm.context import FSMContext

from fsm import MainGroup
from keyboards import get_main_kb, get_stations_kb
from .commands import BOT_COMMANDS_STR
from src.middlewares import DatabaseMd
from src.services import get_nearest_gas_station

main_router = Router(name='start')

main_router.message.middleware(DatabaseMd())


@main_router.message(filters.Command('start'))
async def start(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(
        '<b>Добро пожаловать в сервис поиска ближайших заправочных станций!</b>\n\n'
        'Выберите действие 👇',
        reply_markup=get_main_kb()
    )
    await state.set_state(MainGroup.select_an_action)


@main_router.message(F.location)
async def get_location(msg: types.Message, state: FSMContext) -> None:
    latitude = msg.location.latitude
    longitude = msg.location.longitude

    result = get_nearest_gas_station(latitude, longitude)
    await state.update_data(result=result)

    if result is None:
        await msg.answer('Заправки не найдены 😒')
        return

    await msg.answer(
        'Ближайшие заправочные станции',
        reply_markup=get_stations_kb(result)
    )
    await state.set_state(MainGroup.select_a_station)


@main_router.callback_query(F.data.startswith('show'), MainGroup.select_a_station)
async def show_station_info(callback: types.CallbackQuery, state: FSMContext):
    args = callback.data.split('_')
    try:
        station_id = int(args[1])
    except (IndexError, ValueError):
        pass
    else:
        user_data = await state.get_data()
        station_info = user_data['result'][station_id]
        meta = station_info['properties']['CompanyMetaData']
        name = meta['name']
        address = meta['address']

        ans = f'<b>{name}, {address}</b>\n\n'
        if 'Phones' in meta and meta['Phones']:
            ans += f'Тел.: {meta["Phones"][0]["formatted"]}\n'
        if 'Hours' in meta and meta['Hours']:
            ans += f'Режим работы: {meta["Hours"]["text"]}\n'
        if 'url' in meta and meta['Hours']:
            ans += f'Сайт: {meta["url"]}\n'

        await callback.message.answer(ans)
        await callback.message.answer_location(
            float(station_info['geometry']['coordinates'][1]),
            float(station_info['geometry']['coordinates'][0])
        )

    finally:
        await callback.answer()


@main_router.message(filters.Command('help'))
async def help_(msg: types.Message) -> None:
    await msg.answer('<b>Список команд</b>\n\n' + BOT_COMMANDS_STR)


@main_router.message(filters.Command('author'))
async def author(msg: types.Message) -> None:
    await msg.answer('Автор бота: @ivanstasevich 👨‍💻')
