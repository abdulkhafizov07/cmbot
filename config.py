from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    token: str = Field()

    web_server_host: str = Field("127.0.0.1")
    web_server_port: int = Field(8080)

    webhook_path: str = Field("/webhook")
    webhook_secret: str = Field()
    base_webhook_url: str = Field()

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="cmbot_", extra="ignore"
    )


settings = Settings()  # type: ignore
