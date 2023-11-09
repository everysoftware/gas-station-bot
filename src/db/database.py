from sqlalchemy.ext.asyncio import AsyncSession

from .repositories import UserRepo


class Database:
    session: AsyncSession
    user: UserRepo

    def __init__(
            self,
            session: AsyncSession,
            user: UserRepo = None,
    ):
        self.session = session
        self.user = user or UserRepo(session=session)
