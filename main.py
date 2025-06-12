from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routes import user, ride

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Driver-for-Hire Aggregator App")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include API Routes
app.include_router(user.router, tags=["User"], prefix="/users")
app.include_router(ride.router, tags=["Ride"], prefix="/rides")

@app.get("/")
def root():
    return {"Message":"This is a Driver-for-Hire Aggregator App API"}
