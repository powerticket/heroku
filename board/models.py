from django.conf import settings
from django.db import models


# Create your models here.
class Writing(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


# class Comment(models.Model):
#     writing = models.ForeignKey(Writing, on_delete=models.CASCADE)
#     comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='recomments', null=True, blank=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


#     def __str__(self):
#         return self.title