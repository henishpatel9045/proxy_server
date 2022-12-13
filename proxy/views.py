import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# # WP CHECK

class WpCheck(APIView):
    def post(self, request):
        print(type(request))
        data = request.data
        url = "https://21d5-2402-8100-26a3-d4c7-5503-3164-627b-4aaf.in.ngrok.io"
        url += "/wp/webhook"
        try:
            r = requests.post(url, json=data)
            print(data)
            return Response(status=200)
        except Exception as e:
            return Response(status=400)


    