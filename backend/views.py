from rest_framework import viewsets, permissions

from .serializers import AbonnementSerializer, ServiceSerializer


class AbonnementViewSet(viewsets.ModelViewSet):
    serializer_class = AbonnementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.abonnements.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)