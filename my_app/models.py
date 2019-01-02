from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    website_url = models.URLField(max_length=100)
    year_of_est = models.IntegerField()
    bussiness_type = models.CharField(max_length=100)
    number_of_emp = models.IntegerField()
    industry = models.CharField(max_length=100)
    street_add = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    facebook_url = models.URLField(max_length=100,unique=True)
    insta_url = models.URLField(max_length=100,unique=True)
    linkdin_url = models.URLField(max_length=100,unique=True)
    contacts = models.ForeignKey('contact',on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name_emp = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email_emp = models.EmailField(max_length=100,unique=True)
    mobile = models.IntegerField(unique=True)
    linkdin_emp_url = models.URLField(max_length=100,unique=True)

    def __str__(self):
        return self.name_emp
