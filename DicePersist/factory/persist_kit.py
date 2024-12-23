from .noSQL_kit import NoSQLKit
from .JDBC_kit import JDBCKit
from .sr_kit import SrKit
import streamlit as st

class PersistKit:
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
