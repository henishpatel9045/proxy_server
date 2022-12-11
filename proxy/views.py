from django.http import HttpResponse
import requests

# Create your views here.
# # WP CHECK


def wp_check(request):
    data = request.POST
    url = "https://521a-2402-8100-26a3-d576-5b0f-e682-8794-941f.in.ngrok.io"
    url += "/wp/webhook"
    try:
        r = requests.post(url, data=data)
        print(data)
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=400)

