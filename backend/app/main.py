from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from app.core.database import Base, engine

# Import every model before Base.metadata.create_all()
# These imports register the tables with SQLAlchemy metadata.
from app.models.user import User
from app.models.hotel import Hotel
from app.models.booking import Booking

from app.api.auth_api import router as auth_router
from app.api.user_api import router as user_router
from app.api.hotel_api import router as hotel_router
from app.api.booking_api import router as booking_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables that do not already exist
    Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(
    title="Hotel Booking API",
    description="Demo Hotel Booking Application",
    version="1.0.0",
    lifespan=lifespan,
)


# Allows local React development.
# Through Kubernetes Ingress, frontend and backend use the same origin,
# so Cloudflare requests do not require a separate CORS origin.
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API routers
app.include_router(
    auth_router,
    prefix="/api/v1",
)

app.include_router(
    user_router,
    prefix="/api/v1",
)

app.include_router(
    hotel_router,
    prefix="/api/v1",
)

app.include_router(
    booking_router,
    prefix="/api/v1",
)


# Prometheus metrics
instrumentator = Instrumentator(
    should_group_status_codes=True,
    should_ignore_untemplated=True,
    should_respect_env_var=False,
    should_instrument_requests_inprogress=True,
)

instrumentator.instrument(app).expose(
    app,
    endpoint="/metrics",
    include_in_schema=True,
)


@app.get("/")
def home():
    return {
        "message": "Hotel Booking API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
