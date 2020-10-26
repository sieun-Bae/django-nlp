from django.db import models

from blog.models import TimeStampedModel

class nlp(TimeStampedModel):
	title = models.CharField(max_length=200)