from django.http import JsonResponse

def api_success(request):
    return JsonResponse({"message": "API is working completely okay!"})

def root_success(request):
    return JsonResponse({"message": "Welcome to the root/main endpoint!"})
