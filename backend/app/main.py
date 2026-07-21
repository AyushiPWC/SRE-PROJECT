from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine

from app.api.auth_api import router as auth_router
from app.api.user_api import router as user_router
from app.api.hotel_api import router as hotel_router
from app.api.booking_api import router as booking_router
from app.api.dashboard_api import router as dashboard_router


API_PREFIX = "/api/v1"


app = FastAPI(
    title="Hotel Booking API",
    description="Hotel Booking Application using FastAPI and PostgreSQL",
    version="1.0.0"
)


# ==========================================
# Create Database Tables
# ==========================================

Base.metadata.create_all(
    bind=engine
)


# ==========================================
# CORS Configuration
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# ==========================================
# Register API Routers
# ==========================================

app.include_router(
    auth_router,
    prefix=API_PREFIX
)

app.include_router(
    user_router,
    prefix=API_PREFIX
)

app.include_router(
    hotel_router,
    prefix=API_PREFIX
)

app.include_router(
    booking_router,
    prefix=API_PREFIX
)

app.include_router(
    dashboard_router,
    prefix=API_PREFIX
)


# ==========================================
# Root Endpoint
# ==========================================

@app.get(
    "/",
    tags=["Health"]
)
def home():

    return {
        "message": "Hotel Booking API is running",
        "version": "1.0.0",
        "phase": "Phase 6 - Dashboard"
    }


# ==========================================
# Health Check
# ==========================================

@app.get(
    "/health",
    tags=["Health"]
)
def health_check():

    return {
        "status": "healthy"
    }