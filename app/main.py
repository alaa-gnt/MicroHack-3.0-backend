from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import signals, pipeline, alerts, analytics, knowledge_base, auth
