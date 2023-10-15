from django.db import models

class Board(models.Model):
    """掲示板モデル"""
    board_name = models.CharField(verbose_name='掲示板名', max_length=256)
    def __str__(self):
        return self.board_name