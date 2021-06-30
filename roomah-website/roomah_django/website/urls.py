from django.urls import path, include

from website import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'djangoprofiles', views.HousemateList)
router.register(r'djangohouses', views.HouseList)

urlpatterns = [
    
    path('djangohouse/<slug:house_slug>/', views.HouseDetail.as_view()),
    path('djangohousemate/<slug:housemate_slug>/', views.HousemateDetail.as_view()),
    path('', include(router.urls)),
]