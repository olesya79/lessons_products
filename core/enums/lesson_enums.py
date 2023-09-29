from django.db import models


class StatusOflesson(models.TextChoices):
    Viewed = 'Viewed', 'Viewed'
    Not_viewed = 'Not viewed', 'Not viewed'