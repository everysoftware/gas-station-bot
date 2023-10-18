import datetime

from sqlalchemy import Column, BigInteger, VARCHAR, TIMESTAMP
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.schema import Identity

from .base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = Column(BigInteger, Identity(), unique=True)

    user_id: Mapped[int] = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    """Telegram User ID"""

    username: Mapped[str] = Column(VARCHAR(32), unique=True, nullable=False)

    reg_date: Mapped[datetime] = Column(TIMESTAMP, default=datetime.datetime.now(), nullable=False)

    def __str__(self) -> str:
        return str({'id': self.id})
