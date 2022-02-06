import caldav  # type: ignore

from config import Config


CalDAVClient = caldav.DAVClient(
    url=Config.CALDAV_URL,
    username=Config.CALDAV_USER,
    password=Config.CALDAV_PASSWORD,
)
