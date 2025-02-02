from rest_framework.test import APITestCase
from unittest.mock import patch
from django.urls import reverse
from rest_framework import status


class ExhibitionViewSetTest(APITestCase):

    @patch('museumplanner.views.harvardartsmuseum_api')
    @patch('museumplanner.views.harvard_weather_data')
    def test_list(self, mock_weather_data, mock_harvard_api):
        # Mock the API data
        mock_harvard_api.return_value.json.return_value = {
            "info": {
                "totalrecordsperquery": 1,
                "totalrecords": 1,
                "pages": 1,
                "page": 1,
                "next": None,
                "responsetime": "0.123"
            },
            "records": [
                {
                    "shortdescription": "Short description",
                    "htmldescription": "HTML description",
                    "images": [],
                    "begindate": "2023-01-01",
                    "color": "blue",
                    "description": "Description",
                    "exhibitionid": 1,
                    "title": "Title",
                    "primaryimageurl": None,
                    "temporalorder": 1,
                    "url": "http://example.com",
                    "textiledescription": "Textile description",
                    "enddate": "2023-12-31",
                    "id": 1,
                    "lastupdate": "2023-01-01T00:00:00Z",
                    "poster": None
                }
            ]
        }
        mock_weather_data.return_value = {
            "temperature": [20.0, 21.0, 22.0],
            "rain": [0.0, 0.1, 0.0],
            "timestamps": [1672531200, 1672534800, 1672538400]
        }

        # Define the query parameters
        query_params = {'param1': 'value1', 'param2': 'value2'}

        # Make the request
        url = reverse('exhibitions-list')  # Adjust the URL name as per your configuration
        response = self.client.get(url, query_params)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('info', response.data)
        self.assertIn('records', response.data)
        self.assertIn('weather', response.data)

        # Check the structure of the serialized data
        self.assertEqual(response.data['info']['totalrecordsperquery'], 1)
        self.assertEqual(response.data['records'][0]['title'], "Title")
        self.assertEqual(response.data['weather']['temperature'], [20.0, 21.0, 22.0])
