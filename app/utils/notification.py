from aiogram.types import Message

from app.schemas.trip import TripRead


async def send_notification_trip(trip: TripRead, message: Message):
    await message.answer('You have a scheduled trip with early start time coming up:' + '\n' + trip.get_info())