import pathlib
from dataclasses import dataclass
from os import getenv

from sqlalchemy.engine import URL
from dotenv import load_dotenv


def setup_env() -> None:
    path = pathlib.Path(__file__).parent.parent
    dotenv_path = path.joinpath('.env')
    if dotenv_path.exists():
        load_dotenv(dotenv_path)


setup_env()


@dataclass(frozen=True)
class BotConfig:
    tg_token: str = getenv('TG_TOKEN')
    yandex_api_key: str = getenv('YANDEX_API_KEY')


@dataclass(frozen=True)
class DatabaseConfig:
    db: str = getenv('POSTGRES_DATABASE')
    username: str = getenv('POSTGRES_USERNAME', 'postgres')
    password: str = getenv('POSTGRES_PASSWORD', None)
    port: int = int(getenv('POSTGRES_PORT', 5432))
    host: str = getenv('POSTGRES_HOST', 'localhost')

    driver: str = 'asyncpg'
    database_system: str = 'postgresql'

    def build_connection_str(self) -> str:
        return URL.create(
            drivername=f'{self.database_system}+{self.driver}',
            username=self.username,
            database=self.db,
            password=self.password,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)


@dataclass(frozen=True)
class RedisConfig:
    db: str = getenv('REDIS_DATABASE', 1)
    username: str = getenv('REDIS_USERNAME', None)
    password: str = getenv('REDIS_PASSWORD', None)
    port: int = int(getenv('REDIS_PORT', 6379))
    host: str = getenv('REDIS_HOST', 'localhost')

    state_ttl: int = getenv('REDIS_TTL_STATE', None)
    data_ttl: int = getenv('REDIS_TTL_DATA', None)


@dataclass(frozen=True)
class Config:
    debug: bool = bool(getenv('DEBUG'))
    logging_level: int = getenv('LOGGING_LEVEL', 'INFO')

    bot: BotConfig = BotConfig()
    db: DatabaseConfig = DatabaseConfig()
    redis: RedisConfig = RedisConfig()


cfg = Config()
