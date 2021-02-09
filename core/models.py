from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)  ## auto_now_add : 모델이 생성된 날짜
    updated = models.DateTimeField(auto_now=True)  ## auto_now : 모델이 저장된 날짜

    class Meta:
        abstract = True