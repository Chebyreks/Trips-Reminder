from celery import Celery
from aiogram.types import Message
from datetime import datetime


from app.core.config import settings
from app.schemas.trip import TripRead

celery_app = Celery('tasks', broker=settings.redis_url)





