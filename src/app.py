import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import routers
from config import cfg
from handlers.commands import BOT_COMMANDS
from db import create_async_engine, get_session_maker


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
