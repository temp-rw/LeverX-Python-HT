import base64

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators

from .hashers import UserPBKDF2PasswordHasher


def user_directory_path(instance, filename):
    return f"user_{instance.user.id}{filename}"


class User(models.Model):
    TEACHER = "teacher"
    STUDENT = "student"
    STAFF = "staff"
    USER_ROLE_CHOICES = [
        (TEACHER, "Teacher"),
        (STUDENT, "Student"),
        (STAFF, "Staff"),
    ]

    role = models.CharField(
        max_length=100,
        choices=USER_ROLE_CHOICES,
    )

    name = models.CharField(max_length=254)
    email = models.EmailField(unique=True, blank=False, validators=[validators.validate_email])
    password = models.CharField(max_length=500)

    def set_password(self, password):
        hasher = UserPBKDF2PasswordHasher()
        hash = hasher.encode(password=password, salt='salt').encode(encoding='utf-8')
        self.password = base64.b64encode(hash)

    def verify_password(self, password):
        hasher = UserPBKDF2PasswordHasher()
        hash = hasher.encode(password=password, salt='salt').encode(encoding='utf-8')
        password = base64.b64encode(hash)
        return self.password == password

    def __str__(self):
        return self.name


# class Course(models.Model):
#     name = models.CharField(max_length=254)
#     created = models.DateTimeField(auto_now_add=True)
#     users = models.ManyToManyField(User, through='CourseUser', through_fields=('course', 'user'))
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class CourseUser(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


# class Lection(models.Model):
#     theme = models.CharField(max_length=254)
#     pres_file = models.FileField(upload_to=user_directory_path)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.theme}"
#
#
# class Task(models.Model):
#     lection = models.ForeignKey(Lection, on_delete=models.CASCADE)
#     task_content = models.TextField()
#
#
# class Answer(models.Model):
#     answer_content = models.TextField()
#     mark = models.IntegerField(null=True)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.answer_content}"
#
#
# class Comment(models.Model):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
#     comment_content = models.TextField()
#
#     def __str__(self):
#         return f"{self.text}"
