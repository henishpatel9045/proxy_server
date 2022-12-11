from django.http import HttpResponse

# Create your views here.
# # WP CHECK


def wp_check(request):
    challenge = request.GET.get("hub.challenge", 0)
    return HttpResponse(int(challenge), status=200)

