from django.contrib import admin
from .models import Word
# Register your models here.


class WordAdmin(admin.ModelAdmin):
    model = Word


admin.site.register(Word, WordAdmin)
