from sqlalchemy import Boolean, Column, Integer, String
from database import Base
from database import Base
# from sqlalchemy.orm import relationship



class todo_list(Base):

    __tablename__="Todo_List"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    title = Column(String(50),index=True, nullable=False)
    description = Column(String(255), index=True, nullable=False)
    
class log_in(Base):


    __tablename__ = "log_in"

    email = Column(String(50),index=True, nullable=False,primary_key=True)
    password = Column (String(50),index=True, nullable=False)


# class to_do(Base):

#     __tablename__ = "to_do"

#     id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
#     work_topic = Column(String(50), nullable=False,primary_key=True)
#     working_hr = Column(float(50), nullable=False,primary_key=True)

#     user = relationship("AdminUserModel", backref="products")

  
