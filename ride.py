from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from typing import Optional,List
from datetime import datetime,timedelta
from app import models,schemas,crud,auth
from app.database import get_db

router = APIRouter()

# Passenger creates a ride request
@router.post("/",response_model=schemas.RideRequestOut)
def create_ride(request:schemas.RideRequestCreate,db:Session=Depends(get_db),current_user:models.User=Depends(auth.get_current_user)):
    if current_user.user_role != "passenger":
        raise HTTPException(status_code=403,detail="Only passengers can request rides")
    return crud.create_ride(db=db,pass_id=current_user.user_id,ride=request)

# Passenger views their own rides
@router.get("/my",response_model=List[schemas.RideRequestOut])
def get_my_rides(db:Session=Depends(get_db),current_user:models.User=Depends(auth.get_current_user)):
    if current_user.user_role != 'passenger':
        raise HTTPException(status_code=403,detail="Only passengers can view their rides")
    return crud.get_passenger_rides(db=db,passenger_id=current_user.user_id)

# Passenger view current "pending" ride request
@router.get("/my/current",response_model=List[schemas.RideRequestOut])
def get_current_ride(db:Session=Depends(get_db),current_user:models.User=Depends(auth.get_current_user)):
    if current_user.user_role != 'passenger':
        raise HTTPException(status_code=403,detail="Only passengers can current ride.")
    return crud.get_current_ride_for_passenger(db=db,passenger_id=current_user.user_id)

# Passenger view "accepted" ride request
@router.get("/my/pastrides",response_model=List[schemas.RideRequestOut])
def get_current_ride(db:Session=Depends(get_db),current_user:models.User=Depends(auth.get_current_user)):
    if current_user.user_role != 'passenger':
        raise HTTPException(status_code=403,detail="Only passengers can current ride.")
    return crud.get_accepted_rides_passenger(db=db,passenger_id=current_user.user_id)

# Driver views all pending ride requests
@router.get("/pending",response_model=List[schemas.RideRequestOut])
def get_pending_rides(db:Session=Depends(get_db),current_user:models.User=Depends(auth.get_current_user)):
    if current_user.user_role != "driver":
        raise HTTPException(status_code=403,detail="Only drivers can view pending rides.")
    return crud.get_pending_rides(db=db)

# Driver accepts a ride
@router.put("/{ride_id}/accept",response_model=schemas.RideRequestOut)
def accept_ride(ride_id:int,db:Session=Depends(get_db),current_user:models.User=Depends(auth.get_current_user)):
    if current_user.user_role != 'driver':
        raise HTTPException(status_code=403,detail="Passenger cannot accept a ride.")
    utc_now = datetime.utcnow()
    ist_now = utc_now + timedelta(hours=5, minutes=30)
    return crud.accept_ride(db=db,ride_id=ride_id,driver_id=current_user.user_id,accepted_at=ist_now)

# Driver views rides they accepted
@router.get("/my/accepted",response_model=List[schemas.RideRequestOut])
def get_accepted_rides(db:Session=Depends(get_db),current_user:models.User=Depends(auth.get_current_user)):
    if current_user.user_role != 'driver':
        raise HTTPException(status_code=403,detail='Only drivers can view their rides')
    return crud.get_driver_rides(db=db,driver_id=current_user.user_id)