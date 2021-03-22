from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

from retrieve_data.views import parse_events


class EventApiView(APIView):
    http_method_names = ['post']

    def post(self, request):
        body = request.body
        response = parse_events(body)
        return Response({'countItem': len(response), 'Ids': response})

