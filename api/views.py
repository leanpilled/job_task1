from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .tasks import process_file
from .models import File
from .serializers import FileSerializer

    
@api_view(['GET'])
def get_files(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many = True)
    return JsonResponse({'files': serializer.data})


@api_view(['POST'])
def post_file(request):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        file_instance = serializer.save()
        process_file.delay(file_instance.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
