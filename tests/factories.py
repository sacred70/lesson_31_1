import factory

from ads.models import Ad, Category
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = factory.Faker("name")
    slug = factory.Faker("ean", lenght=8)


class AdFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Ad

    name = factory.Faker("name")
    price = 300
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
