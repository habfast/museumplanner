import requests
from django.conf import settings
from django.utils.http import urlencode

from museumplanner.constants import HARVARD_ARTS_MUSEUM_API_ENDPOINT


def harvardartsmuseum_api(query_params: dict) -> requests.Response:
    query_params["apikey"] = settings.HARVARD_ARTS_MUSEUM_API_KEY

    endpoint = f"{HARVARD_ARTS_MUSEUM_API_ENDPOINT}?{urlencode(query_params)}"

    response = requests.get(endpoint)
    response.raise_for_status()
    return response
