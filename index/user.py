from django.db import models


class User(models.Model):
    user_id = models.IntegerField(unique=True, db_index=True)
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "user"
        ordering = ["-created_at"]