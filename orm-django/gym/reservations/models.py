from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.email


class SportClass(models.Model):
    name = models.CharField(max_length=100)
    max_capacity = models.PositiveIntegerField(
        default=10
    )  # Will be populated in migrations

    def __str__(self):
        return self.name


class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sport_class = models.ForeignKey(SportClass, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("client", "sport_class")  # Uniqueness validation

    def clean(self):
        if Booking.objects.filter(
            client=self.client, sport_class=self.sport_class
        ).exists():
            raise ValidationError("The client already has a booking for this class.")

    def __str__(self):
        return f"{self.client} - {self.sport_class}"


@receiver(post_migrate)
def create_default_classes(sender, **kwargs):
    if sender.name == "reservations":
        SportClass = sender.get_model("SportClass")
        if not SportClass.objects.exists():
            SportClass.objects.create(name="Yoga", max_capacity=25)
            SportClass.objects.create(name="CrossFit", max_capacity=20)
            SportClass.objects.create(name="Swimming", max_capacity=25)
