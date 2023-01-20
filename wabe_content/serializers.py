from rest_framework import serializers
from solid_backend.media_object.serializers import MediaObjectSerializer
from drf_spectacular.extensions import OpenApiSerializerFieldExtension

from .models import Word, Tone, Meaning, MDTextField


class MDStringField(serializers.CharField):

    class Meta:
        swagger_schema_fields = {
            "type": "mdstring"
        }


class MDField(serializers.CharField):
    pass


class DisplayNameModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super(DisplayNameModelSerializer, self).to_representation(instance)

        return serializers.OrderedDict(filter(lambda x: not x[1] in (None, ""), ret.items()))


class ToneSerializer(DisplayNameModelSerializer):

    serializer_field_mapping = {
        **serializers.ModelSerializer.serializer_field_mapping,
        MDTextField: MDField
    }

    class Meta:
        model = Tone
        exclude = ["word"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class MeaningSerializer(DisplayNameModelSerializer):

    serializer_field_mapping = {
        **serializers.ModelSerializer.serializer_field_mapping,
        MDTextField: MDField
    }

    class Meta:
        model = Meaning
        exclude = ["word"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class WordSerializer(DisplayNameModelSerializer):

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
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class MdFieldExtension(OpenApiSerializerFieldExtension):
    target_class = "wabe_content.serializers.MDField"

    def map_serializer_field(self, auto_schema, direction):
        schema = auto_schema._map_serializer_field(self.target, direction, bypass_extensions=True)
        schema['format'] = 'mdstring'
        return schema