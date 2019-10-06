from django.contrib import admin

from .models import CodeTrick, Language

# Register your models here.

admin.site.register(Language)
admin.site.register(CodeTrick)