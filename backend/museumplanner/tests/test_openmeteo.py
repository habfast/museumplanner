import unittest
from unittest.mock import patch, MagicMock
from museumplanner.openmeteo import openmeteo_client, harvard_museum_meteo
from openmeteo_sdk import WeatherApiResponse


class TestMeteo(unittest.TestCase):

    @patch("museumplanner.openmeteo.requests_cache.CachedSession")
    @patch("museumplanner.openmeteo.retry")
    @patch("museumplanner.openmeteo.openmeteo_requests.Client")
    def test_openmeteo_client(self, MockClient, mock_retry, MockCachedSession):
        mock_session = MagicMock()
        MockCachedSession.return_value = mock_session
        mock_retry_session = MagicMock()
        mock_retry.return_value = mock_retry_session

        openmeteo_client()
        openmeteo_client()
        client = openmeteo_client()

        MockCachedSession.assert_called_once_with(".cache", expire_after=3600)
        mock_retry.assert_called_once_with(mock_session, retries=5, backoff_factor=0.2)
        MockClient.assert_called_once_with(session=mock_retry_session)
        self.assertEqual(client, MockClient.return_value)

    @patch("museumplanner.openmeteo.openmeteo_client")
    def test_harvard_museum_meteo(self, mock_openmeteo_client):
        mock_client = MagicMock()
        mock_response = MagicMock(spec=WeatherApiResponse)
        mock_client.weather_api.return_value = [mock_response]
        mock_openmeteo_client.return_value = mock_client

        response = harvard_museum_meteo(["temp", "rain"])

        mock_openmeteo_client.assert_called_once()
        mock_client.weather_api.assert_called_once_with(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": 42.373611, "longitude": -71.110558, "hourly": ["temp", "rain"], "forecast_days": 3},
        )
        self.assertEqual(response, mock_response)
