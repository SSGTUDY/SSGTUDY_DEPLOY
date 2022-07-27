# Generated by Django 4.0.6 on 2022-07-25 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0004_alter_recruit_recruit_writer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('match', '0002_alter_comment_comment_recruit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_recruit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mypage.recruit'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
