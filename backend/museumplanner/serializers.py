from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    temperature = serializers.ListSerializer(child=serializers.DecimalField(max_digits=5, decimal_places=2), read_only=True)
    rain = serializers.ListSerializer(child=serializers.DecimalField(max_digits=5, decimal_places=2), read_only=True)


class ImageSerializer(serializers.Serializer):
    date = serializers.CharField(allow_null=True, required=False)
    copyright = serializers.CharField(allow_null=True, required=False)
    imageid = serializers.IntegerField()
    idsid = serializers.IntegerField()
    format = serializers.CharField()
    caption = serializers.CharField(allow_null=True, required=False)
    description = serializers.CharField(allow_null=True, required=False)
    technique = serializers.CharField(allow_null=True, required=False)
    renditionnumber = serializers.CharField()
    displayorder = serializers.IntegerField()
    baseimageurl = serializers.URLField()
    alttext = serializers.CharField(allow_null=True, required=False)
    width = serializers.IntegerField()
    iiifbaseuri = serializers.URLField()
    height = serializers.IntegerField()

class PosterSerializer(serializers.Serializer):
    imageurl = serializers.URLField()
    caption = serializers.CharField(allow_null=True, required=False)

class ExhibitionRecordSerializer(serializers.Serializer):
    shortdescription = serializers.CharField(allow_null=True, required=False)
    htmldescription = serializers.CharField(allow_null=True, required=False)
    images = ImageSerializer(many=True, default=[])
    begindate = serializers.DateField()
    color = serializers.CharField(allow_null=True, required=False)
    description = serializers.CharField(allow_null=True, required=False)
    exhibitionid = serializers.IntegerField()
    title = serializers.CharField()
    primaryimageurl = serializers.URLField(default=None)
    temporalorder = serializers.IntegerField()
    url = serializers.URLField()
    textiledescription = serializers.CharField(allow_null=True, required=False)
    enddate = serializers.DateField(allow_null=True, required=False)
    id = serializers.IntegerField()
    lastupdate = serializers.DateTimeField()
    poster = PosterSerializer(default=None)

class InfoSerializer(serializers.Serializer):
    totalrecordsperquery = serializers.IntegerField()
    totalrecords = serializers.IntegerField()
    pages = serializers.IntegerField()
    page = serializers.IntegerField()
    next = serializers.URLField()
    responsetime = serializers.CharField()

class ExhibitionListSerializer(serializers.Serializer):
    info = InfoSerializer()
    records = ExhibitionRecordSerializer(many=True)
    weather = WeatherSerializer()
