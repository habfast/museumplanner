from rest_framework import views, viewsets
from rest_framework.response import Response

from museumplanner.harvardartsmuseum_api import harvardartsmuseum_api
from museumplanner.openmeteo import harvard_weather_data
from museumplanner.pagination import HarvardArtsMuseumApiPagination
from museumplanner.serializers import ExhibitionListSerializer


class ExhibitionViewSet(viewsets.GenericViewSet):
    serializer_class = ExhibitionListSerializer

    def list(self, request):
        # Your logic to fetch data from the external API
        query_params = request.query_params.dict()
        api_data = harvardartsmuseum_api(query_params).json()
        api_data["weather"] = harvard_weather_data()

        serializer = self.get_serializer(instance=api_data)
        return Response(serializer.data)
