from django.db import models

class Goat(models.Model):
    tag_number = models.CharField(max_length=50, unique=True)
    breed = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    health_status = models.CharField(max_length=100, default="Healthy")
    purchase_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.tag_number
