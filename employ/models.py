from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_add = models.EmailField(max_length=100, unique=True)
    number = models.CharField(max_length=12, blank=True)
    # add is good for ontime modification
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # updating

    def __str__(self):
        return self.first_name

    # when we add makemigration command it generate a migration file which contail query to create data

    # model should be registerd in the admin pannel then only we can see the table in admin pannel
