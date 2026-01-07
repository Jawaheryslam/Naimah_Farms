from django.db import models
from django.conf import settings


class Goat(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    STATUS_CHOICES = [
        ('alive', 'Alive'),
        ('sold', 'Sold'),
        ('dead', 'Dead'),
    ]

    BREED_CHOICES = [
        ('somali', 'Somali'),
        ('galla', 'Galla'),
        ('giriama', 'Giriama'),
        ('mixed', 'Mixed Breed'),
    ]

    name = models.CharField(max_length=100, blank=True, null=True)
    tag_number = models.CharField(max_length=50, unique=True)
    breed = models.CharField(
        max_length=20,
        choices=BREED_CHOICES,
        default='mixed'
        )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='alive')

    def __str__(self):
        return self.name or f"Goat {self.id}"


class BirthRecord(models.Model):
    mother_goat = models.ForeignKey(
        Goat,
        on_delete=models.CASCADE,
        related_name='births'
    )
    date_of_birth = models.DateField()
    number_of_kids = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Birth on {self.date_of_birth} ({self.number_of_kids} kids)"


class HealthRecord(models.Model):
    goat = models.ForeignKey(
        Goat,
        on_delete=models.CASCADE,
        related_name='health_records'
    )
    date = models.DateField()
    condition = models.CharField(max_length=255)
    treatment = models.TextField()
    vaccine_administered = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Health record for Goat {self.goat.id} on {self.date}"


class Sale(models.Model):
    goat = models.ForeignKey(Goat, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    sale_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale of Goat {self.goat.id}"


class Purchase(models.Model):
    animal_type = models.CharField(max_length=100)
    purchase_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.animal_type


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('transport', 'Transport'),
        ('medication', 'Medication'),
        ('salaries', 'Salaries'),
        ('others', 'Others'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"