import unittest
from unittest.mock import patch, MagicMock

from django.test import TestCase

from museumplanner.harvardartsmuseum_api import harvardartsmuseum_api
from museumplanner.constants import HARVARD_ARTS_MUSEUM_API_ENDPOINT


class TestHarvardArtsMuseumAPI(TestCase):

    @patch('museumplanner.harvardartsmuseum_api.requests.get')
    @patch('museumplanner.harvardartsmuseum_api.settings')
    def test_harvardartsmuseum_api(self, mock_settings, mock_get):
        # Mock the settings to return a fake API key
        mock_settings.HARVARD_ARTS_MUSEUM_API_KEY = 'fake_api_key'

        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Define the query parameters
        query_params = {'param1': 'value1', 'param2': 'value2'}

        # Call the function
        response = harvardartsmuseum_api(query_params)

        # Construct the expected endpoint URL
        expected_endpoint = f"{HARVARD_ARTS_MUSEUM_API_ENDPOINT}?param1=value1&param2=value2&apikey=fake_api_key"

        # Assertions
        mock_get.assert_called_once_with(expected_endpoint)
        mock_response.raise_for_status.assert_called_once()
        self.assertEqual(response, mock_response)
