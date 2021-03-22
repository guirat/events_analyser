from rest_framework.views import APIView
from rest_framework.response import Response
from retrieve_data.views import parse_events
from django.http import HttpResponse


class EventApiView(APIView):
    http_method_names = ['post']

    def post(self, request, format=None):
        body = request.body
        result = parse_events(body)
        try:
            with open('events.csv', 'rb') as csv_file:
                response = HttpResponse(csv_file.read(), content_type='application/csv')
                response['Content-Disposition'] = f'attachment; filename="events.csv"'
                return response
        except OSError as e:
            raise(e)

