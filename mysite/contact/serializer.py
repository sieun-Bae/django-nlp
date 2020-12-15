from .models import Contact
from rest_framework import serializers

class ContactSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contact
		fields = [ 'publish_date', 'name', 'email', 'number', 'message' ]