from django.db import models


class selectionCount(models.Model):
    name = models.TextField()   # 경로 이름
    value = models.IntegerField(default=0)  # 변수 값

    def __str__(self):
        return self.name