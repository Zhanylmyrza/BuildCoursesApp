from CoursesApp.models import Category,Branch,Contact,Course
from CoursesApp.serializer import CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CourseApi(APIView):
  def get(self,request):
    query_set=Course.objects.all()
    return Response({'Data':CourseSerializer(query_set,many=True).data})
  def post(self,request):
    serializer=CourseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

class CourseDetailView(APIView):
  def get(self,request,id=None): 
    courseId=get_object_or_404(Course,id=id)
    serializer = CourseSerializer(courseId)
    return Response(serializer.data)
    
  def delete(self, request, id=None):
    item = Course.objects.get(id=id).delete()   
    return Response({'id': str(id) + ' delete'})
