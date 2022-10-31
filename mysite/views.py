from django.http import HttpResponse
from django.template import loader
from datetime import datetime, timezone


def index(request):
    current_date =datetime.now(timezone.utc).isoformat()
    return HttpResponse(f'<body>{current_date}</body>')