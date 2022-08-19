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
    recruit_hashtag = models.ManyToManyField('Hashtag', blank=True)

    # 좋아요 구현
    like = models.ManyToManyField(User, related_name='likes', blank = True)
    like_count = models.PositiveIntegerField(default=0)

    # 북마크
    recruit_bookmark = models.ManyToManyField('Bookmark', related_name = 'bookmarks', blank = True)

    # 가입하기
    recruit_register = models.ManyToManyField('match.RecruitUser', related_name = 'recruit_users', blank = True)

    def __str__(self):
        return self.recruit_title

class Hashtag(models.Model):
    hashtag_content = models.CharField(max_length = 30, default="#")

    def __str__(self):
        return self.hashtag_content

class Bookmark(models.Model):
    bookmark_id = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name = 'bookmarks', null = True)
    bookmark_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'bookmarks', null = True)

    def __str__(self):
        return self.bookmark_user.nickname