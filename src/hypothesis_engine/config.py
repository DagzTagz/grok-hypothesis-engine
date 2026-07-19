"""Runtime configuration loaded from environment (never hardcode secrets)."""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings.

    Values come from environment variables and optional `.env` file.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    xai_api_key: str | None = Field(default=None, validation_alias="XAI_API_KEY")
    xai_base_url: str = Field(default="https://api.x.ai/v1", validation_alias="XAI_BASE_URL")
    xai_model: str = Field(default="grok-4.5", validation_alias="XAI_MODEL")

    def require_api_key(self) -> str:
        if not self.xai_api_key or not self.xai_api_key.strip():
            raise RuntimeError(
                "Missing XAI_API_KEY. Copy .env.example to .env and set your key, "
                "or export XAI_API_KEY. See getting-started.md."
            )
        return self.xai_api_key.strip()


def get_settings() -> Settings:
    return Settings()
