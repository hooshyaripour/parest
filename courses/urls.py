from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from courses import views

urlpatterns = [

    path('courses/', views.CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    path('courses/<int:pk>/highlight/',
         views.CourseHighlight.as_view(), name='course-highlight'), # new
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
