from .noSQL_kit import NoSQLKit
from .JDBC_kit import JDBCKit
from .sr_kit import SrKit
import streamlit as st

class SingletonMeta(type):
    """Мета-клас для реалізації Singleton."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Створюємо і зберігаємо єдиний екземпляр
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class PersistKit(metaclass=SingletonMeta):
    """Singleton-клас для фабрики сховищ."""
    @staticmethod
    def get_persistence_kit(type_):
        if type_ == "nosql":
            return NoSQLKit()
        elif type_ == "jdbc":
            return JDBCKit()
        elif type_ == "sr":
            return SrKit()
        else:
            raise ValueError("Unsupported persistence type.")
