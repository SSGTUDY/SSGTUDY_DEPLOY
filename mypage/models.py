from django.db import models

# Create your models here.
class Recruit(models.Model):
    recruit_field_CHOICES = (
        ('study', '스터디'),
        ('club', '소모임'),
        ('project', '프로젝트'),
        ('survey', '설문조사')
    )
    recruit_field = models.CharField(max_length=20, choices=recruit_field_CHOICES)
    recruit_status_CHOICES = (
        ('ongoing', '모집중'),
        ('end', '모집완료'),
    )
    recruit_status = models.CharField(max_length=20, choices=recruit_status_CHOICES)
    recruit_title = models.CharField(max_length=100)
    recruit_period_start = models.DateField()
    recruit_period_end = models.DateField()
    recruit_number = models.IntegerField()
    recruit_hashtag = models.ManyToManyField('Hashtag', blank = True)
    recruit_meeting_CHOICES = (
        ('offline', '대면'),
        ('online', '비대면'),
        ('TBD', '추후결정'),
    )
    recruit_meeting = models.CharField(max_length=20, choices=recruit_meeting_CHOICES)
    recruit_content = models.TextField()
    recruit_image = models.ImageField()

    def __str__(self):
        return self.recruit_title

class Hashtag(models.Model):
    hashtag = models.CharField(max_length=50)

    def __str__(self):
        return self.hashtag
