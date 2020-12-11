from rest_framework import serializers
from . import models


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = models.User(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = instance
        if validated_data['password'] is not None:
            user.set_password(validated_data['password'])
            user.save()
        return user


# class CourseSerializer(DynamicFieldsModelSerializer):
#     course_user = models.CourseUser
#
#     class Meta:
#         model = models.Course
#         fields = ['id', 'name', 'created']


# class LectionSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = models.Lection
#         fields = ['id', 'theme']
#
#
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Task
#         fields = ['id', 'task_content']
#
#
# class AnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Answer
#         fields = ['id', 'answer-content', 'mark', 'task', 'user']
#         depth = 1
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Comment
#         fields = ['task', 'user', 'comment_content']
#         depth = 1
