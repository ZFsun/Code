from django.db import models


# Create your models here.

class Dataset(models.Model):
    path = models.CharField('路径', max_length=200, blank=True)


class Statistics(models.Model):
    """
    time weather scene
    """
    # time_num = models.IntegerField('时间')
    # weather_num = models.IntegerField('天气')
    # scene_num = models.IntegerField('场景')
    dawn_num = models.IntegerField('黎明', default=0)
    day_num = models.IntegerField('白天', default=0)
    dusk_num = models.IntegerField('黄昏', default=0)
    night_num = models.IntegerField('晚上', default=0)

    sunny_num = models.IntegerField('晴天', default=0)
    rain_num = models.IntegerField('雨天', default=0)
    overcast_num = models.IntegerField('阴天', default=0)
    cloudy_num = models.IntegerField('多云', default=0)

    urban_num = models.IntegerField('城市', default=0)
    hightway_num = models.IntegerField('高速', default=0)
    parking_num = models.IntegerField('停车场', default=0)
    othersway_num = models.IntegerField('其他', default=0)
