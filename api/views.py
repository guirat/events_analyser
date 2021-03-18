from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response


class EventApiView(APIView):
    http_method_names = ['post']

    def post(self, request, format=None):
        return Response()


# @csrf_exempt
# def post(request):
#     if request.method == "POST":
#         response = ""
#     return JsonResponse(response)
