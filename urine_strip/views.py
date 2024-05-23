from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import ImageUploadSerializer
from PIL import Image
import cv2
import numpy as np

# Labels for each test on the strip
LABELS = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']

def index(request):
    return render(request, 'index.html')

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = ImageUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            image = Image.open(request.FILES['file'])
            colors = analyze_image(image)
            return JsonResponse(colors)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def analyze_image(image):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    colors = extract_colors(image)
    return colors

def extract_colors(image, num_colors=10):
    height, width, _ = image.shape
    segment_height = height // num_colors
    colors = {}

    for i in range(num_colors):
        segment = image[i*segment_height:(i+1)*segment_height, :]
        avg_color = segment.mean(axis=0).mean(axis=0)
        colors[LABELS[i]] = tuple(map(int, avg_color))

    return colors

def home(req):
    return render(req,'index.html')