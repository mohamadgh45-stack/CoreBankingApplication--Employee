from sqlalchemy import select

from Common.Entities.employee import Employee
from Common.Repositories.iemployee_repository import IEmployeeRepository
from DataAccess.config.database import create_session
from DataAccess.models.employee import EmployeeModel


class SQLAlchemyEmployeeRepository(IEmployeeRepository):


    def get_by_username_password(self, username: str, password: str) -> Employee:
        with create_session() as session:
            statement = select(EmployeeModel).where(
                EmployeeModel.username == username,
                EmployeeModel.password == password,
            )
            model = session.scalars(statement).first()

            if model is None:
                return None

            return self._to_entity(model)

    def insert(self, employee: Employee):
        with create_session() as session:
            model = EmployeeModel(
                first_name=employee.first_name,
                last_name=employee.last_name,
                username=employee.username,
                password=employee.password,
                mobile=employee.mobile,
                employee_status_id=employee.status.value,
            )
            session.add(model)

    @staticmethod
    def _to_entity(model: EmployeeModel) -> Employee:
        # BusinessLogic works with the plain Employee entity, not the
        # SQLAlchemy model - keeps the ORM detail inside DataAccess only.
        return Employee(
            model.id,
            model.first_name,
            model.last_name,
            model.username,
            model.password,
            model.mobile,
            model.employee_status_id,
        )
