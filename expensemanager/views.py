from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    test_var = {
        "key1": "value1",
        "key2": "value2",
    }

    return JsonResponse(test_var)