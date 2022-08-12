# Generated by Django 3.2.3 on 2022-08-12 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_content', models.CharField(max_length=1000)),
                ('comment_recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mypage.recruit')),
                ('comment_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomment_date', models.DateTimeField(auto_now_add=True)),
                ('recomment_content', models.CharField(max_length=1000)),
                ('recomment_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recomments', to='match.comment')),
                ('recomment_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recomments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
