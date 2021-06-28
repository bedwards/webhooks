import json
from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from .models import Webhook


@csrf_exempt
def create_webhook(request):
    data = json.loads(request.body.decode('utf-8'))
    webhook = Webhook.objects.create(url=data['url'])
    return HttpResponse(serialize('json', [webhook]),
                        content_type='application/json')
