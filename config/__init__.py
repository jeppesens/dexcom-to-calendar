import os
from typing import Optional


class _Config(type):

    def _bool(self, env: str, default: bool = None) -> Optional[bool]:
        v: str
        if default is None:
            v = os.environ['DESCOM_OUTSIDE_US']
        else:
            v = os.getenv(env, '')

        if v.upper() in ['1', 'TRUE']:
            return True
        elif v.upper() in ['0', 'FALSE']:
            return False
        return default or None

    @property
    def DEXCOM_PASSWORD(self) -> str:
        return os.environ['DEXCOM_PASSWORD']

    @property
    def DEXCOM_USERNAME(self) -> str:
        return os.environ['DEXCOM_USERNAME']

    @property
    def DESCOM_OUTSIDE_US(self) -> bool:
        return self._bool('DESCOM_OUTSIDE_US', True)  # type: ignore

    @property
    def TICK_SEC(self) -> int:
        return 60

    @property
    def LOG_LEVEL(self) -> str:
        return os.getenv('LOG_LEVEL', 'INFO')

    @property
    def CALDAV_HOST(self) -> str:
        heroku = os.getenv('HEROKU_APP_NAME')
        if heroku:
            return f'{heroku}.herokuapp.com'
        if os.getenv('CALDAV_URL'):
            return os.getenv('CALDAV_HOST', '')
        return os.environ['CALDAV_HOST']

    @property
    def CALDAV_URL(self) -> str:
        return os.getenv('CALDAV_URL') or f'https://{self.CALDAV_HOST}/'

    @property
    def CALDAV_USER(self) -> str:
        return os.environ['CALDAV_USER']

    @property
    def CALDAV_PASSWORD(self) -> str:
        return os.environ['CALDAV_PASSWORD']

    @property
    def CALENDAR_NAME(self) -> str:
        return 'BG'


class Config(metaclass=_Config):
    pass


if __name__ == '__main__':
    # Checks that all necessary envs are set with an overkill map
    *map(lambda k: k.startswith('__') or getattr(Config, k), dir(Config.__class__)),
