from django.db import models
from django.contrib.auth.models import User

class Notebook(models.Model):
    note_title = models.TextField()
    note_data = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'notebook'
        unique_together = (('id', 'note_title'),)

