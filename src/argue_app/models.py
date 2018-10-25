from django.db import models
import django.utils.timezone as tz

# class Data(models.Model):
#     date_time = models.DateTimeField(blank=False)
#     type = models.ForeignKey('DataType', blank=False, on_delete=True)
#     value = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)

class Argument(models.Model):
    opponent = models.CharField(max_length=200)
    last_date = models.DateField(null=True, blank=True)
    outcome = models.CharField(max_length=200)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)


class Profile(models.Model):
    bio  = models.CharField(max_length=200)
    rank = models.IntegerField(default=0)
    user = models.OneToOneField("User", on_delete=models.CASCADE)
