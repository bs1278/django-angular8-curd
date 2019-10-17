import json
from django.core.serializers import serialize
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
	"""
	Post Model. 
	"""
	post_title = models.CharField(
		_("Post Title"), 
		max_length=150
	)
	post_text = models.TextField(
		_("Post Text")
	)

	def __str__(self):
		return self.post_title

	class Meta:
		verbose_name = _("Posts")
		verbose_name_plural = _("Posts")
		ordering = ['post_title']

	def serialize(self):
		data={
			"id":self.id,
			"post_title":self.post_title,
			"post_text":self.post_text
		}
		data = json.dumps(data)
		return data