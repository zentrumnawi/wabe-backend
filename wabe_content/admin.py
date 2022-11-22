from django.contrib import admin
from solid_backend.media_object.admin import MediaObjectInline

from .models import Word, Tone, Meaning
# Register your models here.


class ToneAdminInline(admin.StackedInline):
    model = Tone


class MeaningAdminInline(admin.StackedInline):
    model = Meaning


class WordAdmin(admin.ModelAdmin):
    model = Word
    inlines = [ToneAdminInline, MeaningAdminInline, MediaObjectInline]


class ToneAdmin(admin.ModelAdmin):
    model = Tone


class MeaningAdmin(admin.ModelAdmin):
    model = Meaning


admin.site.register(Word, WordAdmin)
admin.site.register(Tone, ToneAdmin)
admin.site.register(Meaning, MeaningAdmin)
