from datetime import timedelta

import caldav  # type: ignore
from caldav import Calendar, Event
from pydexcom import GlucoseReading  # type: ignore

from services.caldav_client import CalDAVClient
from services.dexcom import Dexcom
from config import Config
from utils.create_ical import create_ical


def _add_bg_to_calendar(bg: GlucoseReading) -> None:
    my_principal = CalDAVClient.principal()
    # Let's try to find or create a calendar ...
    calendar: Calendar
    try:
        # This will raise a NotFoundError if calendar does not exist
        calendar = my_principal.calendar(name=Config.CALENDAR_NAME)
        assert(calendar)
        # calendar did exist, probably it was made on an earlier run
        # of this script
    except caldav.error.NotFoundError:
        # Let's create a calendar
        calendar = my_principal.make_calendar(name=Config.CALENDAR_NAME)

    ical_str = create_ical(
        dtstart=bg.time,
        dtend=bg.time + timedelta(minutes=15),
        summary=f'{bg.mmol_l} {bg.trend_arrow}',
    )

    all_events = calendar.events()

    new_event: Event = calendar.save_event(ical_str)

    # Delete all old events
    for e in all_events:
        if e.id != new_event.id:
            e.delete()


def put_bg_to_calendar() -> None:
    bg = Dexcom.get_current_glucose_reading()
    return _add_bg_to_calendar(bg)
