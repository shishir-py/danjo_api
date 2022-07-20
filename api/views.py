from rest_framework.response import Response
from rest_framework.decorators import api_view
from video.models import video
from .serializers import VideoSerializer


@api_view(['GET'])
def getData(request):
    items =video.objects.all()
    serializer =VideoSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer =VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)