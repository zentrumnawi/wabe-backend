from django.contrib import admin
from solid_backend.media_object.admin import MediaObjectInline

from .models import Word, Tone, Meaning, GeneralInformation


# Register your models here.


class ToneAdminInline(admin.StackedInline):
    model = Tone


class MeaningAdminInline(admin.StackedInline):
    model = Meaning


class GeneralInformationInline(admin.StackedInline):
    model = GeneralInformation


class WordAdmin(admin.ModelAdmin):
    model = Word
    inlines = [ToneAdminInline, MeaningAdminInline, MediaObjectInline]


admin.site.register(Word, WordAdmin)
admin.site.register(Tone, admin.ModelAdmin)
admin.site.register(Meaning, admin.ModelAdmin)
