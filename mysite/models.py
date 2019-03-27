from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    github_link = models.URLField()
    description = models.TextField()
    thumbnail = models.ImageField(null=True)
    live = models.URLField(blank=True, null=True)
    tech = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "{0}".format(self.title)


class Message(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    body = models.TextField()
    budget = models.IntegerField()

    def __str__(self):
        return "{0} from {1}".format(self.name, self.address)
