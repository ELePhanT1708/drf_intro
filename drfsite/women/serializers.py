import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'category', 'content')


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_created_at = serializers.DateTimeField(read_only=True)
    time_updated_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        w = Women.objects.create(**validated_data)
        return w

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_created_at = validated_data.get('time_created_at', instance.time_created_at)
        instance.time_updated_at = validated_data.get('time_updated_at', instance.time_updated_at)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance


# def encode():
#     data_class = WomenModel('Ramil Khikmatullin', 'Ramil Khikmatullin : Student from BMSTU , has a bachelor degree '
#                                                   'in computer systems for automation in factories')
#     model_sr = WomenSerializer(data_class)
#
#     print(data_class, model_sr.data, type(model_sr.data), sep='\n')
#
#     return JSONRenderer().render(model_sr.data)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title": "Ramil Khikmatullin", "content": "Student from BMSTU , has a bachelor degree"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
