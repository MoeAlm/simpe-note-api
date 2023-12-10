from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .models import Note
from .serializers import NoteSerializer
from notes_api import permission


# Create your views here.

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class NoteViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (
        IsAuthenticated,
        permission.UpdateOwnStatus
    )

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
