from datetime import datetime
from typing import Any
import uuid

from icalendar import Calendar, Event  # type: ignore


def create_ical(dtstart: datetime, dtend: datetime, summary: str, **kwargs: Any) -> str:
    language = 'en_SE'
    my_instance = Calendar()
    my_instance.add('prodid', f'-//dexcom-calendar//caldav//{language}')
    my_instance.add('version', '2.0')
    component = Event()
    component.add('dtstamp', datetime.now())
    component.add('uid', uuid.uuid1())

    attributes = {
        'dtstart': dtstart,
        'dtend': dtend,
        'summary': summary,
        **kwargs,
    }
    for attribute in attributes:
        if attributes[attribute] is not None:
            component.add(attribute, attributes[attribute])
    my_instance.add_component(component)
    bytes_value = my_instance.to_ical()
    return bytes_value.decode('utf-8').replace('\r\n', '\n')
