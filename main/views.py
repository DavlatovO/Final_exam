from django.shortcuts import render
from django.shortcuts import render
from .import models
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import TeacherSerializers, LikeSerializers, CommentSerializers, CourseSerializers, LessonSerializers
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action

# Start of viewset and Detail for Teacher model
class TeacherViewset(viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

class TeacherAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    
        

# Start of viewset and Detail for Course model
class CourseViewset(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    

class CourseAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    

# Start of viewset and Detail for Lesson model
class LessonViewset(viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    

class LessonAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticatedOrReadOnly] 


# Start of viewset and Detail for Comment model
class CommentViewset(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    

class CommentAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticatedOrReadOnly] 

# Start of viewset and Detail for Like model
class LikeViewset(viewsets.ModelViewSet):
    queryset = models.Like.objects.all()
    serializer_class = LikeSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    


class LikeAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Like.objects.all()
    serializer_class = LikeSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    



#Sending emails for test
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import smtplib
import logging

class SendEmailView(APIView):
    def post(self, request):
        sender_email = "davlatovoybek26@gmail.com"
        sender_password = "muco infq rxeg nyzh" 
        try:
            receiver_email = request.data.get("receiver_email")
            subject = request.data.get("subject")
            message = request.data.get("message")

            if not receiver_email or not subject or not message:
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

            text = f"Subject: {subject}\n\n{message}"

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, text)
            server.quit()

            return Response({'message': f'Email has been sent to {receiver_email}'}, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error("Failed to send email", exc_info=True)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from rest_framework.request import Request

from .models import Lesson  
from .serializers import LessonSerializers  
class SearchNews(APIView):
    def get(self, request: Request):
        word = request.query_params.get('word')
        lessons = Lesson.objects.filter(Q(description__icontains=word) | Q(name__icontains=word))
        return Response(LessonSerializers(lessons, many=True).data)
