from django.contrib import admin
from .models import Post,Tag,PostTagRelation
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(PostTagRelation)
#