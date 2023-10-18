from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from sqlalchemy.orm import sessionmaker

from db.database import Database


class DatabaseMd(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
            ) -> Any:
        session_maker: sessionmaker = data['session_maker']
        async with session_maker() as session:
            db = Database(session)
            data['db'] = db
            async with db.session.begin():
                user = await db.user.get(event.from_user.id)
                if user is None:
                    db.user.new(
                        event.from_user.id,
                        event.from_user.username if event.from_user.username is not None
                        else '',
                    )
            return await handler(event, data)
