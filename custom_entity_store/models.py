import logging
import uuid
from django.db import models


logger = logging.getLogger(__name__)


class Entity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.UUIDField(editable=False)
    data = models.JSONField(default={})
