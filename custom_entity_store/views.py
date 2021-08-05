import logging

from django.http import JsonResponse
from rest_framework.generics import GenericAPIView


logger = logging.getLogger(__name__)


class PingView(GenericAPIView):
    def get(self, request):
        logger.info("Ping received for custom-entity-store")
        return JsonResponse(["Ping received for custom-entity-store"], safe=False)
