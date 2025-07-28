from solid_backend.media_object.serializers import MediaObjectSerializer
from solid_backend.utils.serializers import SolidModelSerializer

from .models import Word, Tone, ToneAdvanced, Meaning, GeneralInformation


class ToneSerializer(SolidModelSerializer):

    class Meta:
        model = Tone
        exclude = ["word"]


class ToneAdvancedSerializer(SolidModelSerializer):

    class Meta:
        model = ToneAdvanced
        exclude = ["word"]


class MeaningSerializer(SolidModelSerializer):

    class Meta:
        model = Meaning
        exclude = ["word"]


class GeneralInformationSerializer(SolidModelSerializer):

    class Meta:
        model = GeneralInformation
        exclude = ["word"]


class WordSerializer(SolidModelSerializer):

    general_information = GeneralInformationSerializer()
    tone = ToneSerializer()
    tone_advanced = ToneAdvancedSerializer()
    meaning = MeaningSerializer()
    media_objects = MediaObjectSerializer(many=True)

    class Meta:
        model = Word
        fields = "__all__"
