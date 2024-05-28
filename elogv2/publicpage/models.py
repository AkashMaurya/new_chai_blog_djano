from django.db import models
from django.utils import timezone


# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KL", "KIWI"),
        ("PL", "PLAIN"),
        ("EL", "ELACHI"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    data_added = models.DateTimeField(default=timezone.now)
    type_of_chai = models.CharField(choices=CHAI_TYPE_CHOICE, max_length=2)

    def __str__(self):
        return f"{self.name}, {self.image}, {self.data_added}, {self.type_of_chai}"
