from django.db import models

# Create your models here.


# Year table /
class Year(models.Model):
	year = models.CharField(max_length=50)

	def __str__(self):
		return self.year
# / Year table


# Language table /
class Language(models.Model):
	name = models.CharField(max_length=50)
	year = models.ForeignKey(Year, on_delete=models.CASCADE)
# / Language table


# Project table /
def upload_location(project, filename):
	return "%s/%s" %(project.name, filename)

class Project(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	picture = models.ImageField(upload_to=upload_location, max_length=50, blank=True, null=True)
	year = models.ForeignKey(Year, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
# / Project table


# Alumni table /
def upload_location(alumni, filename):
	return "%s/%s" %(alumni.last_name, filename)

class Alumni(models.Model):
	class Meta:
		verbose_name_plural = 'Alumni'

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	email = models.EmailField(max_length=50, blank=True, null=True)
	github_link = models.URLField(blank=True, null=True)
	phone_number = models.CharField(max_length=32, blank=True, null=True)
	picture = models.ImageField(upload_to=upload_location, max_length=255, blank=True, null=True)
	cv = models.FileField(upload_to=upload_location)
	language = models.ForeignKey(Language, on_delete=models.CASCADE)

	def __str__(self):
		return self.first_name + " " + self.last_name
# / Alumni table




















