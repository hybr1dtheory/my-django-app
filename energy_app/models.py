from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    region = models.CharField(max_length=20)

    def __str__(self):
        return f"username: {self.username}\nname: {self.first_name} {self.last_name}\nregion: {self.region}"


class Meter(models.Model):
    meter_name = models.CharField(max_length=32)
    phases = models.IntegerField(default=1)
    kt = models.IntegerField(default=1)
    commercial = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"name: {self.meter_name}\nphases: {self.phases}\nkt: {self.kt}"


class Reading(models.Model):
    read_time = models.DateTimeField()
    value = models.FloatField()
    meter_id = models.ForeignKey(Meter, on_delete=models.CASCADE)
