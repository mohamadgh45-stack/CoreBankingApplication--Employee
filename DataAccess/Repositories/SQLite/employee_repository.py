import sqlite3
from Common.Entities.employee import Employee
from Common.Repositories.iemployee_repository import IEmployeeRepository


class SQLiteEmployeeRepository(IEmployeeRepository):
    def get_by_username_password(self, username: str, password: str) -> Employee:
        with sqlite3.connect("CoreBaningDB.db") as connection:
            cursor= connection.cursor()
            cursor.execute("Select...")

    def insert(self, employee: Employee):
        with sqlite3.connect("CoreBaningDB.db") as connection:
            cursor = connection.cursor()
            cursor.execute("Insert...")