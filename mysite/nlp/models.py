from django.db import models

from blog.models import TimeStampedModel

class Post(TimeStampedModel):
	#time = models.
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=300)
	#log_in = models.
