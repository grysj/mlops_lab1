from main import export_envs
from settings import Settings


export_envs("test")
settings = Settings()


def test_read_settings():
    # settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "app_test"
    assert settings.HASLO != ""
