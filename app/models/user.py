from typing import Annotated
from datetime import datetime
from sqlalchemy import Integer, DATETIME, text, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base

datetime_auto = Annotated[datetime, mapped_column(DATETIME, server_default=text("TIMEZONE('utc', now())"))]
varchar_128 = Annotated[str, mapped_column(VARCHAR, nullable=False)]

class User(Base):
    __tablename__ = "user"

    name: Mapped[varchar_128]
    chat_id: Mapped[int] = mapped_column(Integer(), nullable=False, primary_key=True)
    registration_date = Mapped[datetime_auto]
