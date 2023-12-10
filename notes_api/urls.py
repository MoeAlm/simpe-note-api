from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, UserLoginApiView

router = DefaultRouter()
router.register(r'note', NoteViewSet, basename='note')

urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
