from sqlalchemy import Column, Integer, String, Boolean, Date, Numeric, ForeignKey, Enum
from sqlalchemy import declarative_base


db = create_engene("")
Base = declarative_base()

class usuario(Base):
    __tablename__ ="usuarios"
    id = Column("id", Integer, primarykey=True, autoincrement=True)
    email = Column ("email", String, nullable = False)

    def __init__(self)