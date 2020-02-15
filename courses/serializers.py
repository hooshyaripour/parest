from django.contrib.auth.models import User
from rest_framework import serializers

from courses.models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    teacher = serializers.ReadOnlyField(source='teacher.username')
    #blogs = Blog.objects.filter(author=author).values_list('id', flat=True)

    #highlight = serializers.HyperlinkedIdentityField( # new
    #    view_name='course-highlight', format='html')

    lessons = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('url', 'id', 'title', 'teacher', 'lessons' )


class UserSerializer(serializers.HyperlinkedModelSerializer): # new
    courses = serializers.HyperlinkedRelatedField( # new
        many=True, view_name='course-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'courses') # new