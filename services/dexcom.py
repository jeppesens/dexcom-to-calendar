from pydexcom import Dexcom as DexcomClient  # type: ignore
from config import Config


Dexcom = DexcomClient(
    username=Config.DEXCOM_USERNAME,
    password=Config.DEXCOM_PASSWORD,
    ous=Config.DESCOM_OUTSIDE_US,
)
