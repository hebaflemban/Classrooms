from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User as

class Classroom(models.Model):
	subject = models.CharField(max_length=120)
	grade = models.IntegerField()
	year = models.IntegerField()
	teacher = models.ForeignKey(User, on_delete = models.SET_DEFAULT, default = 1)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})


class Student(models.Model):
	male = 'M'
	female = 'F'
	Gender = [(male ,'Male'),(female,'Female')]

	name = models.CharField(max_length=50)
	dob = models.DateField()
	gender = models.CharField(max_length=2, choices = Gender)
	exam_grade = models.IntegerField()
	classroom = models.Foreignkey(Classroom, on_delete = models.SET_NULL, default = 1)
