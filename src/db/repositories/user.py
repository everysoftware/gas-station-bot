from sqlalchemy.ext.asyncio import AsyncSession

from .repo import Repository
from ..models import User


class UserRepo(Repository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=User, session=session)

    def new(
            self,
            user_id: int,
            username: str,
    ) -> User:
        new_user = User(
            user_id=user_id,
            username=username,
        )
        self.session.add(new_user)
        return new_user
