from rest_framework import serializers
from solid_backend.media_object.serializers import MediaObjectSerializer

from .models import Word, Tone, Meaning


class DisplayNameModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super(DisplayNameModelSerializer, self).to_representation(instance)

        return serializers.OrderedDict(filter(lambda x: not x[1] is None, ret.items()))


class ToneSerializer(DisplayNameModelSerializer):

    class Meta:
        model = Tone
        exclude = ["word"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class MeaningSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Meaning
        exclude = ["word"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class WordSerializer(DisplayNameModelSerializer):
    tone = ToneSerializer()
    meaning = MeaningSerializer()
    media_objects = MediaObjectSerializer(many=True)

    class Meta:
        model = Word
        fields = "__all__"
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}
