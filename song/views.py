from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

@api_view(["GET"])
def songs_list(request):
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def songs_details(request, pk):
    song = get_object_or_404(Song, pk = pk)
    if request.method == "GET":
        serializer = SongSerializer(song)
        return Response(serializer.data)
