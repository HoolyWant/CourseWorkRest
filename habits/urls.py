from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitsViewSet, HabitsListAPI

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'habits', HabitsViewSet, basename='habits')


urlpatterns = [
    path('habits/public/', HabitsListAPI.as_view(), name='public_habits')
] + router.urls
