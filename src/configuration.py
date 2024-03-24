import logging
import os
from dataclasses import dataclass
from dotenv import load_dotenv

from sqlalchemy.engine import URL

load_dotenv()


@dataclass
class DatabaseConfig:
    """Database connection variables."""

    name: str | None = os.environ.get('POSTGRES_DATABASE')
    user: str | None = os.environ.get('POSTGRES_USER')
    passwd: str | None = os.environ.get('POSTGRES_PASSWORD', None)
    port: int = int(os.environ.get('POSTGRES_PORT', 5432))
    host: str = os.environ.get('POSTGRES_HOST', 'db')
    # host: str = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    driver: str = 'asyncpg'
    database_system: str = 'postgresql'

    def build_connection_str(self) -> str:
        """This function build a connection string."""
        return URL.create(
            drivername=f'{self.database_system}+{self.driver}',
            username=self.user,
            database=self.name,
            password=self.passwd,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)


@dataclass
class RedisConfig:
    """Redis connection variables."""

    db: int = int(os.environ.get('REDIS_DATABASE', 1))
    """ Redis Database ID """
    host: str = os.environ.get('REDIS_HOST', 'redis')
    port: int = int(os.environ.get('REDIS_PORT', 6379))
    passwd: str | None = os.environ.get('REDIS_PASSWORD')
    username: str | None = os.environ.get('REDIS_USERNAME')
    state_ttl: int | None = os.environ.get('REDIS_TTL_STATE', None)
    data_ttl: int | None = os.environ.get('REDIS_TTL_DATA', None)


@dataclass
class BotConfig:
    """Bot configuration."""

    token: str = os.environ.get("BOT_TOKEN")


@dataclass
class Configuration:
    """All in one configuration's class."""

    debug = bool(os.environ.get('DEBUG'))
    logging_level = int(os.environ.get('LOGGING_LEVEL', logging.INFO))

    db = DatabaseConfig()
    redis = RedisConfig()
    bot = BotConfig()


conf = Configuration()
