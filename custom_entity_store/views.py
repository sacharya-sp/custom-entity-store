import logging

from django.http import JsonResponse
from rest_framework.generics import GenericAPIView


logger = logging.getLogger(__name__)


class PingView(GenericAPIView):
    def post(self, request):
        logger.info("Ping received")
        return JsonResponse(["json: " + request.body.decode("utf-8")], safe=False)
