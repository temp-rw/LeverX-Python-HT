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


# class CourseSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = models.Course
#         fields = ['id', 'name', 'created']
#
#
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
