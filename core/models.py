from django.db import models

class Man(models.Model):
    ip = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

class Message(models.Model):
    """
    储存聊天记录，避免一刷新就没了聊天记录
    用ip作为用户id

    1. 需要通过ip定位用户，不然不知道是谁发的
    2. 记录发送时间、发送人、内容
    """
    time = models.BigIntegerField()
    ip = models.CharField(max_length=30)
    room = models.CharField(max_length=20, default='001')
    content = models.CharField(max_length=300)
