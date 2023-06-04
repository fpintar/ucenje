from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models heret


class Item(models.Model):

    def __str__(self) -> str:
        return self.item_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500, default="https://th.bing.com/th/id/OIP.CAXQe3AgWFel1hIzxDZ6owEsDg?w=268&h=201&c=7&r=0&o=5&pid=1.7")

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
