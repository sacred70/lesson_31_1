from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import UniqueConstraint

from users.models import User


class Ad(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="ad_image", blank=True, null=True)
    category = models.ForeignKey("ads.Category", on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)
    constraints = [UniqueConstraint(fields=["name", "owner"], name="my_constraint")]

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name


class Category(models.Model):
    slug = models.SlugField(max_length=10, validators=[MinLengthValidator(5)], unique=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


def __str__(self):
    return self.name


def serialize(self):
    return {'name': self.name}
