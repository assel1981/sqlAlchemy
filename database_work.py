from sqlalchemy import create_engine, Integer, ForeignKey
from sqlalchemy.orm import as_declarative, declared_attr, mapped_column, Mapped, Session

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@as_declarative()
class AbstractModel():
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class UserModel(AbstractModel):
    __tablename__ = 'users'
    name: Mapped[str] =mapped_column()
    fullname: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column()



class AddressModel(AbstractModel):
    __tablename__ = 'Address'
    email: Mapped[str] =mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey(column='users.id'))


with Session(engine) as session:
    with session.begin():
        AddressModel.metadata.create_all(engine)
        user=UserModel(user_id=1, name='Jack', fullname='Jack Cow') #noqa
        session.add(user)










