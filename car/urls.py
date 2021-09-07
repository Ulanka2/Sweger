from django.urls import path
from rest_framework.routers import SimpleRouter

from car.views import CarView, CarDocumentView

router = SimpleRouter()
router.register('car', CarView)
router.register('cardoc', CarDocumentView)
urlpatterns = []
urlpatterns += router.urls
