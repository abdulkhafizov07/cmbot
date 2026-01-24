from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    token: str = Field()

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="cmbot_", extra="ignore"
    )


settings = Settings()  # type: ignore
