from rest_framework import serializers
from solid_backend.media_object.serializers import MediaObjectSerializer
from solid_backend.utils.serializers import SolidModelSerializer
from drf_spectacular.extensions import OpenApiSerializerFieldExtension, OpenApiSerializerExtension

from .models import Word, Tone, Meaning, MDTextField


class MDStringField(serializers.CharField):

    class Meta:
        swagger_schema_fields = {
            "type": "mdstring"
        }


class MDField(serializers.CharField):
    pass


class ToneSerializer(SolidModelSerializer):

    serializer_field_mapping = {
        **serializers.ModelSerializer.serializer_field_mapping,
        MDTextField: MDField
    }

    class Meta:
        model = Tone
        exclude = ["word"]


class MeaningSerializer(SolidModelSerializer):

    serializer_field_mapping = {
        **serializers.ModelSerializer.serializer_field_mapping,
        MDTextField: MDField
    }

    class Meta:
        model = Meaning
        exclude = ["word"]


class WordSerializer(SolidModelSerializer):

    tone = ToneSerializer()
    meaning = MeaningSerializer()
    media_objects = MediaObjectSerializer(many=True)
    serializer_field_mapping = {
        **serializers.ModelSerializer.serializer_field_mapping,
        MDTextField: MDField
    }

    class Meta:
        model = Word
        fields = "__all__"
