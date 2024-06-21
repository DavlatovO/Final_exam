from rest_framework import serializers
from .import models

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['user', 'photo', 'full_name', 'phone', 'experience']


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['name', 'duration', 'price', 'teacher']   


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ['course', 'name', 'media', 'description']          


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['lesson', 'user', 'text']                  

        
class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = ['lesson', 'user', 'text', 'is_like', 'is_dislike']          



class SearchSerializer(serializers.Serializer):
    word = serializers.CharField(required=True)