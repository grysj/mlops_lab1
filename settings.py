# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    HASLO: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        # implement me!
        # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
        if value in ("dev", "test", "prod"):
            return value
        else:
            raise ValueError("ENVIRONMENT must be one of: dev, test, prod")

    @field_validator("HASLO")
    @classmethod
    def validate_haslo(cls, value):
        if value:
            return value
        else:
            raise ValueError("HASLO must be not empty")
