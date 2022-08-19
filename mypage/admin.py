from django.contrib import admin
from .models import Bookmark, Recruit, Hashtag

# Register your models here.
admin.site.register(Recruit)
admin.site.register(Hashtag)
admin.site.register(Bookmark)