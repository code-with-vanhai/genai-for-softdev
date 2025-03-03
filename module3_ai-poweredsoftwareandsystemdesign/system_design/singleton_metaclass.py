class SingletonMeta(type):
    """
    Metaclass to ensure only one instance of a class exists.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppConfig(metaclass=SingletonMeta):
    """
    Application Configuration Singleton.
    """
    def __init__(self):
        self._config = {}

    def set(self, key, value):
        """Set a configuration value."""
        self._config[key] = value

    def get(self, key, default=None):
        """Get a configuration value."""
        return self._config.get(key, default)

    def show_all(self):
        """Display all configuration values."""
        return self._config


# Usage Example
config1 = AppConfig()
config1.set("database_url", "mysql://localhost:3306/mydb")
config1.set("debug", True)

config2 = AppConfig()
print(config2.get("database_url"))  # Output: mysql://localhost:3306/mydb
print(config2.get("debug"))  # Output: True

# Check if both instances are the same
print(config1 is config2)  # Output: True (Singleton behavior)

# Display all configurations
print(config1.show_all())  # Output: {'database_url': 'mysql://localhost:3306/mydb', 'debug': True}
