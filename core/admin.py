from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from core.models import Article

class AuthorAdmin(SummernoteModelAdmin):
    pass
admin.site.register(Article, AuthorAdmin)
