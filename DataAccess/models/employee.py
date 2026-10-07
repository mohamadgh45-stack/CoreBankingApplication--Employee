from DataAccess.models.base import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class EmployeeModel(Base):
    __tablename__ = "Employee"


    id: Mapped[int] = mapped_column("Id", Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column("FirstName", String(100), nullable=False)
    last_name: Mapped[str] = mapped_column("LastName", String(100), nullable=False)
    username: Mapped[str] = mapped_column("Username", String(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column("Password", String(64), nullable=False)
    mobile: Mapped[str] = mapped_column("Mobile", String(20), nullable=True)
    employee_status_id: Mapped[int] = mapped_column("EmployeeStatusId", Integer, nullable=False, default=1)