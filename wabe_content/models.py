from django.db import models
from solid_backend.content.models import SolidBaseProfile
from django.utils.translation import ugettext_lazy as _


class Word(SolidBaseProfile):

    name = models.CharField(max_length=200, verbose_name=_("Titel"))

    graphic = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Graphie"),
    )
    lexem = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Lexem"),
    )
    etymology = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Etymologie"),
    )
    semantics = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Semantik"),
    )

    class Meta:
        verbose_name = _("Wort")
        verbose_name_plural = _("Wörter")

