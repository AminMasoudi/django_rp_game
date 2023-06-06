from django.http import JsonResponse
from helpers import LINKS
# Create your views here.

def index(request):
    if request.method == "GET":
        return JsonResponse({
            "msg":"W3LC0M3",
            "links": LINKS
            })