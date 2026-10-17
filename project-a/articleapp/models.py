from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Attachment(models.Model):
    file = models.FileField(upload_to="attachments/")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="attachments")
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


class AuditLog(models.Model):
    action = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action