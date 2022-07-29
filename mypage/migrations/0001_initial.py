# Generated by Django 4.0.6 on 2022-07-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruit_field', models.CharField(choices=[('study', '스터디'), ('club', '소모임'), ('project', '프로젝트'), ('survey', '설문조사')], max_length=20)),
                ('recruit_status', models.CharField(choices=[('ongoing', '모집중'), ('end', '모집완료')], max_length=20)),
                ('recruit_title', models.CharField(max_length=100)),
                ('recruit_period_start', models.DateField(verbose_name='data published')),
                ('recruit_period_end', models.DateField(verbose_name='data published')),
                ('recruit_number', models.IntegerField()),
                ('recruit_meeting', models.CharField(choices=[('offline', '대면'), ('online', '비대면'), ('TBD', '추후결정')], max_length=20)),
                ('recruit_content', models.TextField()),
                ('recruit_image', models.ImageField(upload_to='')),
                ('recruit_hashtag', models.ManyToManyField(blank=True, to='mypage.hashtag')),
            ],
        ),
    ]
