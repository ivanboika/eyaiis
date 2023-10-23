from sqlalchemy import create_engine, select, insert, update
from sqlalchemy.orm import Session
from models import Address, Base
from datetime import datetime

date_format = '%d.%m.%Y %H:%M'


class Controller:
    def __init__(self):
        self.engine = create_engine("sqlite:///foo.db", echo=True)
        Base.metadata.create_all(self.engine)

    def create_object(self, name, is_vip, address, age, time):
        with Session(self.engine) as session:
            time = datetime.strptime(time, date_format)
            session.execute(insert(Address), {"name": name, "is_vip": is_vip, "address": address, "age": age, "date": time})
            session.commit()

    def get_all_objects(self):
        data = []
        stmt = select(Address)
        with Session(self.engine) as session:
            for item in session.scalars(stmt):
                data.append(item)
        return data

    def delete_object(self, object):
        with Session(self.engine) as session:
            session.delete(object)
            session.commit()

    def edit_object(self, object):
        with Session(self.engine) as session:
            session.execute(update(Address).where(Address.id == object.id), object.__kek__())
            session.commit()
