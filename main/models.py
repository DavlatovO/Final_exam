from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='teachers/')
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.full_name


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="1 oylik kurs narxi so'm da")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}: Muddati {self.duration} oy. Narxi: {self.price} so'm"


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    media = models.FileField(upload_to='videos/', blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Foydalanuvchilat darslarga izoh berish qismi"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Like(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField()
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('lesson', 'user'),)


    def __str__(self):
        return self.lesson


class Send_emails(models.Model):
    ...