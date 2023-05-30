from rest_framework import routers
from ads.views.cat import *


router = routers.SimpleRouter()
router.register("", CategoryViewSet)
urlpatterns = router.urls
