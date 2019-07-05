from django.db import models

# testing
import datetime
from django.utils import timezone

# Create your models here.
class Service(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	# pub_date = models.DateTimeField('date published')
	# exp_date = models.DateTimeField('date expired')
	def __str__(self):
		return self.title
# To add more
# ?to add 'service type' and link to a drop-down menu?/other object class

# class Type(models.Model):



class TestQuestion(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class TestChoice(models.Model):
	question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

