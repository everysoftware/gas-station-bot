from aiogram.fsm.state import StatesGroup, State


class MainGroup(StatesGroup):
    select_an_action = State()
    select_a_station = State()
