from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Groups(models.Model):
    SECTIONGROUP = (
        ('Tech', 'Tech'),
        ('Anime', 'Anime'),
        ('Crypto', 'Crypto'),
        ('Graphics', 'Graphics')
    )
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=SECTIONGROUP)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



class Specialization(models.Model):
    CATEGORY = (
        ('Tech', 'Tech'),
        ('Anime', 'Anime'),
        ('Crypto', 'Crypto'),
        ('Graphics', 'Graphics')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    groups = models.ForeignKey(Groups, null=True, on_delete=models.SET_NULL)
    level = models.CharField(max_length=200, null=True, choices=CATEGORY)
    whatsapp_num = models.CharField(max_length=200, null=True)
    email_address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.groups.name