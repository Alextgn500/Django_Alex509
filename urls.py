from django.urls import path
from . import views
from .views import UserRegisterView
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

def test_view(request):
    return HttpResponse("Test OK")

urlpatterns = [
path('register/', UserRegisterView.as_view(), name='register'),
]

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = router.urls

