import os
from dotenv import load_dotenv
from Presentation.main_view import MainView
from BusinessLogic.user_business_logic import UserBusinessLogic
from DataAccess.Repositories.SQLServer.employee_repository import SQLServerEmployeeRepository

load_dotenv()

sql_server_host = os.getenv("SQLSERVER_HOST", ".")
sql_server_database = os.getenv("SQLSERVER_DATABASE")

repository = SQLServerEmployeeRepository(sql_server_host, sql_server_database)
user_business = UserBusinessLogic(repository)

MainView(user_business)
