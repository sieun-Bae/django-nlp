from django.db import models

class Contact(models.Model):
	# user = models.ForeignKey(User, defalult=1, null=True, on_delete=models.SET_NULL)
	# id = models.IntegerField()
	publish_date = models.DateTimeField(auto_now = True)
	name = models.TextField(null = True, blank=True)
	email = models.TextField(null = True, blank=True)
	number = models.TextField(null = True, blank=True)
	message = models.TextField(null = True, blank=True)

	class Meta:
		ordering = [ "-name" ]