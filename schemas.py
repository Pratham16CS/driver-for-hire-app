from pydantic import BaseModel,EmailStr
from enum import Enum
from typing import Optional
from datetime import datetime

#User Schema
# User Role
class UserRole(str,Enum):
    passenger = "passenger"
    driver = "driver"

# Base Schema (shared fields)

class UserBase(BaseModel):
    name:str
    email:EmailStr
    user_role:UserRole

class UserCreate(UserBase):
    password_hash:str

    class Config:
        orm_mode = True

class UserOut(UserBase):
    user_id:int

class UserLogin(BaseModel):
    email:EmailStr
    password:str

#RideRequest Schema
class RideStatus(str,Enum):
    Pending = "Pending"
    Accepted = "Accepted"

class RideRequestBase(BaseModel):
    pickup:str
    destination:str

#Create Schema (used when passenger submits ride)
class RideRequestCreate(RideRequestBase):
    pass  # No timestamps or IDs at creation

# used when driver accepts a ride
class RideRequestUpdate(BaseModel):
    ride_status:Optional[RideStatus]
    driver_id:Optional[int]
    accepted_at: Optional[datetime]=None

# Read Schema [used in response]
class RideRequestOut(RideRequestBase):
    ride_id:int
    ride_status:RideStatus
    created_at:datetime
    accepted_at: Optional[datetime] = None
    passenger_id:int
    driver_id:Optional[int] = None

    class Config:
        orm_mode = True 
 
class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    sub:Optional[str] = None

