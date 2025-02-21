from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import entries

@csrf_exempt
def get_entry(request):
    if request.method == "POST":
        return JsonResponse({"key1":"value1"}, status=200)
    else:
        if 'name' in request.GET:
            name = request.GET['name']
            obj = entries.objects.filter(guestname=name)
            if len(obj) == 1:
                res = {
                    "guestname": obj[0].guestname,
                    "content":   obj[0].content
                }
            else:
                res = {"error_msg": "no record or duplicated records got"}
        else:
            res = {"error_msg": "parameter error"}
        return JsonResponse(res, status=200)
