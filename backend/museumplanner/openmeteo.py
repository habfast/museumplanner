from functools import cache

import openmeteo_requests
from openmeteo_sdk import WeatherApiResponse

from museumplanner.constants import OPENMETEO_API_ENDPOINT, HARVARD_MUSEUM_LAT, HARVARD_MUSEUM_LONG
import requests_cache
from retry_requests import retry


@cache
def openmeteo_client():
    cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    return openmeteo_requests.Client(session=retry_session)


def harvard_museum_meteo() -> WeatherApiResponse:
    responses = openmeteo_client().weather_api(
        OPENMETEO_API_ENDPOINT,
        params={"latitude": HARVARD_MUSEUM_LAT, "longitude": HARVARD_MUSEUM_LONG, "hourly": ["temperature_2m", "rain"]},
    )
    return responses[0]
