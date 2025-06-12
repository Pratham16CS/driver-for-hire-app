from sqlalchemy.orm import Session
from .models import User,RideRequest
from .schemas import UserCreate,RideRequestCreate
from typing import Optional,List
from datetime import datetime

# User CRUD

def get_user_by_email(db:Session,email:str) -> Optional[User]:
    return db.query(User).filter(User.email==email).first()

def user_by_id(db:Session,id:int) -> Optional[User]:
    return db.query(User).filter(User.user_id==id).first()

def create_user(db:Session,user:UserCreate) -> User:
    db_user = User(
        name = user.name,
        email = user.email,
        password_hash = user.password_hash,
        user_role = user.user_role.value
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Ride Request CRUD
def create_ride(db:Session,pass_id:int,ride:RideRequestCreate) -> RideRequest:
    db_ride = RideRequest(
        pickup = ride.pickup,
        destination = ride.destination,
        ride_status = "Pending",
        passenger_id = pass_id
    )
    db.add(db_ride)
    db.commit()
    db.refresh(db_ride)
    return db_ride

def get_passenger_rides(db:Session,passenger_id:int)->List[RideRequest]:
    return db.query(RideRequest).filter(RideRequest.passenger_id==passenger_id).all()

def get_driver_rides(db:Session,driver_id:int) -> List[RideRequest]:
    return db.query(RideRequest).filter(RideRequest.driver_id==driver_id).all()

def get_pending_rides(db:Session)->List[RideRequest]:
    return db.query(RideRequest).filter(RideRequest.ride_status=='Pending').all()

def accept_ride(db:Session,ride_id:int,driver_id:int,accepted_at:datetime) -> Optional[RideRequest]:
    ride = db.query(RideRequest).filter(RideRequest.ride_id == ride_id).first()
    if ride and ride.ride_status == 'Pending':
        ride.ride_status = "Accepted"
        ride.driver_id = driver_id
        ride.accepted_at = accepted_at
        db.commit()
        db.refresh(ride)
        return ride
    return None

def get_ride_by_id(db:Session,ride_id:int) -> Optional[RideRequest]:
    return db.query(RideRequest).filter(RideRequest.ride_id==ride_id).first()

def get_current_ride_for_passenger(db:Session,passenger_id:int) -> Optional[RideRequest]:
    return (
        db.query(RideRequest).filter(
            RideRequest.passenger_id == passenger_id,
            RideRequest.ride_status.in_(["Pending"])
        )
        .order_by(RideRequest.created_at.desc()).all()
    )

def get_accepted_rides_passenger(db:Session,passenger_id:int)-> Optional[RideRequest]:
    return (
        db.query(RideRequest).filter(
            RideRequest.passenger_id == passenger_id,
            RideRequest.ride_status.in_(["Accepted"])
        )
        .order_by(RideRequest.created_at.desc()).all()
    )

def get_driver_rides(db:Session,driver_id:int)->List[RideRequest]:
    return db.query(RideRequest).filter(RideRequest.driver_id==driver_id).all()
