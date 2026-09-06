from django.http import JsonResponse

def api_success(request):
    return JsonResponse({"message": "API is working completely fine!"})

def root_success(request):
    return JsonResponse({"message": "Welcome to the root endpoint!"})
