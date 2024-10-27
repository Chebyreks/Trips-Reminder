from typing import Annotated, Any
from datetime import datetime
from sqlalchemy import Integer, DATETIME, text, VARCHAR, ForeignKey, JSON, BOOLEAN
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base
from enum import Enum

datetime_auto = Annotated[datetime, mapped_column(DATETIME, server_default=text("TIMEZONE('utc', now())"))]
varchar_128 = Annotated[str, mapped_column(VARCHAR, nullable=False)]
int_pk = Annotated[int, mapped_column(Integer(), autoincrement=True, primary_key=True)]
json = Annotated[dict[Any, Any], mapped_column(JSON, nullable=False)]
datetime_annotation = Annotated[datetime, mapped_column(DATETIME, nullable=False)]

class TransportType(Enum):
    metro = 1
    bus = 2
    car = 3
    train = 4
    airplane = 5

class Trip(Base):
    __tablename__ = "trip"

    id: Mapped[int_pk]
    chat_id: Mapped[int] = mapped_column(ForeignKey("user.chat_id"))
    to_place: Mapped[json]
    from_place: Mapped[json]
    to_place_title: Mapped[varchar_128]
    from_place_title: Mapped[varchar_128]
    transport_type: Mapped[TransportType] = mapped_column(VARCHAR, nullable=False)
    create_date = Mapped[datetime_auto]
    travel_date = Mapped[datetime_annotation]
    notification_before_travel = Mapped[datetime_annotation]
    isEnded: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)