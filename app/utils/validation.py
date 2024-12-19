from aiogram.types import Message
import datetime as dt
from pytz.tzinfo import DstTzInfo

from app.schemas.trip import TransportEnum
from app.schemas.coordinates import Coordinates
from app.utils.get_timezone import timezone_adaptation


async def check_validation_string(string: str, message: Message) -> bool:
    correct_date = True
    if not (len(string) <= 128):
        correct_date = False
        await message.answer("The string must have no more than 128 characters")

    return correct_date

async def check_validation_travel_datetime(date_time: str, timezone: DstTzInfo, message: Message) -> dt.datetime | None:
    try:
        date, time = date_time.split()
        datetime = dt.datetime.fromisoformat(date + 'T' + time)
    except ValueError:
        await message.answer("Incorrect format")
        return
    datetime = timezone_adaptation(datetime, timezone)
    if datetime <= message.date.replace(tzinfo=None):
        await message.answer("Time in past cannot be specified")
        return
    if datetime > dt.datetime.fromisoformat("2100-01-01"):
        await message.answer("Travel time must be less than 2100 years")
        return
    return datetime

async def check_validation_notification_time(time: str, travel_date: dt.datetime, message: Message) -> dt.datetime | None:
    days = hours = minutes = seconds = 0
    match time:
        case '10 minutes':
            minutes = 10
        case '20 minutes':
            minutes = 20
        case '30 minutes':
            minutes = 30
        case _:
            for value in time.split():
                if not value.isdigit():
                    await message.answer("Incorrect format")
                    return
            days, hours, minutes, seconds = [int(value) for value in time.split()]
    timedelta_value = dt.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    if not (dt.timedelta(seconds=1) <= timedelta_value <= dt.timedelta(days=365)):
        await message.answer("The notification time can be from 1 second to 1 year")
        return
    if travel_date - timedelta_value <= message.date.replace(tzinfo=None):
        await message.answer("Notification time in past cannot be specified")
        return
    return dt.datetime.fromisoformat('1970-01-01') + timedelta_value

async def check_validation_transport_type(transport_type: str, message: Message) -> bool:
    correct_data = False
    for tr_type in list(TransportEnum):
        if TransportEnum(tr_type).name == transport_type:
            correct_data = True
            break
    if not correct_data:
        await message.answer("Press the button")
    return correct_data


async def check_validation_number_of_trip(len_trips: int, number: str, message: Message) -> bool:
    if not number.isdigit():
        await message.answer('Enter a number')
        return False
    if int(number) < 1:
        await message.answer('Number must be positive')
        return False
    if int(number) > len_trips:
        await message.answer(f'Enter number up to {len_trips}')
        return False
    return True

async def check_validation_location(message: Message) -> Coordinates | None:
    if message.location:
        location = Coordinates(latitude=str(message.location.latitude),
                               longitude=str(message.location.longitude))
        return location
    else:
        await message.answer('Send the location')
        return



