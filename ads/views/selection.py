from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.permissions import IsCreatedBy
from ads.serializers import SelectionListSerializer, SelectionDetailSerializer, SelectionSerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    default_serializer = SelectionSerializer

    serializer_classes = {
        'list': SelectionListSerializer,
        'retrieve': SelectionDetailSerializer
    }
    default_permissions = [AllowAny()]
    permissions = {
        'create': [IsAuthenticated()],
        'update': [IsAuthenticated(), IsCreatedBy()],
        'partial_update': [IsAuthenticated(), IsCreatedBy()],
        'destroy': [IsAuthenticated(), IsCreatedBy()]
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permissions)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)