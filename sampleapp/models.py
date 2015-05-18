from django.db import models
from django.contrib.auth import login
from django.contrib.auth.signals import user_logged_in

# Create your models here.
# users and items are for single 

class User(models.Model):
	userid = models.CharField(max_length=30,primary_key=True)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email = models.emailField

	#it is for printing out with normal words
	def _unicode_(self):
		return self.name


class Items(models.Model):
	userid=models.ForeignKey(User)
	itemsid=models.CharField(max_length=30,primary_key=True)
	itemname= models.CharField(max_length=100)
	comments = models.CharField(max_length=254)
	ratings = models.CharField(max_length=30)
	decision=models.BooleanField(deault=False)

	def _unicode_(self):
		return self.name

#Groups and boards contained user and items


class Groups(models.Model):
	user = models.OneToOneField(User,primary_key=True)
	groupid = models.CharField(max_length=30,primary_key=Ture)

	def _unicode_(self):
		return self.name

class Shareboards(models.Model):
	groupid = models.ForeignKey(Groups)
	user = models.OneToOneField(User,primary_key=True)
	itemname= models.CharField(max_length=100)
	comments = models.CharField(max_length=254)
	ratings = models.CharField(max_length=30)
	decision=models.BooleanField(deault=False)

	def _unicode_(self):
		return self.name

class Queryhistory(models.Model):
	userid = models.ForeignKey(User)
	query = models.CharField(max_length=254)

	def _unicode_(self):
		return self.names