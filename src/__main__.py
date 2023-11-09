import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from src.config import cfg
from src.db import create_async_engine, get_session_maker
from src.handlers import routers
from src.handlers.commands import BOT_COMMANDS


async def main() -> None:
    logging.basicConfig(level=cfg.logging_level, stream=sys.stdout)

    bot = Bot(cfg.bot.tg_token, parse_mode='HTML')
    await bot.set_my_commands(BOT_COMMANDS)

    engine = create_async_engine(cfg.db.build_connection_str())
    session_maker = get_session_maker(engine)

    dp = Dispatcher()

    for router in routers:
        dp.include_router(router)

    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
        session_maker=session_maker,
    )


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info('Bot stopped')
