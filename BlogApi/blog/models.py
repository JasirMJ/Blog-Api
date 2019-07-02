from django.db import models

# Create your models here.

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100,null=True)
    post_name = models.CharField(max_length=100,null=True)
    post_description  = models.CharField(max_length=200,null=True)
    post_tag_id = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.post_name

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name

class PostTagRelation(models.Model):
    id = models.AutoField(primary_key=True)
    id_post = models.CharField(max_length=200,default=None)
    id_tag = models.CharField(max_length=200,default=None)