from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
    	return self.name

class Habbit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    occurences = models.IntegerField(default=0)
    def __str__(self):
        return self.name
