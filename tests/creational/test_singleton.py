import pytest

from patterns.creational.singleton import Singleton, AppConfig


@pytest.fixture(autouse=True)
def reset_singleton():
    """Reset singleton instances before each test to ensure test isolation."""
    Singleton._instance = None
    AppConfig._instance = None
    AppConfig._initialized = False
    yield
    Singleton._instance = None
    AppConfig._instance = None
    AppConfig._initialized = False


# --- Singleton Base Tests ---


def test_singleton_same_instance():
    s1 = Singleton()
    s2 = Singleton()
    assert s1 is s2


def test_singleton_only_one_instance():
    instances = [Singleton() for _ in range(10)]
    assert all(inst is instances[0] for inst in instances)


# --- AppConfig Tests ---


def test_appconfig_is_singleton():
    config1 = AppConfig()
    config2 = AppConfig()
    assert config1 is config2


def test_appconfig_default_settings():
    config = AppConfig()
    assert config.get("database_url") == "localhost:5432"
    assert config.get("debug") is False
    assert config.get("language") == "en"


def test_appconfig_set_and_get():
    config = AppConfig()
    config.set("language", "ar")
    assert config.get("language") == "ar"


def test_appconfig_shared_state():
    config1 = AppConfig()
    config2 = AppConfig()
    config1.set("theme", "dark")
    assert config2.get("theme") == "dark"


def test_appconfig_missing_key_returns_none():
    config = AppConfig()
    assert config.get("nonexistent_key") is None


def test_appconfig_initialized_only_once():
    config1 = AppConfig()
    config1.set("language", "ar")
    config2 = AppConfig()
    assert config2.get("language") == "ar"  # Not reset to "en"


def test_appconfig_add_new_setting():
    config = AppConfig()
    config.set("max_connections", 100)
    assert config.get("max_connections") == 100


def test_appconfig_overwrite_setting():
    config = AppConfig()
    assert config.get("debug") is False
    config.set("debug", True)
    assert config.get("debug") is True