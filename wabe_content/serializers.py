from rest_framework import serializers
from solid_backend.media_object.serializers import MediaObjectSerializer
from solid_backend.utils.serializers import SolidModelSerializer

from .models import Word, Tone, Meaning


class MDStringField(serializers.CharField):

    class Meta:
        swagger_schema_fields = {
            "type": "mdstring"
        }


class MDField(serializers.CharField):
    pass


class ToneSerializer(SolidModelSerializer):

    class Meta:
        model = Tone
        exclude = ["word"]


class MeaningSerializer(SolidModelSerializer):

    class Meta:
        model = Meaning
        exclude = ["word"]


class WordSerializer(SolidModelSerializer):

    tone = ToneSerializer()
    meaning = MeaningSerializer()
    media_objects = MediaObjectSerializer(many=True)

    class Meta:
        model = Word
        fields = "__all__"
