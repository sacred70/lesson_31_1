from pytest_factoryboy import register
from factories import *

pytest_plugins = "test.fixtures"

register(CategoryFactory)
register(AdFactory)
register(UserFactory)
