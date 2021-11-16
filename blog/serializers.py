


from django.db.models import fields
from django.db.models.fields.related import ForeignKey
from rest_framework import serializers

from blog.models import Post

class PostSirializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'