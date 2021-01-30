from django.conf.urls import url, include
from rest_framework import routers
from . import views 

app_name = 'api'

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('task', views.ToDoViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url(r'^authenticate/', views.CustomObtainAuthToken.as_view()),
]