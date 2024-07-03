from aiogram import Bot
from aiogram.enums import ParseMode
from pydantic_settings import BaseSettings
from redis.asyncio import Redis


class Secrets(BaseSettings):
    token: str
    admin_id: int
    openai_key: str
    openai_base_url: str
    redis_host: str
    delay: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


secrets = Secrets()

redis_conn = Redis(host=secrets.redis_host)

bot = Bot(token=secrets.token, parse_mode=ParseMode.MARKDOWN)