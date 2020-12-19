from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.UserList.as_view(), name="user_list"),
    path('user/<pk>', views.UserDetail.as_view(), name='user_detail'),
]
