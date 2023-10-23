from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Address(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    age: Mapped[int] = mapped_column(default=18)
    address: Mapped[str] = mapped_column()
    is_vip: Mapped[bool] = mapped_column(default=False)
    name: Mapped[str] = mapped_column()
    date: Mapped[datetime] = mapped_column()

    def __str__(self):
        return f"{self.name}, {self.age}, {self.address}, {self.is_vip}, {self.date}"

    def __kek__(self):
        return {"name": self.name, "is_vip": self.is_vip, "address": self.address, "age": self.age, "date": self.date}
