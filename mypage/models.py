from django.db import models
from home.models import User

class Recruit(models.Model):
    recruit_writer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'recruits', null=True)
    recruit_date = models.DateTimeField(auto_now_add=True, blank=True)
    recruit_field_CHOICES = (
        ('study', '스터디'),
        ('club', '소모임'),
        ('project', '프로젝트'),
        ('survey', '설문조사')
    )
    recruit_field = models.CharField(max_length=20, choices=recruit_field_CHOICES, default='study')
    recruit_status_CHOICES = (
        ('ongoing', '모집중'),
        ('end', '모집완료'),
    )
    recruit_status = models.CharField(max_length=20, choices=recruit_status_CHOICES, default='ongoing')
    recruit_title = models.CharField(max_length=100)
    recruit_period_start = models.DateField()
    recruit_period_end = models.DateField()
    recruit_number = models.IntegerField()
    recruit_meeting_CHOICES = (
        ('offline', '대면'),
        ('online', '비대면'),
        ('TBD', '추후결정'),
    )
    recruit_meeting = models.CharField(max_length=20, choices=recruit_meeting_CHOICES, default='offline')
    recruit_content = models.TextField()
    recruit_image = models.ImageField(upload_to='images/', null=True, blank = True)

    def __str__(self):
        return self.recruit_title

class Hashtag(models.Model):
    hashtag_recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name = "hashtags", null=True)
    hashtag_writer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'hashtags', null=True)
    hashtag_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    hashtag_content = models.CharField(max_length = 30, unique=True, default="#")

    def __str__(self):
        return self.hashtag_content