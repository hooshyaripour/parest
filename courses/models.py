from django.db import models


class Course(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, default='notitle')
    description = models.TextField(blank=True)
    teacher = models.ForeignKey('auth.User', related_name='courses', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='images/courses/', null=True, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(default=1)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/courses/', null=True, blank=True)
    vfile_addr = models.CharField(max_length=256, blank=False, default='noaddr')
    vfile_size = models.IntegerField(default=0)  # Byte
    vfile_chunk_count = models.IntegerField(default=0)
    vfile_chunk_size = models.IntegerField(default=1)   # Byte
