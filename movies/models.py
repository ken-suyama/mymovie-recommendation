from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Tag(models.Model):
    name = models.CharField('ジャンル', max_length=32)

    def __str__(self):
        return self.name

class Movies(models.Model):

    title = models.CharField('タイトル', max_length=100)
    rank = models.IntegerField('ランキング', default=0, null=True, blank=True)
    image = models.TextField('画像', null=True, blank=True)
    check = models.BooleanField('閲覧済', default=False)
    score = models.IntegerField('評価点', validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    date = models.TextField('公開日', null=True, blank=True)
    time = models.TextField('上映時間', null=True, blank=True)
    content = models.TextField('あらすじ', null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='ジャンル', blank=True)
    


    def __str__(self):
        return self.title


class Meta:
    db_table = 'movie'
    verbose_name = verbose_name_plural = '映画'
# Create your models here.
