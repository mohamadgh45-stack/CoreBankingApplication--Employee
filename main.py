from Presentation.main_view import MainView
from BusinessLogic.user_business_logic import UserBusinessLogic
from DataAccess.Repositories.SQLAlchemy.employee_repository import SQLAlchemyEmployeeRepository
from DataAccess.config.database import engine
from DataAccess.models.base import Base


Base.metadata.create_all(engine)

repository = SQLAlchemyEmployeeRepository()
user_business = UserBusinessLogic(repository)

MainView(user_business)
