from django.db import models
#from django.conf import settings

'''
daily datasets
- time when it saved
- answer for question1
- answer for question2
- answer for question3
'''
# User = settings.AUTH_USER_MODEL

class Post(models.Model):
	# user = models.ForeignKey(User, defalult=1, null=True, on_delete=models.SET_NULL)
	# id = models.IntegerField()
	publish_date = models.DateTimeField(auto_now = True)
	answer1 = models.TextField(null=True, blank=True)
	answer2 = models.TextField(null=True, blank=True)
	answer3 = models.TextField(null=True, blank=True)
	
	def post_save(self):
		self.save()

	class Meta:
		ordering = [ "-publish_date" ]

		