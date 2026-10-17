from django.contrib import admin
from .models import Article, Attachment, AuditLog

admin.site.register(Article)
admin.site.register(Attachment)
admin.site.register(AuditLog)