from django.db import models

class report(models.Model):
	title = models.CharField(max_length = 100)
	pub_date = models.DateTimeField()
	body = models.TextField(max_length = 300)
	

#wordcloud
#UpsandDowns
#PercentageOfMood
class visualize(TimeStampedModel)