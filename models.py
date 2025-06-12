from sqlalchemy import Column,Integer,String,Enum,ForeignKey,TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String,unique=True,index=True)
    password_hash = Column(String)
    user_role = Column(Enum("passenger","driver",name="user_role"))



class RideRequest(Base):
    __tablename__ = 'ride_requests'
    ride_id = Column(Integer,primary_key=True)
    pickup = Column(String,nullable = False)
    destination = Column(String,nullable = False)
    ride_status = Column(Enum("Pending","Accepted",name="ride_status"))
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    accepted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    passenger_id = Column(Integer,ForeignKey("users.user_id"),nullable=False)
    driver_id = Column(Integer,ForeignKey("users.user_id"),nullable=True)
    passenger = relationship("User",foreign_keys=[passenger_id],backref="passenger_rides")
    driver = relationship("User",foreign_keys=[driver_id],backref="driver_riders")

