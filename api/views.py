from rest_framework.views import APIView
from retrieve_data.views import parse_events
from django.http import HttpResponse
from django.conf import settings


class EventApiView(APIView):
    http_method_names = ["post"]

    def post(self, request):
        body = request.body
        parse_events(body)
        try:
            with open(settings.CSV_FILE_NAME, "rb") as csv_file:
                response = HttpResponse(csv_file.read(), content_type="application/csv")
                response["Content-Disposition"] = f'attachment; filename="{settings.CSV_FILE_NAME})"'
                return response
        except OSError as e:
            raise (e)
