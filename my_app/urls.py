from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Company',views.CompanyView)
router.register('Contact',views.ContactView)

urlpatterns = [
    path('',include(router.urls))

]
