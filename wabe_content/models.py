from django.db import models
from solid_backend.content.models import SolidBaseProfile
from solid_backend.content.fields import ConcatCharField
from solid_backend.utils.drf_spectacular_extensions import MDTextField as NewMDTextField
from django.utils.translation import ugettext_lazy as _

from .choices import TONE_CHOICES, MEANING_CHOICES


class MDTextField(models.TextField):
    pass


class Word(SolidBaseProfile):
    name = models.CharField(max_length=200, verbose_name=_("Titel"))

    graphic = MDTextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Graphie"),
    )
    lexem = MDTextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Lexem"),
    )
    etymology = MDTextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Etymologie"),
    )
    semantics = MDTextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Semantik"),
    )

    class Meta:
        verbose_name = _("Wort")
        verbose_name_plural = _("Wörter")


class Tone(models.Model):

    word = models.OneToOneField(
        Word,
        related_name="tone",
        on_delete=models.CASCADE,
        verbose_name=_("Wort")
    )
    description = MDTextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Beschreibung"),
    )
    indo_germ = ConcatCharField(
        max_length=400,
        concat_choices=[TONE_CHOICES, TONE_CHOICES, TONE_CHOICES, TONE_CHOICES, TONE_CHOICES],
        seperators=[", ", " und "],
        verbose_name=_("Indogermanisch zu Germanisch"),
        default="",
        blank=True
    )
    germ_to_ahd = ConcatCharField(
        max_length=400,
        concat_choices=[TONE_CHOICES, TONE_CHOICES, TONE_CHOICES, TONE_CHOICES, TONE_CHOICES],
        seperators=[", ", " und "],
        verbose_name=_("Germanisch zu Ahd."),
        default="",
        blank=True
    )
    ahd_to_mhd = ConcatCharField(
        max_length=400,
        concat_choices=[TONE_CHOICES, TONE_CHOICES, TONE_CHOICES, TONE_CHOICES, TONE_CHOICES],
        seperators=[", ", " und "],
        verbose_name=_("Ahd. zu Mhd"),
        default="",
        blank=True
    )
    mhd_to_nhd = ConcatCharField(
        max_length=400,
        concat_choices=[TONE_CHOICES, TONE_CHOICES, TONE_CHOICES, TONE_CHOICES, TONE_CHOICES],
        seperators=[", ", " und "],
        verbose_name=_("Mhd. zu Nhd."),
        default="",
        blank=True
    )

    class Meta:
        verbose_name = _("Lautwandel")
        verbose_name_plural =_("Lautwandel")


class Meaning(models.Model):
    word = models.OneToOneField(
        Word,
        related_name="meaning",
        on_delete=models.CASCADE,
        verbose_name=_("Wort")
    )
    description = MDTextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Beschreibung"),
    )
    meaning_type = ConcatCharField(
        max_length=400,
        concat_choices=[MEANING_CHOICES, MEANING_CHOICES, MEANING_CHOICES, MEANING_CHOICES, MEANING_CHOICES],
        seperators=[", ", " und "],
        verbose_name=_("Mhd. zu Nhd."),
        default="",
        blank=True
    )

    class Meta:
        verbose_name = _("Bedeutungswandel")
        verbose_name_plural = _("Bedeutungswandel")


class GeneralInformation(models.Model):

    word = models.OneToOneField(
        to=Word,
        on_delete=models.CASCADE,
        related_name="general_information",
        verbose_name=_("Wort"),
    )

    name = models.CharField(max_length=200, verbose_name=_("Titel"))

    graphic = NewMDTextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Graphie"),
    )
    lexem = NewMDTextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Lexem"),
    )
    etymology = NewMDTextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Etymologie"),
    )
    semantics = NewMDTextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Semantik"),
    )

    class Meta:
        verbose_name = _("Allgemein")
        verbose_name_plural = _("Allgemein")
