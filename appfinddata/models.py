from django.db import models
from django.core.validators import MaxLengthValidator

class WebsiteData(models.Model):

	title = models.TextField( validators=[MaxLengthValidator(500)], verbose_name = 'Title', blank = True, help_text = 'Title of  your URL')
	meta_description = models.TextField( validators=[MaxLengthValidator(1500)], verbose_name = 'Meta Description', blank = True, help_text = ' Meta Description')
	meta_keywords = models.TextField( validators=[MaxLengthValidator(1500)],verbose_name = 'Meta Keywords', blank = True, help_text = ' Meta Key words. ')
	
	def __unicode__(self):
		return self.title
	
	class Meta:
		verbose_name = 'website data'
		verbose_name_plural = 'website data'


