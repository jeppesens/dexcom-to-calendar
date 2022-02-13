from datetime import datetime
from typing import Any
import uuid

import pytz

from icalendar import Calendar, Event  # type: ignore


def _assume_utc_date(d: datetime) -> datetime:
    if not d.tzinfo:
        return pytz.utc.localize(d)
    return d


def create_ical(dtstart: datetime, dtend: datetime, summary: str, **kwargs: Any) -> str:
    language = 'en_SE'
    my_instance = Calendar()
    my_instance.add('prodid', f'-//dexcom-calendar//caldav//{language}')
    my_instance.add('version', '2.0')
    component = Event()
    component.add('dtstamp', datetime.now())
    component.add('uid', uuid.uuid1())

    attributes = {
        'dtstart': _assume_utc_date(dtstart),
        'dtend': _assume_utc_date(dtend),
        'summary': summary,
        **kwargs,
    }
    for attribute in attributes:
        if attributes[attribute] is not None:
            component.add(attribute, attributes[attribute])
    my_instance.add_component(component)
    bytes_value = my_instance.to_ical()
    return bytes_value.decode('utf-8').replace('\r\n', '\n')
