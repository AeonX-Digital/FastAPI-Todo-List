from sqlalchemy import Boolean, Column, Integer, String
from database import Base
from database import Base


class todo_list(Base):

    __tablename__="Todo_List"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    title = Column(String(50),index=True, nullable=False)
    description = Column(String(255), index=True, nullable=False)
    
