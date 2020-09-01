from django.db import models

# Create your models here.


class Profile(models.Model):

    full_name = models.CharField(max_length = 200)
    email_address = models.EmailField(max_length = 254)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'


    def __str__(self):
        return self.username

class Cash_per_account(models.Model):
    cash_id = models.ForeignKey(Profile, on_delete= models.CASCADE)
    cash = models.IntegerField(default = 100)

    